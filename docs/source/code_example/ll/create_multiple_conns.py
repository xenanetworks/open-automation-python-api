import asyncio
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection

async def my_awesome_func():
    handler1 = TransportationHandler(debug=False)
    await establish_connection(handler1, "192.168.1.198")

    await utils.apply(
        cmd.C_LOGON(handler1).set("xena"),
        cmd.C_OWNER(handler1).set("JonDoe"),
    ) # establish connection using username "JonDoe".

    handler2 = TransportationHandler(debug=False)
    await establish_connection(handler2, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler2).set("xena"),
        cmd.C_OWNER(handler2).set("Alice"),
    ) # establish connection using username "Alice".

    handler3 = TransportationHandler(debug=False)
    await establish_connection(handler3, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler3).set("xena"),
        cmd.C_OWNER(handler3).set("Bob"),
    ) # establish connection using username "Bob".

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()