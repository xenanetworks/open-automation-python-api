from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PX_RW,
    PX_MII,
    PX_TEMPERATURE,
    PX_RW_SEQ,
    PX_I2C_CONFIG,
    PX_RW_SEQ_BANK,
)


class PortTransceiver:
    """L23 port transceiver."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id

        self.i2c_config = PX_I2C_CONFIG(conn, module_id, port_id)
        """Access speed on a transceiver.
        :type: PX_I2C_CONFIG
        """

    def access_temperature(self):
        """Transceiver temperature in Celsius.

        :return: Transceiver temperature integral and decimal parts
        :rtype: PX_TEMPERATURE
        """

        return PX_TEMPERATURE(
            self.__conn,
            self.__module_id,
            self.__port_id,
        )

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

    def access_rw_seq(self, page_address: int, register_address: int, byte_count: int) -> "PX_RW_SEQ":
        """Sequential read/write a number of bytes to the register interface supported by the media-independent interface (MII) transceiver.

        :param page_address: page address (0-255)
        :type page_address: int
        :param register_address: register address (0-255)
        :type register_address: int
        :param byte_count: the number of bytes to read/write
        :type byte_count: int
        :return: transceiver register values
        :rtype: PX_RW_SEQ
        """
        return PX_RW_SEQ(
            self.__conn,
            self.__module_id,
            self.__port_id,
            page_address,
            register_address,
            byte_count
        )

    def access_rw_seq_bank(self, bank_address: int, page_address: int, register_address: int, byte_count: int) -> "PX_RW_SEQ_BANK":
        """Sequential read/write a number of bytes to the register interface supported by the media-independent interface (MII) transceiver.

        :param bank_address: bank address (0-255)
        :type bank_address: int
        :param page_address: page address (0-255)
        :type page_address: int
        :param register_address: register address (0-255)
        :type register_address: int
        :param byte_count: the number of bytes to read/write
        :type byte_count: int
        :return: transceiver register values
        :rtype: PX_RW_SEQ_BANK
        """
        return PX_RW_SEQ_BANK(
            self.__conn,
            self.__module_id,
            self.__port_id,
            bank_address,
            page_address,
            register_address,
            byte_count
        )