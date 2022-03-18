from typing import (
    Dict,
    Type,
)
from .interfaces import CMD_TYPE

COMMANDS_REGISTRY: Dict[int, CMD_TYPE] = {}
"""A global registry of which map command id to its class implementation."""

def register_command(xmc_cls: CMD_TYPE) -> Type:
    """A decorator used for register commands descriptors in to global registry"""
    if xmc_cls.code in COMMANDS_REGISTRY:
        raise RuntimeError(
            f"Command with the same code {xmc_cls.code} for the command {COMMANDS_REGISTRY[xmc_cls.code]}!"
        )
    COMMANDS_REGISTRY[xmc_cls.code] = xmc_cls
    return xmc_cls
