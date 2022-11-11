import asyncio
from contextlib import suppress
from xoa_driver.v2 import testers
from xoa_driver.internals.revisions import VALKYRIE_MODULES


async def main():
    print(VALKYRIE_MODULES)
    async with testers.L23Tester("demo.xenanetworks.com", username="ACO") as t:
        print(await t.capabilities.get())


if __name__ == "__main__":
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
