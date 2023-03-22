import asyncio
from xoa_driver import testers

async def main():
    # create tester instance and establish connection
    async with testers.L23Tester("192.168.1.200", "xoa") as my_tester: 
        print(my_tester.session.is_online)
        # when leaving this block, the TCP connection will be closed.


if __name__ == "__main__":
    asyncio.run(main())