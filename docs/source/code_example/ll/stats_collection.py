import asyncio
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection

async def background_task(handler: TransportationHandler):
    while True:
        print(await cmd.PT_STREAM(handler, 0, 0, 0).get()) # port 0/0, stream[0]
        print(await cmd.PR_TPLDTRAFFIC(handler, 0, 1, 0).get()) # # port 0/1, stream [0]
        await asyncio.sleep(1)

async def my_awesome_func():
    # my code ...
    handler = TransportationHandler(debug=False)
    await establish_connection(handler, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler).set("xena"),
        cmd.C_OWNER(handler).set("JonDoe"),
    ) # establish connection using username "JonDoe".

    asyncio.create_task(background_task(handler)) # put function to work in the background
    print("Task working in background")

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()