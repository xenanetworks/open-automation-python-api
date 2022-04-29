from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    C_IPADDRESS,
    C_DHCP,
    C_MACADDRESS,
    C_HOSTNAME,
)
class ManagementInterface:
    """
    Tester management interface address configuration.
    """
    def __init__(self, conn: "itf.IConnection" ) -> None:
        self.ip_address = C_IPADDRESS(conn)
        """
        Chassis management port IP address configuration.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_IPADDRESS`
        """
        self.dhcp = C_DHCP(conn)
        """
        Chassis management port IP address configuration with DHCP.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_DHCP`
        """
        self.macaddress = C_MACADDRESS(conn)
        """
        Chassis management port MAC address.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_MACADDRESS`
        """
        self.hostname = C_HOSTNAME(conn)
        """
        Chassis management hostname.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_HOSTNAME`
        """