import asyncio

from xoa_driver import testers
from xoa_driver import modules

async def my_awesome_func():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    
    my_module = tester.modules.obtain(0)

    # check if module is of types which we are suspecting
    if not isinstance(my_module, modules.ModuleChimera):
        print(my_module.info.media_info_list)
        
        my_port = my_module.ports.obtain(0) # get reference to instance of port 0
        print(my_port.comment.get())

        # other code ...

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()