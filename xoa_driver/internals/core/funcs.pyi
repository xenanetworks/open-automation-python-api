from __future__ import annotations
from asyncio.events import AbstractEventLoop
from typing import (
    AsyncGenerator,
    Literal,
    TypeVar,
    overload
)
from .token import Token
from .transporter.handler import TransportationHandler


async def establish_connection(transporter: TransportationHandler, host: str, port: int = 22606, loop: "AbstractEventLoop" | None = None) -> None:
    ...


_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")


@overload
async def apply_iter(__cmd_token1: Token[_T1]) -> AsyncGenerator[_T1, None]:
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2]) -> AsyncGenerator[_T1 | _T2, None]:
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3]) -> AsyncGenerator[_T1 | _T2 | _T3, None]:
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1, None]:
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2, None]:
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3, None]:
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], *, return_exceptions: bool = False) -> AsyncGenerator[_T1 | Exception, None]:
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], *, return_exceptions: bool = False) -> AsyncGenerator[_T1 | _T2 | Exception, None]:
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], *, return_exceptions: bool = False) -> AsyncGenerator[_T1 | _T2 | _T3 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], *, return_exceptions: bool = False) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], *, return_exceptions: bool = False) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1]) -> tuple[_T1]:
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2]) -> tuple[_T1, _T2]:
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3]) -> tuple[_T1, _T2, _T3]:
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4]) -> tuple[_T1, _T2, _T3, _T4]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5]) -> tuple[_T1, _T2, _T3, _T4, _T5]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], *, return_exceptions: Literal[False]) -> tuple[_T1]:
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2]:
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3]:
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], *, return_exceptions: bool = False) -> tuple[_T1 | Exception]:
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], *, return_exceptions: bool = False) -> tuple[_T1 | Exception, _T2 | Exception]:
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], *, return_exceptions: bool = False) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], *, return_exceptions: bool = False) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], *, return_exceptions: bool = False) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception]:  # noqa: E501
    ...
