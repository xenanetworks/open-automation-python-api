import typing
from xoa_driver import enums

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