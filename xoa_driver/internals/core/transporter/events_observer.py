from __future__ import annotations
import asyncio
from typing import (
    Callable,
    Final,
    Any,
    Coroutine,
)
from collections import defaultdict

ON_EVT_DISCONNECTED: Final[int] = -1

CB = Callable[..., Coroutine[Any, None, None]]

#TODO: add type annotation for callback function


class EventsObserver:

    __slots__ = ("__events", )

    def __init__(self) -> None:
        self.__events: dict[int, list[CB]] = defaultdict(list)

    def dispatch(self, evt: int, *args, **kwargs) -> None:
        for evt_func in self.__events.get(evt, []):
            asyncio.create_task(
                evt_func(*args, **kwargs)
            ).add_done_callback(self.__handle_exceptions)

    def __handle_exceptions(self, fut: "asyncio.Future") -> None:
        if e := fut.exception():
            raise e

    def subscribe(self, evt: int, func: CB) -> None:
        self.__events[evt].append(func)


