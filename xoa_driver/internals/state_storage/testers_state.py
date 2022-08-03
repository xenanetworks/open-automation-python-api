import asyncio
from typing import (
    Optional,
    Final,
)
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.core.transporter import funcs
from xoa_driver.internals.core.commands import enums

from xoa_driver.internals.core.commands import (
    C_RESERVATION,
    C_CAPABILITIES,
    C_RESERVEDBY,
)



class TesterLocalState:
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
        tester._conn.subscribe(C_RESERVATION, utils.Update(self, "reservation", "operation", format=lambda a: enums.ReservedStatus(a)))


class GenuineTesterLocalState(TesterLocalState):
    __slots__ = ("build_string",)
    def __init__(self, host: str, port: int) -> None:
        super().__init__(host, port)
        self.build_string: str = ""
    
    async def initiate(self, tester) -> None:
        bs, _ = await asyncio.gather(
            tester.build_string.get(),
            super().initiate(tester)
        )
        self.build_string = bs.build_string