import asyncio
from functools import partial
import inspect
import json
import platform
from typing import Any, Callable, Coroutine, Dict, List, Optional, Tuple
from xoa_driver.util import (
    an_config,
    an_log,
    lt_config,
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
            "an": partial(self.check_port_apply, an_config),
            "anlt_status": partial(self.check_port_return, anlt_status),
            "an_status": partial(self.check_port_return, an_status),
            "an_log": partial(self.check_port_return, an_log),
            "lt": partial(self.check_port_apply, lt_config),
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
        self.construct_doc_dic()

    def parse_args(self, method: Callable, raw_args: List[str]) -> Dict:
        assert isinstance(method, Callable), "The 'method' para should be a callable."
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
                k = kr.replace("--", "").replace('-', '_')
            else:
                valid_para = list(sig_dic.keys())[overlook + 1 :]
                k = valid_para[i]
                v = r
            typing = sig_dic[k].annotation
            if typing == bool:
                if v.lower() in ("true", "enable"):
                    v = True
                else:
                    v = False
            arg_dic[k] = typing(v)

        for j, (k, para_dic) in enumerate(sig_dic.items()):
            if j <= overlook:
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
        """
            --module:int
            --port:int
        - Reserve the port to configure
        """
        assert self.current_tester is not None, "Please 'connect' a tester."
        self.current_port = get_port(self.current_tester, module_id, port_id)
        await self.run_token(port_reserve(self.current_port))

    async def port_reset(self, module_id: int, port_id: int):
        """
            --module:int
            --port:int
        - Reset the port
        """
        assert self.current_tester is not None, "Please 'connect' a tester."
        self.current_port = get_port(self.current_tester, module_id, port_id)
        await self.run_token(port_reset(self.current_port))

    async def check_port_apply(self, token_coro, **kw):
        assert self.current_port is not None, "Please 'port_reserve' a port."
        tokens = await partial(token_coro, self.current_port)(**kw)
        await apply(*tokens)

    async def check_port_return(self, token_coro, **kw):
        assert self.current_port is not None, "Please 'port_reserve' a port."
        result = await partial(token_coro, self.current_port)(**kw)
        return result

    async def quit(self) -> None:
        self.running = False

    def construct_doc_dic(self) -> None:
        doc_dic = {}
        for k, method in self.method.items():
            if k not in ("quit", "q", "exit"):
                if isinstance(method, KeepArgPartial):
                    func = method.func
                elif isinstance(method, partial):
                    func = method.args[0]
                else:
                    func = method
                info = ""
                doc = inspect.getdoc(func)
                if doc:
                    for i in doc.split("\n"):
                        info += f"    {i}\n"
                    info += "-" * 79
                doc_dic[k] = info
        self.doc_dic = doc_dic

    async def help(self, line: str = "") -> str:
        """
        - Please type 'help <command>' for more information.
        """
        if not line:
            info = "Please type 'help <command>' for more information. Available commands are: \n"
            for k, v in self.doc_dic.items():
                info += f"{k}\n"
                info += f"{v}\n"
        else:
            key = line.replace("-", "_")
            info = f"{key}\n"
            info += self.doc_dic.get(key, "")
            if info is None:
                return "No commands match."
        return info

    async def run(self) -> None:
        while self.running:
            try:
                input_string = input("xena:> ")
                lines = [i for i in input_string.split(" ") if i]
                if not lines:
                    continue
                method_name, *raw_args = lines
                replaced_name = method_name.replace("-", "_")
                method = self.method.get(replaced_name, None)
                if method is None:
                    print("No commands match.")
                    continue
                kw = self.parse_args(method, raw_args)
                result = await method(**kw)
                if replaced_name == "connect":
                    self.current_tester = result
                    print(replaced_name, " <OK>")
                elif replaced_name in ("an_log", "lt_log", "help"):
                    print(result)
                elif replaced_name in (
                    "an_status",
                    "lt_status",
                    "anlt_status",
                    "txtap_get",
                ):
                    print(json.dumps(result, indent=2))
                else:
                    print(replaced_name, " <OK>")
            except Exception as e:
                print(f"{type(e)}: {e}")


if __name__ == "__main__":
    plat = platform.system().lower()
    if plat == "windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(cli_main())
