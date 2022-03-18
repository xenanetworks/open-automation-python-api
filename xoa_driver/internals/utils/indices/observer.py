from enum import IntEnum, auto


class IndexEvents(IntEnum):
    DEL = auto()

class IndicesObserver:
    def __init__(self) -> None:
        self.__subscriptions = {}
    
    def subscribe(self, evt, func) -> None:
        assert evt not in self.__subscriptions, f"Event <{evt}> is already registered."
        self.__subscriptions[evt] = func

    def notify(self, evt, index_inst) -> None:
        self.__subscriptions[evt](index_inst)