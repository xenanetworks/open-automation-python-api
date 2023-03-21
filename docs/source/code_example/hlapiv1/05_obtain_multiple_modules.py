import asyncio
from xoa_driver import testers
from xoa_driver import modules

async def main():
    # create tester instance and establish connection
    my_tester = await testers.L23Tester("192.168.1.200", "xoa") 
    
    # get reference to instance of module under slot 0 and 2
    my_modules = my_tester.modules.obtain_multiple(0, 2) 

    for module in my_modules:
        # check if module is of types which we are suspecting
        if not isinstance(module, modules.ModuleChimera): 
            print(module.info.media_info_list)

if __name__ == "__main__":
    asyncio.run(main())