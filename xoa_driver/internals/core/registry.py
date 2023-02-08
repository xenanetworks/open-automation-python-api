from __future__ import annotations
from typing import Type
from .interfaces import CMD_TYPE

COMMANDS_REGISTRY: dict[int, Type[CMD_TYPE]] = dict()
"""A global registry of which map command id to its class implementation."""


def register_command(xmc_cls: Type[CMD_TYPE]) -> Type:
    """A decorator used for register commands descriptors in to global registry"""
    global COMMANDS_REGISTRY
    if xmc_cls.code in COMMANDS_REGISTRY:
        raise RuntimeError(
            f"Command with the same code {xmc_cls.code} for the command {COMMANDS_REGISTRY[xmc_cls.code]}!"
        )
    COMMANDS_REGISTRY[xmc_cls.code] = xmc_cls
    return xmc_cls


def get_command(command_idx: int):
    global COMMANDS_REGISTRY
    xmc_type = COMMANDS_REGISTRY.get(command_idx, None)
    if not xmc_type:
        raise RuntimeError(f"Command with id: {command_idx} is not implemented")