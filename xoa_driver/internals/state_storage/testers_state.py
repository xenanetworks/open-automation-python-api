import asyncio
from typing import (
    Optional,
    Final,
)
from xoa_driver.internals.core import funcs
from xoa_driver.internals.commands import enums
from xoa_driver.internals.commands import (
    C_RESERVATION,
    C_CAPABILITIES,
    C_RESERVEDBY,
)
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.exceptions.testers import UnsupportedFirmwareError

MIN_SUPPORTED_VERSION = 446.5


class TesterLocalState:
    """Tester local state

    :param host: tester's address/hostname
    :type host: str
    :param port: the port number for connection establishment
    :type port: int
    """
    __slots__ = (
        "host",
        "port",
        "model",
        "capabilities",
        "serial_number",
        "version_major",
        "driver_version",
        "reservation",
        "reserved_by",
    )

    def __init__(self, host: str, port: int) -> None:
        self.host: Final[str] = host
        self.port: Final[int] = port
        self.model: str = ""
        self.capabilities: Optional["C_CAPABILITIES.GetDataAttr"] = None
        self.serial_number: int = 0
        self.version_major: int = 0
        self.driver_version: int = 0
        self.reservation: enums.ReservedStatus = enums.ReservedStatus.RELEASED
        self.reserved_by: str = ""

    async def initiate(self, tester) -> None:
        (
            capabilities_resp,
            model_res,
            v_major_res,
            serial_res,
            reserved_by_res,
            reservation_resp,
        ) = await funcs.apply(
            tester.capabilities.get(),
            tester.model.get(),
            tester.version_no.get(),
            tester.serial_no.get(),
            tester.reserved_by.get(),
            tester.reservation.get(),
        )
        self.reserved_by = reserved_by_res.username
        self.model = model_res.model
        self.driver_version = v_major_res.pci_driver_version
        self.version_major = v_major_res.chassis_major_version
        self.serial_number = serial_res.serial_number
        self.reservation = reservation_resp.operation
        self.capabilities = capabilities_resp

    def register_subscriptions(self, tester) -> None:
        tester._conn.subscribe(C_RESERVEDBY, utils.Update(self, "reserved_by", "username"))
        tester._conn.subscribe(C_RESERVATION, utils.Update(self, "reservation", "operation"))


class GenuineTesterLocalState(TesterLocalState):
    """Genuine Tester Local State

    :param host: tester's address/hostname
    :type host: str
    :param port: the port number for connection establishment
    :type port: int
    """
    __slots__ = ("build_string", "version_minor")

    def __init__(self, host: str, port: int) -> None:
        super().__init__(host, port)
        self.build_string: str = ""
        self.version_minor: int = 0

    async def initiate(self, tester) -> None:
        bs, v_minor, _ = await asyncio.gather(
            tester.build_string.get(),
            tester.version_no_minor.get(),
            super().initiate(tester)
        )
        self.build_string = bs.build_string
        self.version_minor = v_minor.chassis_minor_version
        current_version = float(f"{self.version_major}.{self.version_minor}")
        if current_version < MIN_SUPPORTED_VERSION:
            raise UnsupportedFirmwareError(current_version)
