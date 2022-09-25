import asyncio
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection

async def my_awesome_func():
    handler = TransportationHandler(debug=False)
    await establish_connection(handler, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler).set("xena"),
        cmd.C_OWNER(handler).set("JonDoe"),
    ) # establish connection using username "JonDoe".

    print(await cmd.M_PORTCOUNT(handler, 0).get()) # get test module 0 port count

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