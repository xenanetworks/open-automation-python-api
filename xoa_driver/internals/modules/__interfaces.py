import typing

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
class ModuleInitData(typing.Protocol):
    module_id: int
    ports_count: int
    revision: str


class IPort(typing.Protocol):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        ...

    # def __await__(self):
    #     ...

    # async def _setup(self):
    #     ...