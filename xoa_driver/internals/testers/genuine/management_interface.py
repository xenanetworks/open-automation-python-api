from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    C_IPADDRESS,
    C_DHCP,
    C_MACADDRESS,
    C_HOSTNAME,
)
class ManagementInterface:
    def __init__(self, conn: "itf.IConnection" ) -> None:
        self.ip_address = C_IPADDRESS(conn)
        self.dhcp = C_DHCP(conn)
        self.macaddress = C_MACADDRESS(conn)
        self.hostname = C_HOSTNAME(conn)