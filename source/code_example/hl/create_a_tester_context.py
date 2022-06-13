# import available testers
from xoa_driver import testers

async def my_awesome_script():
    async with testers.L23Tester("192.168.1.200", "JonDoe") as tester: # create tester instance and establish connection
        print(tester.session.is_online)
        # other code ...
        # when leaving this block, the TCP connection will be closed.