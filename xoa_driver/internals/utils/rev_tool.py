from __future__ import annotations
from typing import (
    Type,
    TypeVar
)

T = TypeVar("T")


class RegisterModule:
    """Register revision and it's module class"""

    def __init__(self, modules_store: dict[str, Type], rev: str) -> None:
        self.modules_store = modules_store
        self.revision = rev

    def __call__(self, module_type: Type[T]) -> Type[T]:
        if self.revision in self.modules_store:
            raise RuntimeError(f"Module of revision: {self.revision}, is already registered.")
        self.modules_store[self.revision] = module_type
        return module_type
