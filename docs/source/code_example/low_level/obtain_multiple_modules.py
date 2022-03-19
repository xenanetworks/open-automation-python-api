# import available module
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection

async def my_awesome_script():
    handler1 = TransportationHandler(debug=False)
    await establish_connection(handler1, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler1).set("xena"),
        cmd.C_OWNER(handler1).set("JonDoe"),
    ) # establish connection using username "JonDoe".

    print(await cmd.M_PORTCOUNT(handler, 0).get()) # get test module 0 port count
    print(await cmd.M_PORTCOUNT(handler, 1).get()) # get test module 1 port count
    print(await cmd.M_PORTCOUNT(handler, 2).get()) # get test module 2 port count

    # other code ...