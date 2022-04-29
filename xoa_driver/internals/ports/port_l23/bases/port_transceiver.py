from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    PX_RW,
    PX_MII,
    PX_TEMPERATURE,
)

class PortTransceiver:
    """L23 port transceiver."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.temperature = PX_TEMPERATURE(conn, module_id, port_id)
        """Transceiver temperature in Celsius.
        Representation of :class:`~xoa_driver.internals.core.commands.px_commands.PX_TEMPERATURE`
        """
    
    def access_rw(self, page_address: int, register_address: int) -> "PX_RW":
        """Access to register interface by the transceiver.

        :param page_address: page address
        :type page_address: int
        :param register_address: register address
        :type register_address: int
        :return: transceiver register values
        :rtype: PX_RW
        """
        return PX_RW(
            self.__conn, 
            self.__module_id, 
            self.__port_id, 
            page_address, 
            register_address
        )
    
    def access_mii(self, register_address: int) -> "PX_MII":
        """Access to the register interface supported by the media-independent interface (MII) transceiver.

        :param register_address: register address
        :type register_address: int
        :return: register values
        :rtype: PX_MII
        """
        return PX_MII(
            self.__conn, 
            self.__module_id, 
            self.__port_id,
            register_address
        )