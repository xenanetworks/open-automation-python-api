import asyncio

from xoa_driver import testers
from xoa_driver import modules

async def my_awesome_func():
    # create tester instance and establish connection
    tester = await testers.L23Tester("192.168.1.200", "xoa") 

    for module in tester.modules:
        # check if module is of types which we are suspecting
        if not isinstance(module, modules.ModuleChimera): 
            print(module.info.media_info_list)
        else:
            print("Is chimera module")

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()