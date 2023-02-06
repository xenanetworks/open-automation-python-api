import asyncio
from xoa_driver import utils
from xoa_driver import enums
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection

async def my_awesome_func():
    handler = TransportationHandler(debug=False)
    await establish_connection(handler, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler).set("xena"),
        cmd.C_OWNER(handler).set("xoa"),
    ) # establish connection using username "xoa".

    reservation = await cmd.P_RESERVATION(handler, 0, 0).get() # port 0/0
    if not reservation == enums.ReservedStatus.RELEASED:
        await cmd.P_RESERVATION(handler, 0, 0).set(enums.ReservedAction.RELINQUISH)
    await cmd.P_RESERVATION(handler, 0, 0).set(enums.ReservedAction.RESERVE)

    await cmd.P_COMMENT(handler, 0, 0).set(comment="My Port")

    # other code ...

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()