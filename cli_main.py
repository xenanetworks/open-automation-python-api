import asyncio
from functools import partial
import inspect
import json
import platform
from typing import Any, Callable, Coroutine, Dict, List, Optional, Tuple
from xoa_driver.cli import (
    an,
    an_log,
    lt,
    lt_clear,
    lt_coeff_dec,
    lt_log,
    lt_nop,
    lt_coeff_inc,
    lt_preset,
    lt_preset0,
    lt_status,
    lt_trained,
    anlt_status,
    connect,
    get_port,
    an_status,
    port_reserve,
    LinkTrainingSupported,
    port_reset,
    txtap_get,
    txtap_set,
    link_recovery,
)
from xoa_driver.ports import GenericAnyPort
from xoa_driver.utils import apply
from xoa_driver.misc import Token


def set_windows_loop_policy() -> None:
    plat = platform.system().lower()

    if plat == "windows":
        policy = asyncio.WindowsSelectorEventLoopPolicy()
        asyncio.set_event_loop_policy(policy)


async def cli_main() -> None:
    await Client().run()


class KeepArgPartial(partial):
    pass


class Client:
    def __init__(self) -> None:
        self.current_tester = None
        self.current_port = None
        self.running = True
        self.method = {
            "connect": KeepArgPartial(connect, "l23"),
            "port_reserve": self.port_reserve,
            "port_reset": self.port_reset,
            "an": partial(self.check_port_apply, an),
            "anlt_status": partial(self.check_port_return, anlt_status),
            "an_status": partial(self.check_port_return, an_status),
            "an_log": partial(self.check_port_return, an_log),
            "lt": partial(self.check_port_apply, lt),
            "lt_status": partial(self.check_port_return, lt_status),
            "lt_clear": partial(self.check_port_apply, lt_clear),
            "lt_nop": partial(self.check_port_apply, lt_nop),
            "lt_coeff_inc": partial(self.check_port_apply, lt_coeff_inc),
            "lt_coeff_dec": partial(self.check_port_apply, lt_coeff_dec),
            "lt_preset": partial(self.check_port_apply, lt_preset),
            "lt_preset0": partial(self.check_port_apply, lt_preset0),
            "lt_trained": partial(self.check_port_apply, lt_trained),
            "lt_log": partial(self.check_port_return, lt_log),
            "txtap_get": partial(self.check_port_return, txtap_get),
            "txtap_set": partial(self.check_port_apply, txtap_set),
            "link_recovery": partial(self.check_port_apply, link_recovery),
            "quit": self.quit,
            "exit": self.quit,
            "q": self.quit,
            "help": self.help,
        }

    def parse_args(self, method: Callable, raw_args: List[str]) -> Dict:
        assert isinstance(method, Callable)
        if isinstance(method, partial) and (not isinstance(method, KeepArgPartial)):
            sig_dic = inspect.signature(method.args[0]).parameters
            overlook = len(method.args) - 1
        else:
            sig_dic = inspect.signature(method).parameters
            overlook = -1
        arg_dic = {}
        for i, r in enumerate(raw_args):
            v = None
            if r.startswith("--"):
                kr, v = r.split("=")
                k = kr.replace("--", "")
            else:
                k = list(sig_dic.keys())[i]
                v = r
            typing = sig_dic[k].annotation
            if typing == bool:
                if v in ("true", "enable"):
                    v = True
                else:
                    v = False
            arg_dic[k] = typing(v)

        for i, (k, para_dic) in enumerate( sig_dic.items()):
            if i <= overlook:
                continue
            default_val = para_dic.default
            if default_val != inspect.Parameter.empty and arg_dic.get(k) is None:
                v = default_val
                typing = sig_dic[k].annotation
                arg_dic[k] = typing(v)
        return arg_dic

    async def run_token(self, token_coro: Coroutine[Any, Any, List[Token]]):
        tokens = await token_coro
        await apply(*tokens)

    async def port_reserve(self, module_id: int, port_id: int):
        assert self.current_tester is not None
        self.current_port = get_port(self.current_tester, module_id, port_id)
        await self.run_token(port_reserve(self.current_port))

    async def port_reset(self, module_id: int, port_id: int):
        assert self.current_tester is not None
        self.current_port = get_port(self.current_tester, module_id, port_id)
        await self.run_token(port_reset(self.current_port))

    async def check_port_apply(self, token_coro, **kw):
        assert self.current_port is not None
        tokens = await partial(token_coro, self.current_port)(**kw)
        await apply(*tokens)

    async def check_port_return(self, token_coro, **kw):
        assert self.current_port is not None
        result = await partial(token_coro, self.current_port)(**kw)
        return result

    async def quit(self) -> None:
        self.running = False

    async def help(self, *lines: str) -> str:
        info = ""
        if not lines:
            info = "Please type 'help <command> for more information'. Available commands are: \n"
            info += "".join(
                [
                    f"    {k}\n"
                    for k in self.method
                    if k not in ("quit", "q", "exit", "help")
                ]
            )

        return info

    async def run(self) -> None:
        while self.running:
            input_string = input("xena:> ")
            lines = [i for i in input_string.split(" ") if i]
            if not lines:
                continue
            method_name, *raw_args = lines
            method = self.method.get(method_name.replace("-", "_"), None)
            if method is None:
                print("No commands match.")
                continue
            args = self.parse_args(method, raw_args)
            result = await method(**args)
            if method_name == "connect":
                self.current_tester = result
            elif method_name in ("an_log", "lt_log", "help"):
                print(result)
            elif method_name in ("an_status", "lt_status", "anlt_status", "txtap_get"):
                print(json.dumps(result, indent=2))
            else:
                print(method_name, " <OK>")


if __name__ == "__main__":
    plat = platform.system().lower()
    if plat == "windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(cli_main())
