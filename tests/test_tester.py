import sys
import os
import asyncio
import pytest
import time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports


async def test_tester():
    a = time.time()
    async with testers.L23Tester("192.168.1.198", "JonDoe") as tester:
        print("01.", await tester.name.get())
        print("02.", await tester.comment.get())
        print("03.", await tester.version_no.get())
        print("04.", await tester.version_no_minor.get())
        print("05.", await tester.serial_no.get())
        print("06.", await tester.build_string.get())
        print("07.", await tester.model.get())
        print("08.", await tester.management_interface.ip_address.get())
        print("10.", await tester.management_interface.dhcp.get())
        print("12.", await tester.management_interface.macaddress.get())
        print("13.", tester.info.reserved_by)
        for m in tester.modules:
            print(f"        {{{m.module_id}}}")
            print("    2.", await m.model.get())
            if not isinstance(m, modules.ModuleChimera): 
                print("    3.", await m.revision.get())
            print("    4.", await m.version_number.get())
            print("    5.", await m.serial_number.get())
            print("    6.", m.info.reserved_by)
            print()
            for p in m.ports:
                print(f"        {{{p.kind.port_id}}}")
                print("        1.", await p.comment.get())
                print("        2.", p.info. reserved_by)
                print("        3.", await p.interface.get())
                if not isinstance(p, ports.PortChimera): 
                    print("        4.", p.info.port_possible_speeds)
                    print("        5.", p.info.sync_status)
                    print("        6.", p.info.traffic_state)
                print()
    print(time.time() - a)

# %%
def main():
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test_tester())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    pytest.main(main())
