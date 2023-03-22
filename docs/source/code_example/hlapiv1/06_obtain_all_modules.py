import asyncio
from xoa_driver import testers
from xoa_driver import modules

CHASSIS_IP = "demo.xenanetworks.com"
USERNAME = "xoa"

async def main():
    # create tester instance and establish connection
    my_tester = await testers.L23Tester(CHASSIS_IP, USERNAME)

    for module in my_tester.modules:
        # check if module is of types which we are suspecting
        if not isinstance(module, modules.ModuleChimera): 
            print(module.info.media_info_list)
        else:
            print("Is chimera module")

if __name__ == "__main__":
    asyncio.run(main())