from dataclasses import dataclass
from typing import (
    Callable, 
    Type,
    TYPE_CHECKING,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core.protocol.struct_response import Response
    from xoa_driver.internals.core import interfaces as itf

@dataclass
class Update:
    inst: Type
    property_name: str
    response_key: str
    condition: Callable[["Response"], bool] = lambda _: True

    # keep it Async just for consistant interface of event_observer
    async def __call__(self, response: "Response") -> None:
        if not self.condition(response):
            return None
        v = getattr(response.values, self.response_key)
        setattr(self.inst, self.property_name, v)



def on_event(self, evt: "itf.CMD_TYPE", callback: "itf.CallbackType") -> None:
    async def _f(response: "Response", *args, **kwargs) -> None:
        if not self._check_identity(response):
            return None
        await callback(self, response.values, *args, **kwargs)
    self._conn.subscribe(evt, _f)