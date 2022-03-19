# import available module
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection

async def my_awesome_script():
    handler = TransportationHandler(debug=False)
    await establish_connection(handler1, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler).set("xena"),
        cmd.C_OWNER(handler).set("JonDoe"),
    ) # establish connection using username "JonDoe".

    print(await cmd.P_SPEED_SUPPORTED(handler, 0, 0).get()) # get speeds supported of port 0/0
    print(await cmd.P_SPEED_SUPPORTED(handler, 0, 1).get())# get speeds supported of port 0/1

    # other code ...