import asyncio
from typing import (
    Dict,
    List,
    Callable,
    Final,
    Any,
    Coroutine,
)
from collections import defaultdict

ON_EVT_DISCONNECTED: Final[int] = -1

CB = Callable[..., Coroutine[Any, None, None]]

# ToDo: add type anntation for callback funcion
class EventsObserver:

    __slots__ = ( "__events", "__loop" )

    def __init__(self) -> None:
        self.__events: Dict[int, List[CB]] = defaultdict(list)
        self.__loop = asyncio.get_event_loop()

    def dispatch(self, evt: int, *args, **kwargs) -> None:
        for evt_func in self.__events.get(evt, []):
            self.__loop.create_task(
                evt_func(*args, **kwargs)
            ).add_done_callback(self.__handle_exceptions)

    def __handle_exceptions(self, fut: "asyncio.Future") -> None:
        if e := fut.exception():
            raise e

    def subscribe(self, evt: int, func: CB) -> None:
        self.__events[evt].append(func)