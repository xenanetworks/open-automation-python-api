from __future__ import annotations
# Generated file

from asyncio.events import AbstractEventLoop
from typing import (
    AsyncGenerator,
    Literal,
    TypeVar,
    overload,
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
_T6 = TypeVar("_T6")
_T7 = TypeVar("_T7")
_T8 = TypeVar("_T8")
_T9 = TypeVar("_T9")
_T10 = TypeVar("_T10")
_T11 = TypeVar("_T11")
_T12 = TypeVar("_T12")
_T13 = TypeVar("_T13")
_T14 = TypeVar("_T14")
_T15 = TypeVar("_T15")
_T16 = TypeVar("_T16")
_T17 = TypeVar("_T17")
_T18 = TypeVar("_T18")
_T19 = TypeVar("_T19")
_T20 = TypeVar("_T20")
_T21 = TypeVar("_T21")
_T22 = TypeVar("_T22")
_T23 = TypeVar("_T23")
_T24 = TypeVar("_T24")
_T25 = TypeVar("_T25")
_T26 = TypeVar("_T26")
_T27 = TypeVar("_T27")
_T28 = TypeVar("_T28")
_T29 = TypeVar("_T29")
_T30 = TypeVar("_T30")
_T31 = TypeVar("_T31")
_T32 = TypeVar("_T32")
_T33 = TypeVar("_T33")
_T34 = TypeVar("_T34")
_T35 = TypeVar("_T35")


@overload
async def apply_iter(__cmd_token1: Token[_T1]) -> AsyncGenerator[_T1, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2]) -> AsyncGenerator[_T1 | _T2, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3]) -> AsyncGenerator[_T1 | _T2 | _T3, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30 | _T31, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30 | _T31 | _T32, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], __cmd_token33: Token[_T33]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30 | _T31 | _T32 | _T33, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], __cmd_token33: Token[_T33], __cmd_token34: Token[_T34]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30 | _T31 | _T32 | _T33 | _T34, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30 | _T31, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30 | _T31 | _T32, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], __cmd_token33: Token[_T33], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30 | _T31 | _T32 | _T33, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], __cmd_token33: Token[_T33], __cmd_token34: Token[_T34], *, return_exceptions: Literal[False]) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30 | _T31 | _T32 | _T33 | _T34, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30 | _T31 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30 | _T31 | _T32 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], __cmd_token33: Token[_T33], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30 | _T31 | _T32 | _T33 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply_iter(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], __cmd_token33: Token[_T33], __cmd_token34: Token[_T34], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> AsyncGenerator[_T1 | _T2 | _T3 | _T4 | _T5 | _T6 | _T7 | _T8 | _T9 | _T10 | _T11 | _T12 | _T13 | _T14 | _T15 | _T16 | _T17 | _T18 | _T19 | _T20 | _T21 | _T22 | _T23 | _T24 | _T25 | _T26 | _T27 | _T28 | _T29 | _T30 | _T31 | _T32 | _T33 | _T34 | Exception, None]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1]) -> tuple[_T1]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2]) -> tuple[_T1, _T2]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3]) -> tuple[_T1, _T2, _T3]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4]) -> tuple[_T1, _T2, _T3, _T4]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5]) -> tuple[_T1, _T2, _T3, _T4, _T5]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28, _T29]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28, _T29, _T30]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28, _T29, _T30, _T31]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28, _T29, _T30, _T31, _T32]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], __cmd_token33: Token[_T33]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28, _T29, _T30, _T31, _T32, _T33]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], __cmd_token33: Token[_T33], __cmd_token34: Token[_T34]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28, _T29, _T30, _T31, _T32, _T33, _T34]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], *, return_exceptions: Literal[False]) -> tuple[_T1]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28, _T29]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28, _T29, _T30]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28, _T29, _T30, _T31]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28, _T29, _T30, _T31, _T32]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], __cmd_token33: Token[_T33], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28, _T29, _T30, _T31, _T32, _T33]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], __cmd_token33: Token[_T33], __cmd_token34: Token[_T34], *, return_exceptions: Literal[False]) -> tuple[_T1, _T2, _T3, _T4, _T5, _T6, _T7, _T8, _T9, _T10, _T11, _T12, _T13, _T14, _T15, _T16, _T17, _T18, _T19, _T20, _T21, _T22, _T23, _T24, _T25, _T26, _T27, _T28, _T29, _T30, _T31, _T32, _T33, _T34]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception, _T22 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception, _T22 | Exception, _T23 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception, _T22 | Exception, _T23 | Exception, _T24 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception, _T22 | Exception, _T23 | Exception, _T24 | Exception, _T25 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception, _T22 | Exception, _T23 | Exception, _T24 | Exception, _T25 | Exception, _T26 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception, _T22 | Exception, _T23 | Exception, _T24 | Exception, _T25 | Exception, _T26 | Exception, _T27 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception, _T22 | Exception, _T23 | Exception, _T24 | Exception, _T25 | Exception, _T26 | Exception, _T27 | Exception, _T28 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception, _T22 | Exception, _T23 | Exception, _T24 | Exception, _T25 | Exception, _T26 | Exception, _T27 | Exception, _T28 | Exception, _T29 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception, _T22 | Exception, _T23 | Exception, _T24 | Exception, _T25 | Exception, _T26 | Exception, _T27 | Exception, _T28 | Exception, _T29 | Exception, _T30 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception, _T22 | Exception, _T23 | Exception, _T24 | Exception, _T25 | Exception, _T26 | Exception, _T27 | Exception, _T28 | Exception, _T29 | Exception, _T30 | Exception, _T31 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception, _T22 | Exception, _T23 | Exception, _T24 | Exception, _T25 | Exception, _T26 | Exception, _T27 | Exception, _T28 | Exception, _T29 | Exception, _T30 | Exception, _T31 | Exception, _T32 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], __cmd_token33: Token[_T33], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception, _T22 | Exception, _T23 | Exception, _T24 | Exception, _T25 | Exception, _T26 | Exception, _T27 | Exception, _T28 | Exception, _T29 | Exception, _T30 | Exception, _T31 | Exception, _T32 | Exception, _T33 | Exception]:  # noqa: E501
    ...


@overload
async def apply(__cmd_token1: Token[_T1], __cmd_token2: Token[_T2], __cmd_token3: Token[_T3], __cmd_token4: Token[_T4], __cmd_token5: Token[_T5], __cmd_token6: Token[_T6], __cmd_token7: Token[_T7], __cmd_token8: Token[_T8], __cmd_token9: Token[_T9], __cmd_token10: Token[_T10], __cmd_token11: Token[_T11], __cmd_token12: Token[_T12], __cmd_token13: Token[_T13], __cmd_token14: Token[_T14], __cmd_token15: Token[_T15], __cmd_token16: Token[_T16], __cmd_token17: Token[_T17], __cmd_token18: Token[_T18], __cmd_token19: Token[_T19], __cmd_token20: Token[_T20], __cmd_token21: Token[_T21], __cmd_token22: Token[_T22], __cmd_token23: Token[_T23], __cmd_token24: Token[_T24], __cmd_token25: Token[_T25], __cmd_token26: Token[_T26], __cmd_token27: Token[_T27], __cmd_token28: Token[_T28], __cmd_token29: Token[_T29], __cmd_token30: Token[_T30], __cmd_token31: Token[_T31], __cmd_token32: Token[_T32], __cmd_token33: Token[_T33], __cmd_token34: Token[_T34], *, return_exceptions: Literal[True], token_timeout_sec: float = 5.0) -> tuple[_T1 | Exception, _T2 | Exception, _T3 | Exception, _T4 | Exception, _T5 | Exception, _T6 | Exception, _T7 | Exception, _T8 | Exception, _T9 | Exception, _T10 | Exception, _T11 | Exception, _T12 | Exception, _T13 | Exception, _T14 | Exception, _T15 | Exception, _T16 | Exception, _T17 | Exception, _T18 | Exception, _T19 | Exception, _T20 | Exception, _T21 | Exception, _T22 | Exception, _T23 | Exception, _T24 | Exception, _T25 | Exception, _T26 | Exception, _T27 | Exception, _T28 | Exception, _T29 | Exception, _T30 | Exception, _T31 | Exception, _T32 | Exception, _T33 | Exception, _T34 | Exception]:  # noqa: E501
    ...
