import asyncio

import asyncio
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection
from xoa_driver import enums
import pytest
import os


CHASSIS_IP = os.environ.get('TEST_CHASSIS_IP', '')
PORT_ID = os.environ.get('TEST_PORT_ID', '')
USERNAME = os.environ.get('TEST_USERNAME', '')


async def macsec_enable_test(handler, _mid, _pid, _stream_id):
    # Default MACSec state is OFF
    resp = await cmd.PS_MACSEC_ENABLE(handler, _mid, _pid, _stream_id).get()
    assert resp.on_off == enums.OnOff.OFF

    # Enable MACSec on the stream
    await cmd.PS_MACSEC_ENABLE(handler, _mid, _pid, _stream_id).set(on_off=enums.OnOff.ON)
    resp = await cmd.PS_MACSEC_ENABLE(handler, _mid, _pid, _stream_id).get()
    assert resp.on_off == enums.OnOff.ON

    # Disable MACSec on the stream
    await cmd.PS_MACSEC_ENABLE(handler, _mid, _pid, _stream_id).set(on_off=enums.OnOff.OFF)
    resp = await cmd.PS_MACSEC_ENABLE(handler, _mid, _pid, _stream_id).get()
    assert resp.on_off == enums.OnOff.OFF

async def macsec_assign_test(handler, _mid, _pid, _stream_id, _macsec_txsc_id):

    # Enable MACSec on the stream
    await cmd.PS_MACSEC_ASSIGN(handler, _mid, _pid, _stream_id).set(_macsec_txsc_id)
    resp = await cmd.PS_MACSEC_ASSIGN(handler, _mid, _pid, _stream_id).get()
    assert resp.tx_sc_index == _macsec_txsc_id

@pytest.mark.xfail(strict=True)
async def macsec_api_test(chassis: str, username: str, port_id: str, stop_event: asyncio.Event, password: str = "xena") -> None:

    # Access module
    _mid = int(port_id.split("/")[0])
    _pid = int(port_id.split("/")[1])

    # Connect to chassis                            
    handler = TransportationHandler(enable_logging=False)
    await establish_connection(handler, host=chassis, port=22606)
    await utils.apply(
        cmd.C_LOGON(handler).set(password),
        cmd.C_OWNER(handler).set(username),
    )

    # Reserve port 
    resp = await cmd.P_RESERVATION(handler, _mid, _pid).get()
    if resp.status == enums.ReservedStatus.RESERVED_BY_OTHER:
        await cmd.P_RESERVATION(handler, _mid, _pid).set(operation=enums.ReservedAction.RELINQUISH)
    if resp.status == enums.ReservedStatus.RESERVED_BY_YOU:
        await cmd.P_RESERVATION(handler, _mid, _pid).set(operation=enums.ReservedAction.RELEASE)
    await cmd.P_RESERVATION(handler, _mid, _pid).set(operation=enums.ReservedAction.RESERVE)

    # Reset port
    await cmd.P_RESET(handler, _mid, _pid).set()

    # Create a stream on port
    _stream_id = 1
    await cmd.PS_CREATE(handler, _mid, _pid, _stream_id).set()
    await cmd.PS_PACKETLENGTH(handler,_mid, _pid, _stream_id).set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000)
    await cmd.PS_ENABLE(handler, _mid, _pid, _stream_id).set(state=enums.OnOffWithSuppress.ON)

    # # Create a MACSec TX SC on the port
    _macsec_txsc_id = 1
    await cmd.P_MACSEC_TXSC_CREATE(handler, _mid, _pid, _macsec_txsc_id).set()

    # # Create a MACSec RX SC on the port
    _macsec_rxsc_id = 1
    await cmd.P_MACSEC_RXSC_CREATE(handler, _mid, _pid, _macsec_rxsc_id).set()

    await macsec_enable_test(handler, _mid, _pid, _stream_id)
    await macsec_assign_test(handler, _mid, _pid, _stream_id, _macsec_txsc_id)

    # Delete MACSec RX SC
    await cmd.P_MACSEC_RXSC_DELETE(handler, _mid, _pid, _macsec_rxsc_id).set()

    # Delete MACSec TX SC
    await cmd.P_MACSEC_TXSC_DELETE(handler, _mid, _pid, _macsec_txsc_id).set()

    # Release port
    await cmd.P_RESERVATION(handler, _mid, _pid).set(operation=enums.ReservedAction.RELEASE)


async def main():
    stop_event = asyncio.Event()
    try:
        await macsec_api_test(
            chassis=CHASSIS_IP,
            username=USERNAME,
            port_id=PORT_ID,
            stop_event=stop_event,
        )
    except KeyboardInterrupt:
        stop_event.set()

if __name__ == "__main__":
    asyncio.run(main())