
import asyncio
from contextlib import suppress
from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import utils
from xoa_driver.enums import *
from xoa_driver import exceptions
from xoa_driver.hlfuncs import anlt, mgmt, anlt_ll_debug

CHASSIS_IP = "10.20.1.207"
USERNAME = "XOA"
MODULE_INDEX = 4
PORT_INDEX = 0

AN = True
LT = False
INTREACTIVE = False
LOOPBACK = False

async def my_test(stop_event: asyncio.Event):
    # create tester instance and establish connection
    tester = await testers.L23Tester(CHASSIS_IP, USERNAME) 

    # access the module on the tester
    module = tester.modules.obtain(MODULE_INDEX)

    # check if the module is of type Thor-400G-7S-1P[b]
    if isinstance(module, modules.MFreya800G1S1P_a):
        port = module.ports.obtain(PORT_INDEX)
        await mgmt.reserve_port(port, force=True)
        await mgmt.reset_port(port)
        r = await port.reservation.get()
        print(r.status)

        await anlt.link_recovery(port=port, enable=False)
        print(f"Link recovery: False")
        await asyncio.sleep(5)
        await anlt.lt_coeff_inc(port=port, lane=0, emphasis=LinkTrainCoeffs.PRE1)
        await anlt.do_anlt(
            port=port, 
            should_do_an=AN, 
            should_do_lt=LT, 
            an_allow_loopback=LOOPBACK, 
            lt_preset0_std=False, 
            lt_initial_modulations={"0": "pam2"}, 
            should_lt_interactive=INTREACTIVE
        )
        

        
async def main():
    stop_event =asyncio.Event()
    try:
        await my_test(stop_event)
    except KeyboardInterrupt:
        stop_event.set()


if __name__=="__main__":
    asyncio.run(main())