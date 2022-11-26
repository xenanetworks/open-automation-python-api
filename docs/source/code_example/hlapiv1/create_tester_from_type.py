import asyncio

from xoa_driver import testers

async def my_awesome_func():
    tester = await testers.L23Tester("192.168.1.200", "xoa") # create tester instance and establish connection using username "xoa".

    # other code ...

    await tester.session.logoff() # gracefully close connection

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()