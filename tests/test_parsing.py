import asyncio
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from xoa_driver.internals.core.commands import PR_TPLDLATENCY
from xoa_driver.internals.core.protocol import command_builders
from xoa_driver.internals.core.protocol.struct_header import ResponseHeader
from xoa_driver import misc

async def test_tester():
    header = ResponseHeader.from_buffer_copy(b'XENA\x00\x01\x000\x03\xf6\x02\x05\x00\x00\x00\x87')
    body = b'\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xffi\xff\xff\xff\xff\xff\xff\xff\xf5\x00\x00\x00\x00\x00\x00\x01\x83\xff\xff\xff\xff\x80\x00\x00\x00\xff\xff\xff\xff\x80\x00\x00\x00\xff\xff\xff\xff\x80\x00\x00\x00'
    result = command_builders.build_from_bytes(PR_TPLDLATENCY, header, body)
    print(result)

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.set_debug(True)
        loop.run_until_complete(test_tester())
    except KeyboardInterrupt:
        pass

def check_time():
    import timeit
    a = timeit.timeit('main()', globals=globals(), number=1)
    print(a)

if __name__ == "__main__":
    main()