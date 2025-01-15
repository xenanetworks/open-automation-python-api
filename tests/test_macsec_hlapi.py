import asyncio
from xoa_driver import testers, modules, ports, enums, exceptions
from xoa_driver.hlfuncs import mgmt
from contextlib import suppress
from xoa_driver.misc import Hex
import random, string, logging
from typing import Generator, Optional, Union, List, Dict, Any

#---------------------------
# GLOBAL PARAMS
#---------------------------
CHASSIS_IP = "10.165.153.50"
USERNAME = "macsec_hlapi"
PORT = "1/1"
DEBUG = True


async def macsec_txsc_description_test(port: ports.GenericL23Port, txsc_id: int) -> None:
    txsc_obj = port.macsec_txscs.obtain(txsc_id)
    value = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=30))
    await txsc_obj.config.description.set(value)
    resp = await txsc_obj.config.description.get()
    if resp.description == value:
        logging.info(f"{macsec_txsc_description_test.__name__} {value}: PASSED")
    else:
        logging.info(f"{macsec_txsc_description_test.__name__} {value}: FAILED")

async def macsec_rxsc_description_test(port: ports.GenericL23Port, rxsc_id: int) -> None:
    rxsc_obj = port.macsec_rxscs.obtain(rxsc_id)
    value = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=30))
    await rxsc_obj.config.description.set(value)
    resp = await rxsc_obj.config.description.get()
    if resp.description == value:
        logging.info(f"{macsec_rxsc_description_test.__name__} {value}: PASSED")
    else:
        logging.info(f"{macsec_rxsc_description_test.__name__} {value}: FAILED")
    
async def macsec_txsc_sci_mode_test(port: ports.GenericL23Port, txsc_id: int) -> None:
    txsc_obj = port.macsec_txscs.obtain(txsc_id)
    for value in enums.MACSecSCIMode:
        if value.name == "UNKNOWN":
            continue
        await txsc_obj.config.sci_mode.set(value)
        resp = await txsc_obj.config.sci_mode.get()
        if resp.mode == value:
            logging.info(f"{macsec_txsc_sci_mode_test.__name__} {value}: PASSED")
        else:
            logging.info(f"{macsec_txsc_sci_mode_test.__name__} {value}: FAILED")

async def macsec_txsc_sci_test(port: ports.GenericL23Port, txsc_id: int) -> None:
    txsc_obj = port.macsec_txscs.obtain(txsc_id)
    _temp_mac = random.randint(0, 0xFFFFFFFFFFFF)
    _temp_port = random.randint(0, 0xFFFF)
    value = Hex(f'{_temp_mac:012x}{_temp_port:04x}')
    await txsc_obj.config.sci.set(value)
    resp = await txsc_obj.config.sci.get()
    if resp.sci == value:
        logging.info(f"{macsec_txsc_sci_test.__name__} {value}: PASSED")
    else:
        logging.info(f"{macsec_txsc_sci_test.__name__} {value}: FAILED")

async def macsec_rxsc_sci_test(port: ports.GenericL23Port, rxsc_id: int) -> None:
    rxsc_obj = port.macsec_rxscs.obtain(rxsc_id)
    _temp_mac = random.randint(0, 0xFFFFFFFFFFFF)
    _temp_port = random.randint(0, 0xFFFF)
    value = Hex(f'{_temp_mac:012x}{_temp_port:04x}')
    await rxsc_obj.config.sci.set(value)
    resp = await rxsc_obj.config.sci.get()
    if resp.sci == value:
        logging.info(f"{macsec_rxsc_sci_test.__name__} {value}: PASSED")
    else:
        logging.info(f"{macsec_rxsc_sci_test.__name__} {value}: FAILED")

async def macsec_txsc_conf_offset_test(port: ports.GenericL23Port, txsc_id: int) -> None:
    txsc_obj = port.macsec_txscs.obtain(txsc_id)
    for value in (0,30,50):
        await txsc_obj.config.confidentiality_offset.set(value)
        resp = await txsc_obj.config.confidentiality_offset.get()
        if resp.offset == value:
            logging.info(f"{macsec_txsc_conf_offset_test.__name__} {value}: PASSED")
        else:
            logging.info(f"{macsec_txsc_conf_offset_test.__name__} {value}: FAILED")

async def macsec_rxsc_conf_offset_test(port: ports.GenericL23Port, rxsc_id: int) -> None:
    rxsc_obj = port.macsec_rxscs.obtain(rxsc_id)
    for value in (0,30,50):
        await rxsc_obj.config.confidentiality_offset.set(value)
        resp = await rxsc_obj.config.confidentiality_offset.get()
        if resp.offset == value:
            logging.info(f"{macsec_rxsc_conf_offset_test.__name__} {value}: PASSED")
        else:
            logging.info(f"{macsec_rxsc_conf_offset_test.__name__} {value}: FAILED")

async def macsec_txsc_ciphersuite_test(port: ports.GenericL23Port, txsc_id: int) -> None:
    txsc_obj = port.macsec_txscs.obtain(txsc_id)
    for value in enums.MACSecCipherSuite:
        if value.name == "UNKNOWN":
            continue
        await txsc_obj.config.cipher_suite.set(value)
        resp = await txsc_obj.config.cipher_suite.get()
        if resp.cipher_suite == value:
            logging.info(f"{macsec_txsc_ciphersuite_test.__name__} {value}: PASSED")
        else:
            logging.info(f"{macsec_txsc_ciphersuite_test.__name__} {value}: FAILED")

async def macsec_rxsc_ciphersuite_test(port: ports.GenericL23Port, rxsc_id: int) -> None:
    rxsc_obj = port.macsec_rxscs.obtain(rxsc_id)
    for value in enums.MACSecCipherSuite:
        if value.name == "UNKNOWN":
            continue
        await rxsc_obj.config.cipher_suite.set(value)
        resp = await rxsc_obj.config.cipher_suite.get()
        if resp.cipher_suite == value:
            logging.info(f"{macsec_rxsc_ciphersuite_test.__name__} {value}: PASSED")
        else:
            logging.info(f"{macsec_rxsc_ciphersuite_test.__name__} {value}: FAILED")

async def macsec_txsc_pn_test(port: ports.GenericL23Port, txsc_id: int) -> None:
    txsc_obj = port.macsec_txscs.obtain(txsc_id)
    for value in range(0, 1000):
        await txsc_obj.config.starting_pn.set(value)
        resp = await txsc_obj.config.starting_pn.get()
        if resp.start == value:
            logging.info(f"{macsec_txsc_pn_test.__name__} {value}: PASSED")
        else:
            logging.info(f"{macsec_txsc_pn_test.__name__} {value}: FAILED")

async def macsec_txsc_vlan_mode_test(port: ports.GenericL23Port, txsc_id: int) -> None:
    txsc_obj = port.macsec_txscs.obtain(txsc_id)
    for value in enums.MACSecVLANMode:
        if value.name == "UNKNOWN":
            continue
        await txsc_obj.config.vlan_mode.set(value)
        resp = await txsc_obj.config.vlan_mode.get()
        if resp.mode == value:
            logging.info(f"{macsec_txsc_vlan_mode_test.__name__} {value}: PASSED")
        else:
            logging.info(f"{macsec_txsc_vlan_mode_test.__name__} {value}: FAILED")

async def macsec_txsc_rekey_mode_test(port: ports.GenericL23Port, txsc_id: int) -> None:
    txsc_obj = port.macsec_txscs.obtain(txsc_id)
    for value in enums.MACSecRekeyMode:
        if value.name == "UNKNOWN":
            continue
        await txsc_obj.config.rekey_mode.set(value)
        resp = await txsc_obj.config.rekey_mode.get()
        if resp.mode == value:
            logging.info(f"{macsec_txsc_rekey_mode_test.__name__} {value}: PASSED")
        else:
            logging.info(f"{macsec_txsc_rekey_mode_test.__name__} {value}: FAILED")

async def macsec_txsc_encrypt_mode_test(port: ports.GenericL23Port, txsc_id: int) -> None:
    txsc_obj = port.macsec_txscs.obtain(txsc_id)
    for value in enums.MACSecEncryptionMode:
        if value.name == "UNKNOWN":
            continue
        await txsc_obj.config.encryption_mode.set(value)
        resp = await txsc_obj.config.encryption_mode.get()
        if resp.mode == value:
            logging.info(f"{macsec_txsc_encrypt_mode_test.__name__} {value}: PASSED")
        else:
            logging.info(f"{macsec_txsc_encrypt_mode_test.__name__} {value}: FAILED")

async def macsec_txsc_sak_test(port: ports.GenericL23Port, txsc_id: int) -> None:
    txsc_obj = port.macsec_txscs.obtain(txsc_id)
    await txsc_obj.sak_type.set(sak_key_type=enums.MACSecSAKKeyType.SAK128)
    _key_indices = [0,1,2,3]
    await txsc_obj.sak_indices.set(key_indices=_key_indices)
    for i in _key_indices:
        resp = await txsc_obj.access_sak_value(i).get()
        if resp.sak_key_value == "00"*16:
            logging.info(f"{macsec_txsc_sak_test.__name__} default all-zero: PASSED")
        else:
            logging.info(f"{macsec_txsc_sak_test.__name__} default all-zero: FAILED")
    for i in _key_indices:
        value = Hex("000102030405060708FF0102030405060708")
        await txsc_obj.access_sak_value(i).set(value)
        resp = await txsc_obj.access_sak_value(i).get()
        if resp.sak_key_value == value:
            logging.info(f"{macsec_txsc_sak_test.__name__} {value}: PASSED")
        else:
            logging.info(f"{macsec_txsc_sak_test.__name__} {value}: FAILED")

async def macsec_rxsc_sak_test(port: ports.GenericL23Port, rxsc_id: int) -> None:
    rxsc_obj = port.macsec_rxscs.obtain(rxsc_id)
    await rxsc_obj.sak_type.set(sak_key_type=enums.MACSecSAKKeyType.SAK128)
    _key_indices = [0,1,2,3]
    await rxsc_obj.sak_indices.set(key_indices=_key_indices)
    for i in _key_indices:
        resp = await rxsc_obj.access_sak_value(i).get()
        if resp.sak_key_value == "00"*16:
            logging.info(f"{macsec_rxsc_sak_test.__name__} default all-zero: PASSED")
        else:
            logging.info(f"{macsec_rxsc_sak_test.__name__} default all-zero: FAILED")
    for i in _key_indices:
        value = Hex("000102030405060708FF0102030405060708")
        await rxsc_obj.access_sak_value(i).set(value)
        resp = await rxsc_obj.access_sak_value(i).get()
        if resp.sak_key_value == value:
            logging.info(f"{macsec_rxsc_sak_test.__name__} {value}: PASSED")
        else:
            logging.info(f"{macsec_rxsc_sak_test.__name__} {value}: FAILED")

async def macsec_rxsc_tpldid_test(port: ports.GenericL23Port, rxsc_id: int) -> None:
    rxsc_obj = port.macsec_rxscs.obtain(rxsc_id)
    for value in range(0, 255):
        await rxsc_obj.config.tpld_id.set(value)
        resp = await rxsc_obj.config.tpld_id.get()
        if resp.tpld_id == value:
            logging.info(f"{macsec_rxsc_tpldid_test.__name__} {value}: PASSED")
        else:
            logging.info(f"{macsec_rxsc_tpldid_test.__name__} {value}: FAILED")

async def macsec_txsc_default_value_test(port: ports.GenericL23Port, txsc_id: int) -> None:
    logging.info(f"TX SC {txsc_id} Default Value Test")
    txsc_obj = port.macsec_txscs.obtain(txsc_id)
    resp = await txsc_obj.config.description.get()
    logging.info(resp.description)
    resp = await txsc_obj.config.sci_mode.get()
    logging.info(resp.mode)
    resp = await txsc_obj.config.sci.get()
    logging.info(resp.sci)
    resp = await txsc_obj.config.confidentiality_offset.get()
    logging.info(resp.offset)
    resp = await txsc_obj.config.cipher_suite.get()
    logging.info(resp.cipher_suite)
    resp = await txsc_obj.config.starting_pn.get()
    logging.info(resp.start)
    resp = await txsc_obj.config.vlan_mode.get()
    logging.info(resp.mode)
    resp = await txsc_obj.config.rekey_mode.get()
    logging.info(resp.mode)
    resp = await txsc_obj.config.encryption_mode.get()
    logging.info(resp.mode)
    resp = await txsc_obj.sak_indices.get()
    logging.info(resp.key_indices)

async def macsec_rxsc_default_value_test(port: ports.GenericL23Port, rxsc_id: int) -> None:
    logging.info(f"RX SC {rxsc_id} Default Value Test")
    rxsc_obj = port.macsec_rxscs.obtain(rxsc_id)
    resp = await rxsc_obj.config.description.get()
    logging.info(resp.description)
    resp = await rxsc_obj.config.sci.get()
    logging.info(resp.sci)
    resp = await rxsc_obj.config.confidentiality_offset.get()
    logging.info(resp.offset)
    resp = await rxsc_obj.config.cipher_suite.get()
    logging.info(resp.cipher_suite)
    resp = await rxsc_obj.sak_indices.get()
    logging.info(resp.key_indices)

async def macsec_stream_test(port: ports.GenericL23Port, stream_id: int, txsc_id: int) -> None:
    stream_obj = port.streams.obtain(stream_id)
    _tpld_id = 10
    _packet_size = 64
    await stream_obj.tpld_id.set(test_payload_identifier=_tpld_id)
    await stream_obj.packet.length.set(length_type=enums.LengthType.FIXED, max_val=_packet_size, min_val=_packet_size)
    for value in enums.OnOff:
        if value.name == "UNKNOWN":
            continue
        await stream_obj.macsec.enable.set(value)
        resp = await stream_obj.macsec.enable.get()
        if resp.on_off == value:
            logging.info(f"{macsec_stream_test.__name__} {value}: PASSED")
        else:
            logging.info(f"{macsec_stream_test.__name__} {value}: FAILED")
    await stream_obj.macsec.enable.set(on_off=enums.OnOff.ON)
    await stream_obj.macsec.assign.set(tx_sc_index=txsc_id)
    resp = await stream_obj.macsec.assign.get()
    if resp.tx_sc_index == txsc_id:
        logging.info(f"{macsec_stream_test.__name__} {txsc_id}: PASSED")
    else:
        logging.info(f"{macsec_stream_test.__name__} {txsc_id}: FAILED")


async def macsec_hlapi_test(
        chassis_ip: str, 
        username: str, 
        port_str: str,
        debug: bool = False,
        ):

    # configure basic logger
    logging.basicConfig(
        format="%(asctime)s  %(message)s",
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler(filename=f"{macsec_hlapi_test.__name__}.log", mode="a"),
            logging.StreamHandler()]
        )
    
    # Establish connection to a Valkyrie tester using Python context manager
    # The connection will be automatically terminated when it is out of the block
    async with testers.L23Tester(host=chassis_ip, username=username, password="xena", port=22606, enable_logging=debug) as tester:

        # Access module
        _mid = int(port_str.split("/")[0])
        _pid = int(port_str.split("/")[1])

        module_obj = tester.modules.obtain(_mid)

        if isinstance(module_obj, modules.E100ChimeraModule):
            return

        # Get the port
        port_obj = module_obj.ports.obtain(_pid)

        logging.info(f"Start")
        await mgmt.reserve_port(port_obj)
        await mgmt.reset_port(port_obj)

        try:
            # await port_obj.macsec_txscs.server_sync()
            txsc_obj = await port_obj.macsec_txscs.create()
            txsc_index = txsc_obj.idx
            # await macsec_txsc_default_value_test(port_obj, txsc_index)
            logging.info(f"-------------------")
            await macsec_txsc_description_test(port_obj, txsc_index)
            await macsec_txsc_sci_mode_test(port_obj, txsc_index)
            await macsec_txsc_sci_test(port_obj, txsc_index)
            await macsec_txsc_conf_offset_test(port_obj, txsc_index)
            await macsec_txsc_ciphersuite_test(port_obj, txsc_index)
            await macsec_txsc_pn_test(port_obj, txsc_index)
            await macsec_txsc_vlan_mode_test(port_obj, txsc_index)
            await macsec_txsc_rekey_mode_test(port_obj, txsc_index)
            await macsec_txsc_encrypt_mode_test(port_obj, txsc_index)
            await macsec_txsc_sak_test(port_obj, txsc_index)
            logging.info(f"-------------------")
            stream_obj = await port_obj.streams.create()
            stream_index = stream_obj.idx
            await macsec_stream_test(port_obj, stream_index, txsc_index)
            logging.info(f"-------------------")
            rxsc_obj = await port_obj.macsec_rxscs.create()
            rxsc_index = rxsc_obj.idx
            # await macsec_rxsc_default_value_test(port_obj, rxsc_index)
            logging.info(f"-------------------")
            await macsec_rxsc_description_test(port_obj, rxsc_index)
            await macsec_rxsc_sci_test(port_obj, rxsc_index)
            await macsec_rxsc_conf_offset_test(port_obj, rxsc_index)
            await macsec_rxsc_ciphersuite_test(port_obj, rxsc_index)
            await macsec_rxsc_tpldid_test(port_obj, rxsc_index)
            await macsec_txsc_sak_test(port_obj, txsc_index)
            logging.info(f"-------------------")

            # await port_obj.traffic.state.set_start()

            resp = await txsc_obj.stats.get()
            logging.info(f"TX SC {txsc_index} Stats: {resp}")

            resp = await rxsc_obj.stats.get()
            logging.info(f"RX SC {rxsc_index} Stats: {resp}")
            
            resp = await port_obj.statistics.tx.macsec.total.get()
            logging.info(f"TX Total Stats: {resp}")
            
            resp = await port_obj.statistics.rx.macsec.total.get()
            logging.info(f"RX Total Stats: {resp}")
            
            logging.info(f"-------------------")
            await asyncio.sleep(5)
            await port_obj.statistics.tx.macsec.clear.set()
            await port_obj.statistics.rx.macsec.clear.set()
            logging.info(f"TX & RX Stats Cleared")

            resp = await txsc_obj.stats.get()
            logging.info(f"TX SC {txsc_index} Stats: {resp}")

            resp = await rxsc_obj.stats.get()
            logging.info(f"RX SC {rxsc_index} Stats: {resp}")
            
            resp = await port_obj.statistics.tx.macsec.total.get()
            logging.info(f"TX Total Stats: {resp}")
            
            resp = await port_obj.statistics.rx.macsec.total.get()
            logging.info(f"RX Total Stats: {resp}")
            logging.info(f"-------------------")
            logging.info(f"End")

            # await port_obj.traffic.state.set_stop()

        except Exception as e:
            logging.info(e)

        # release the port
        await mgmt.free_port(port_obj)


async def main():
    stop_event = asyncio.Event()
    try:
        await macsec_hlapi_test(
            chassis_ip=CHASSIS_IP,
            username=USERNAME,
            port_str=PORT,
            debug=DEBUG
            )
    except KeyboardInterrupt:
        stop_event.set()


if __name__ == "__main__":
    asyncio.run(main())