from __future__ import annotations
from typing import Type
from ._typings import XoaCommandType


class XmpRegistryException(Exception):
    ...


class XmpCmdDuplicatedDefenitionError(XmpRegistryException):
    def __init__(self, xmc_cls: Type[XoaCommandType]) -> None:
        self.cmd_type = xmc_cls
        self.msg = f"The defenition of <{self.cmd_type.__name__}> is duplicated."
        super().__init__(self.msg)


class XmpCmdNotImplemented(XmpRegistryException):
    def __init__(self, cmd_idx: int) -> None:
        self.cmd_idx = cmd_idx
        self.msg = f"The command of the code: [{cmd_idx}], is not implemented or not registered as a XMP command."
        super().__init__(self.msg)


COMMANDS_REGISTRY: dict[int, Type[XoaCommandType]] = dict()
"""A global registry of which map command id to its class implementation."""


def register_command(xmc_cls: Type[XoaCommandType]) -> Type:
    """A decorator used for register commands descriptors in to global registry"""
    global COMMANDS_REGISTRY
    if xmc_cls.code in COMMANDS_REGISTRY:
        raise XmpCmdDuplicatedDefenitionError(xmc_cls)
    COMMANDS_REGISTRY[xmc_cls.code] = xmc_cls
    return xmc_cls


def get_command(command_idx: int) -> Type[XoaCommandType]:
    """Method allows to get a command class by the command code"""
    global COMMANDS_REGISTRY
    xmc_type = COMMANDS_REGISTRY.get(command_idx, None)
    if not xmc_type:
        raise XmpCmdNotImplemented(command_idx)
    return xmc_type
