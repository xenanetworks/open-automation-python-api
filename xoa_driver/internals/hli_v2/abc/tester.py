from abc import ABC
from .module import Module

class Tester(ABC):
    def __init__(self, host: str, username: str, password: str = "xena", port: int = 22606, *, enable_logging: bool = False, custom_logger: CustomLogger | None = None) -> None:
        super().__init__()

    async def connect(self) -> None:
        ...

    async def disconnect(self) -> None:
        ...

    async def reserve(self) -> bool:
        ...

    async def release(self) -> bool:
        ...
