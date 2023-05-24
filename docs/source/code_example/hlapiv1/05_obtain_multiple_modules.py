import asyncio
from xoa_driver import testers
from xoa_driver import modules

CHASSIS_IP = "demo.xenanetworks.com"
USERNAME = "xoa"
MODULE_IDS = [0,1]

async def main():
    # create tester instance and establish connection
    my_tester = await testers.L23Tester(CHASSIS_IP, USERNAME)
    
    # get reference to instance of module under slot 0 and 1
    my_modules = my_tester.modules.obtain_multiple(*MODULE_IDS) 

    for module in my_modules:
        # check if module is of types which we are suspecting
        if not isinstance(module, modules.ModuleChimera): 
            print(module.info.media_info_list)

if __name__ == "__main__":
    asyncio.run(main())