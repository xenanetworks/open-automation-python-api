# Obtain multiple modules

# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_test_modules = tester.modules.obtain_multiple(0, 2) # get reference to instance of module under slot 0
    for module in my_test_modules:
        if not isinstance(module, modules.ModuleChimera): # check if module is of types which we are suspecting
            print(module.info.media_info_list)
    # other code ...