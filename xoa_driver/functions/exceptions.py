from __future__ import annotations

from xoa_driver.ports import GenericAnyPort
from xoa_driver.modules import GenericAnyModule


class ConfigError(Exception):
    msg: str


class NotConnectedError(ConfigError):
    def __init__(self) -> None:
        self.msg = "No tester is connected!"
        super().__init__(self.msg)


class NotSupportPcsPmaError(ConfigError):
    def __init__(self, port: GenericAnyPort) -> None:
        module_id, port_id = port.kind.module_id, port.kind.port_id
        self.msg = f"This port {module_id}/{port_id} does not support pcs_pma!"
        super().__init__(self.msg)


class NotSupportAutoNegError(ConfigError):
    def __init__(self, port: GenericAnyPort) -> None:
        module_id, port_id = port.kind.module_id, port.kind.port_id
        self.msg = f"This port {module_id}/{port_id} does not support auto negotiation!"
        super().__init__(self.msg)


class NotSupportLinkTrainError(ConfigError):
    def __init__(self, port: GenericAnyPort) -> None:
        module_id, port_id = port.kind.module_id, port.kind.port_id
        self.msg = f"This port {module_id}/{port_id} does not support link training!"
        super().__init__(self.msg)


class NotRightLaneLengthError(ConfigError):
    def __init__(self, serdes: list[int]) -> None:
        self.msg = f"Serdes {serdes} should be length of 4!"
        super().__init__(self.msg)


class NotRightLaneValueError(ConfigError):
    def __init__(self, serdes: list[int]) -> None:
        self.msg = f"Serdes {serdes} should be a list of 4 integers ranges from 0 to 255!"
        super().__init__(self.msg)


class NotSupportMedia(ConfigError):
    def __init__(self, module: GenericAnyModule) -> None:
        module_id = module.module_id
        self.msg = f"This module {module_id} does not support this media configuration!"


class NotSupportPortSpeed(ConfigError):
    def __init__(self, module: GenericAnyModule) -> None:
        module_id = module.module_id
        self.msg = f"This module {module_id} does not support the port-speed configuration under its current media configuration!"


__all__ = (
    "ConfigError",
    "NotConnectedError",
    "NotRightLaneLengthError",
    "NotRightLaneValueError",
    "NotSupportAutoNegError",
    "NotSupportLinkTrainError",
    "NotSupportPcsPmaError",
    "NotSupportMedia",
    "NotSupportPortSpeed",
)
