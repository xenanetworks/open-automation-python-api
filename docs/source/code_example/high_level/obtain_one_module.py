# Obtaining one module
# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_test_module = tester.modules.obtain(0) # get reference to instance of module under slot 0
    # check if module is of types which we are suspecting
    if not isinstance(my_test_module, modules.ModuleChimera):
        print(modules.info.media_info_list)
    # other code ...