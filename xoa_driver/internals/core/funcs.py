from __future__ import annotations
import asyncio
from asyncio.events import AbstractEventLoop
import io
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncGenerator,
)
if TYPE_CHECKING:
    from .transporter.handler import TransportationHandler
    from . import interfaces

from .token import Token
from .transporter import exceptions


async def establish_connection(transporter: "TransportationHandler", host: str, port: int = 22606, *, seconds_timeout: int = 5, loop: AbstractEventLoop | None = None) -> None:
    """
    Establish connection to provided host and port and assign ``<TransportationHandler>`` to it.
    """
    assert isinstance(loop, AbstractEventLoop) or loop is None, "<loop> must be an instance of AbstractEventLoop or None"
    __loop = loop if loop else asyncio.get_event_loop()
    try:
        await asyncio.wait_for(
            __loop.create_connection(lambda: transporter, host=host, port=port),
            seconds_timeout
        )
    except OSError:
        raise exceptions.XoaConnectionError(host, port) from None
    except asyncio.exceptions.TimeoutError:
        raise exceptions.XoaConnectionTimeoutError(host, port, seconds_timeout) from None


async def apply_iter(*cmd_tokens: Token[Any], return_exceptions: bool = False, token_timeout_sec: float | None = 5.0) -> AsyncGenerator[Any, None]:
    """
    Main interface for chunking the commands which need to be send to the single tester at the same time.
    """
    if not cmd_tokens:
        return
    conn: "interfaces.IConnection" = cmd_tokens[0].connection
    buffer_bytes = io.BytesIO()
    queue: asyncio.Queue[asyncio.Future] = asyncio.Queue()
    for t in cmd_tokens:
        (data, fut) = await t.connection.prepare_data(t.request)
        buffer_bytes.write(data)
        queue.put_nowait(fut)
    conn.send(buffer_bytes.getvalue())
    buffer_bytes.close()
    del buffer_bytes

    while not queue.empty():
        future = await queue.get()
        try:
            result_ = await asyncio.wait_for(
                asyncio.shield(future),
                token_timeout_sec if return_exceptions else None
            )
        except Exception as e:
            if return_exceptions:
                yield e
            else:
                raise e
        else:
            yield result_
        queue.task_done()
    await queue.join()


async def apply(*cmd_tokens: Token[Any], return_exceptions: bool = False, token_timeout_sec: float | None = 5.0) -> list[Any]:
    """
    Main interface for chunking the commands which need to be send to one or multiple testers at the same time.
    """
    assert len(cmd_tokens) <= 200, "Number of the commands is bigger then 200 for one aggregation, please use function <apply_iter> instead"
    return [
        f async for f in apply_iter(
            *cmd_tokens, 
            return_exceptions=return_exceptions, 
            token_timeout_sec=token_timeout_sec
        )
    ]
