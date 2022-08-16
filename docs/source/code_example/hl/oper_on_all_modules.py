import asyncio

# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection

    for module in tester.modules:
        if not isinstance(module, modules.ModuleChimera): # check if module is of types which we are suspecting
            print(module.info.media_info_list)
        else:
            print("Is chimera module")
    
    # other code ...

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_script())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()