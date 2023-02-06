import asyncio
import socket
import typing
import dataclasses
from binascii import hexlify
from xoa_driver import testers
from xoa_driver import ports
from xoa_driver import utils
from xoa_driver import enums

class ResultError(typing.NamedTuple):
    dummy: int
    non_incre_seq_event_count: int
    swapped_seq_misorder_event_count: int
    non_incre_payload_packet_count: int

class Results(typing.NamedTuple):
    tx: int
    rx: int
    latency: int
    error: ResultError
    fcs: int

    @classmethod
    def from_data(cls, data):
        tx, rx, latency, error, fcs = data
        return cls(
            tx.packet_count_since_cleared, 
            rx.packet_count_since_cleared,
            latency.avg_val,
            ResultError(*dataclasses.astuple(error)),
            fcs.fcs_error_count
        )

async def prepare_port(port: "ports.GenericL23Port") -> None:
    if port.is_reserved_by_me():
        await port.reservation.set_release()
    elif not port.is_released():
        await port.reservation.set_relinquish()
    await utils.apply(
        port.reservation.set_reserve(),
        port.reset.set()
    )

class PortInfo(typing.NamedTuple):
    module_id: int
    port_id: int
    
    def __repr__(self):
        return f"{self.module_id}/{self.port_id}"

class PacketLength(typing.NamedTuple):
    length_type: enums.LengthType
    min_val: int 
    max_val: int
    
    @classmethod
    def from_string(cls, data: str):
        length_type, min_val, max_val = data.split()
        return cls(
            enums.LengthType[length_type],
            int(min_val),
            int(max_val)
        )
        
class Config(typing.NamedTuple):
    ip_address: str
    ports: typing.List[PortInfo]
    rate: int
    size: PacketLength
    duration: int

def read_config(path: str) -> "Config":
    config_dict = {}
    with open(path,'r+') as f:
        for conf in f:
            parsed = conf.strip('\n').split(':')
            if len(parsed) <= 1:
                continue
            config_dict[parsed[0]] = parsed[1]
        return Config(
            ip_address=config_dict["ip_address"],
            ports=[ 
                PortInfo(*map(int, port.split('/'))) 
                for port in config_dict['ports'].split(' ') 
            ],
            rate=int(config_dict["rate"]),
            size=PacketLength.from_string(config_dict["size"]),
            duration=int(config_dict["duration"])
        )

async def set_stream(port: "ports.GenericL23Port", size: tuple, header: str, rate: int) -> None:
    stream = await port.streams.create() # Create one stream at the port
    header_protocol = [ enums.ProtocolOption.ETHERNET, enums.ProtocolOption.IP]
    await utils.apply(
        stream.tpld_id.set(0), # Create the TPLD index of stream
        stream.packet.length.set(*size), # Configure the packet size
        stream.packet.header.protocol.set(header_protocol), # Configure the packet type
        stream.packet.header.data.set(header), # Configure the packet header
        stream.enable.set_on(), # Enable streams
        stream.rate.fraction.set(rate*10000) # Configure the stream rate
    )

async def clear_statistics(port: "ports.GenericL23Port") -> None:
    await utils.apply(
        port.statistics.tx.clear.set(),
        port.statistics.rx.clear.set()
    )

async def start_traffic(ports: typing.List["ports.GenericL23Port"]) -> None:
    await utils.apply(*[p.traffic.state.set_start() for p in ports])

async def stop_traffic(ports: typing.List["ports.GenericL23Port"]) -> None:
    await utils.apply(*[p.traffic.state.set_stop() for p in ports])


async def fetch_result(port: "ports.GenericL23Port") -> "Results":
    stream = port.streams.index(0) # Retrieve stream which we created for port
    tpld = port.statistics.rx.access_tpld(0) # before was port.reception_statistics.access_tpld(0)
    return Results.from_data(
        await utils.apply(
            port.statistics.tx.obtain_from_stream(stream).get(),
            tpld.traffic.get(), 
            tpld.latency.get(),
            tpld.errors.get(),
            port.statistics.rx.extra.get()
        )
    )


async def run_test(test_ports: typing.List["ports.GenericL23Port"], config: "Config") -> None:
    print("Start the scripting...")
    
    print ("Reserve the port...")
    await asyncio.gather(*[ prepare_port(p) for p in test_ports ])
    await asyncio.sleep(3)
    
    MAC1= '000000000002'
    MAC2= '000000000001'
    IP1 = '192.168.100.100'
    IP2 = '192.168.100.101'
    IP1 = hexlify(socket.inet_aton(IP1)).decode()
    IP2 = hexlify(socket.inet_aton(IP2)).decode()
    header1 = f'0x{MAC2}{MAC1}08004500002E000000007FFFF0B6{IP1}{IP2}' 
    header2 = f'0x{MAC1}{MAC2}08004500002E000000007FFFF0B6{IP2}{IP1}'
    
    print("Start to configure the streams...")
    await asyncio.gather(
        set_stream(test_ports[0], config.size, header1, config.rate),
        set_stream(test_ports[1], config.size, header2, config.rate)
    )
    
    print("Start the traffic...")
    await start_traffic(test_ports)
    await asyncio.sleep(2)
    
    await stop_traffic(test_ports)
    await asyncio.gather(*[clear_statistics(p) for p in test_ports]) # Sort of clear ports in parallel
    await asyncio.sleep(1)
    
    await start_traffic(test_ports)
    await asyncio.sleep(config.duration)
    
    await stop_traffic(test_ports)
    await utils.apply(*[p.reservation.set_release() for p in test_ports])
    
    await asyncio.sleep(2)
    
    ports_results = list(await asyncio.gather(*[ fetch_result(p) for p in test_ports ]))
    TX1 = ports_results[0].tx
    TX2 = ports_results[1].tx
    RX1 = ports_results[1].rx
    RX2 = ports_results[0].rx
    
    print('TX1: %s, TX2: %s, RX1: %s, RX2: %s,'%(TX1, TX2, RX1, RX2))

    Lost1 = TX1 - RX1
    Lost2 = TX2 - RX2
    
    output = (
        "----------------------------------------------------------------------------------------------------",
        f"Stream1 |  TX: {TX1}  |  RX: {RX1}  |  Lost : {Lost1} |  FCS: {ports_results[1].fcs}  |  Misoder Error: { ports_results[1].error.swapped_seq_misorder_event_count}  |  Payload Errors: {ports_results[1].error.non_incre_payload_packet_count}",
        "----------------------------------------------------------------------------------------------------",
        f"Stream2 |  TX: {TX2}  |  RX: {RX2}  |  Lost : {Lost2} |  FCS: {ports_results[0].fcs} |  Misoder Error: { ports_results[0].error.swapped_seq_misorder_event_count}  |  Payload Errors: {ports_results[0].error.non_incre_payload_packet_count}",
        "----------------------------------------------------------------------------------------------------",
        "Ending......."
    )
    print("\n".join(output))



async def start() -> None:
    config = read_config("./config.txt")
    print(config.ip_address)
    print(config.ports)
    print('Start to connect to the chassis...')
    async with testers.L23Tester(config.ip_address, "python_test_1", debug=True) as tester:
        test_ports = [ tester.modules.obtain(p.module_id).ports.obtain(p.port_id) for p in config.ports ]
        if any(isinstance(p, ports.PortChimera) for p in test_ports):
            raise ValueError("Please select other port. Chimera Ports can't be used in this test.")
        await run_test(test_ports, config) # type: ignore

def main():
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()