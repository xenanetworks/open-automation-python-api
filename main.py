import asyncio
import platform
from xoa_driver.cli import (
    an,
    an_log,
    anlt_status,
    connect,
    get_port,
    an_status,
    port_reserve,
    LinkTrainingSupported,
)
from xoa_driver.internals.core.transporter.funcs import apply


def set_windows_loop_policy() -> None:
    plat = platform.system().lower()

    if plat == "windows":
        policy = asyncio.WindowsSelectorEventLoopPolicy()
        asyncio.set_event_loop_policy(policy)


async def main() -> None:
    tester = await connect("l23", "87.61.110.114", "xena", "xena", 30606)
    for m in tester.modules:
        print(m.module_id)
        for p in m.ports:
            print("    ", p.kind.port_id)
    port = get_port(tester, 6, 0)

    # print(await an_status(port))
    tokens = await port_reserve(port)

    # tokens += await an(port, True, True)
    await apply(*tokens)
    print(await an_log(port))


if __name__ == "__main__":
    plat = platform.system().lower()
    if plat == "windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
