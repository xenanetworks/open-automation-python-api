import asyncio

from xoa_driver import testers

async def my_awesome_func():
    async with testers.L23Tester("192.168.1.200", "JonDoe") as tester: # create tester instance and establish connection
        print(tester.session.is_online)
        # other code ...
        # when leaving this block, the TCP connection will be closed.
    

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()