import asyncio

import asyncio
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection
from xoa_driver import enums

CHASSIS_IP = "10.10.10.10"
PORT_ID = "0/0"
USERNAME = "TEST"


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
    _stream_id = 0
    await cmd.PS_CREATE(handler, _mid, _pid, _stream_id).set()

    # Create a MACSec TX SC on the port
    _macsec_txsc_id = 0
    await cmd.P_MACSEC_TXSC_CREATE(handler, _mid, _pid, _macsec_txsc_id).set()

    # Create a MACSec RX SC on the port
    _macsec_rxsc_id = 0
    await cmd.P_MACSEC_RXSC_CREATE(handler, _mid, _pid, _macsec_rxsc_id).set()

    # Enable MACSec on the stream
    await cmd.PS_MACSEC_ENABLE(handler, _mid, _pid, _stream_id).set(on_off=enums.OnOff.ON)

    # Disable MACSec on the stream
    await cmd.PS_MACSEC_ENABLE(handler, _mid, _pid, _stream_id).set(on_off=enums.OnOff.OFF)

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