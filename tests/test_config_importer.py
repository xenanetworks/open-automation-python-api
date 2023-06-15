import asyncio
import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # IMPORTANT: Suppose to stay before driver import

from xoa_driver.functions.mgmt import reserve_port, reserve_module, reserve_tester
from xoa_driver.testers import L23Tester
from typing import Coroutine



from xoa_driver.functions.config_cli_convert import (
    read_commands_from_file,
    read_commands_from_string,
    upload_port_config_from_string,
    upload_port_config_from_file,
    upload_module_config_from_string,
    upload_module_config_from_file,
    upload_tester_config_from_string,
    upload_tester_config_from_file,
)  # noqa: E402


@pytest.mark.asyncio
async def test_read_commands_from_file() -> None:
    path = os.path.join(os.path.dirname(__file__), "test_clis", "test_all_commands.txt")
    for c in read_commands_from_file(path):
        print(c)
        print(c.as_request())


@pytest.mark.asyncio
async def test_read_commands_from_string() -> None:
    path = os.path.join(os.path.dirname(__file__), "test_clis", "test_all_commands.txt")
    with open(path, "r") as f:
        content = f.read()
        for c in read_commands_from_string(content):
            print(c)
            print(c.as_request())


@pytest.mark.asyncio
async def test_upload_port_config_from_file() -> None:
    path = os.path.join(os.path.dirname(__file__), "test_clis", "test_port_config.txt")
    module = (await L23Tester("192.168.1.198", "Happy", enable_logging=True)).modules.obtain(1)
    port = module.ports.obtain(0)
    await reserve_port(port, True)
    await upload_port_config_from_file(port, path)


@pytest.mark.asyncio
async def test_upload_port_config_from_string() -> None:
    path = os.path.join(os.path.dirname(__file__), "test_clis", "test_port_config.txt")
    with open(path, "r") as f:
        content = f.read()
        module = (await L23Tester("192.168.1.198", "Happy", enable_logging=True)).modules.obtain(1)
        port = module.ports.obtain(0)
        await reserve_port(port, True)
        await upload_port_config_from_string(port, content)


@pytest.mark.asyncio
async def test_upload_module_config_from_file() -> None:
    path = os.path.join(os.path.dirname(__file__), "test_clis", "test_module_config.txt")
    module = (await L23Tester("192.168.1.198", "Happy", enable_logging=True)).modules.obtain(1)
    await reserve_module(module, True)
    await upload_module_config_from_file(module, path)


@pytest.mark.asyncio
async def test_upload_module_config_from_string() -> None:
    path = os.path.join(os.path.dirname(__file__), "test_clis", "test_module_config.txt")
    with open(path, "r") as f:
        content = f.read()
        module = (await L23Tester("192.168.1.198", "Happy", enable_logging=True)).modules.obtain(1)
        await reserve_module(module, True)
        await upload_module_config_from_string(module, content)


@pytest.mark.asyncio
async def test_upload_tester_config_from_string() -> None:
    path = os.path.join(os.path.dirname(__file__), "test_clis", "test_tester_config.txt")
    with open(path, "r") as f:
        content = f.read()
        tester = await L23Tester("192.168.1.198", "Happy", enable_logging=True)
        await reserve_tester(tester, True)
        await upload_tester_config_from_string(tester, content)


@pytest.mark.asyncio
async def test_upload_tester_config_from_file() -> None:
    path = os.path.join(os.path.dirname(__file__), "test_clis", "test_tester_config.txt")
    tester = await L23Tester("192.168.1.198", "Happy", enable_logging=True)
    await reserve_tester(tester, True)
    await upload_tester_config_from_file(tester, path)


def run(method: Coroutine) -> None:
    import platform

    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(method)


if __name__ == "__main__":
    run(test_upload_module_config_from_file())
    # run(test_upload_module_config_from_string())
    # run(test_upload_port_config_from_file())
    # run(test_upload_port_config_from_string())
    # run(test_upload_tester_config_from_string())
    # run(test_upload_tester_config_from_file())
