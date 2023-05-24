import asyncio
from xoa_driver import testers

CHASSIS_IP = "demo.xenanetworks.com"
USERNAME = "xoa"

async def main():
    # create tester instance and establish connection using username "xoa".
    my_tester = await testers.L23Tester(CHASSIS_IP, USERNAME)

    # gracefully close connection
    await my_tester.session.logoff() 

if __name__ == "__main__":
    asyncio.run(main())