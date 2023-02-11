from __future__ import annotations
import asyncio
from asyncio.events import AbstractEventLoop
from collections import defaultdict
from typing_extensions import TypeGuard
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncGenerator,
    Optional,
    Dict,
    TypeVar,
    Union,
    overload,
)
if TYPE_CHECKING:
    from .handler import TransportationHandler
    from .. import interfaces

from .token import Token
from . import exceptions
from ..protocol.payload.base_struct import ResponseBodyStruct


async def establish_connection(transporter: "TransportationHandler", host: str, port: int = 22606, loop: Optional["AbstractEventLoop"] = None) -> None:
    """
    Establish connection to provided host and port and assign ``<TransportationHandler>`` to it.
    """

    assert isinstance(loop, AbstractEventLoop) or loop is None, "<loop> must be an instance of AbstractEventLoop or None"
    __loop = loop if loop else asyncio.get_event_loop()
    try:
        await __loop.create_connection(lambda: transporter, host=host, port=port)
    except OSError:
        raise exceptions.EstablishConnectionError(host, port) from None


_TT1 = TypeVar("_TT1", bound="ResponseBodyStruct", covariant=True)


async def apply_iter(*cmd_tokens: Token[_TT1 | None]) -> AsyncGenerator[_TT1 | None, None]:
    """
    Main interface for chunking the commands which need to be send to one or multiple testers at the same time.
    """
    aggregator: Dict["interfaces.IConnection", bytearray] = defaultdict(bytearray)
    queue: asyncio.Queue[asyncio.Future] = asyncio.Queue()
    for t in cmd_tokens:
        (data, fut) = await t.connection.prepare_data(t.request)
        aggregator[t.connection].extend(data)
        queue.put_nowait(fut)
    [c.send(r) for c, r in aggregator.items()]
    aggregator.clear()
    while not queue.empty():
        future = await queue.get()
        yield await future
        queue.task_done()
    await queue.join()

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")

@overload
async def apply(__cmd_tokens1: Token[_T1]) -> tuple[_T1]:
    ...


@overload
async def apply(__cmd_tokens1: Token[_T1], __cmd_tokens2: Token[_T2]) -> tuple[_T1, _T2]:
    ...


@overload
async def apply(__cmd_tokens1: Token[_T1], __cmd_tokens2: Token[_T2], __cmd_tokens3: Token[_T3]) -> tuple[_T1, _T2, _T3]:
    ...


@overload
async def apply(__cmd_tokens1: Token[_T1], __cmd_tokens2: Token[_T2], __cmd_tokens3: Token[_T3], __cmd_tokens4: Token[_T4]) -> tuple[_T1, _T2, _T3, _T4]:
    ...


@overload
async def apply(__cmd_tokens1: Token[_T1], __cmd_tokens2: Token[_T2], __cmd_tokens3: Token[_T3], __cmd_tokens4: Token[_T4], __cmd_tokens5: Token[_T5]) -> tuple[_T1, _T2, _T3, _T4, _T5]:
    ...


async def apply(*cmd_tokens: Token[Any]) -> list[Any]:  # type: ignore
    """
    Main interface for chunking the commands which need to be send to one or multiple testers at the same time.
    """
    assert len(cmd_tokens) <= 200, "Number of the commands is bigger then 200 for one aggregation, please use function <apply_iter> instead"
    return [f async for f in apply_iter(*cmd_tokens)]
