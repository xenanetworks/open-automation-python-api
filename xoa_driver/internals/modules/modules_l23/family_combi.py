import typing
import functools
from xoa_driver import ports
from xoa_driver.internals.core.commands import P_CAPABILITIES
from xoa_driver.internals.utils import ports_manager as pm
from xoa_driver.internals.utils.cap_id import CapID

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23


D_FAMELY_ID = CapID(1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
F_FAMELY_ID = CapID(0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


CombiTypes = typing.Union[
    ports.POdin1G4S4PCombi, 
    ports.POdin10G4S2PCombi,
]

CombiTypesB = typing.Union[
    ports.POdin1G4S4PCombi_b, 
    ports.POdin10G4S2PCombi_b,
]

async def _port_resolver(conn: "itf.IConnection", module_id: int, port_id: int, port_map: typing.Dict[int, typing.Type]) -> typing.Coroutine[typing.Any, typing.Any, CombiTypes]:
    cap = await P_CAPABILITIES(conn, module_id, port_id).get()
    current_port_id = CapID.create_from_capabilities(cap)
    port_type = port_map[current_port_id.to_int()]
    return await port_type(conn, module_id, port_id)


@typing.final
class MOdin10G4S2PCombi(ModuleL23):
    """Test module Odin-10G-4S-2P-Combi"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        PORTS_MAP = {
            D_FAMELY_ID.to_int(): ports.POdin1G4S4PCombi,
            F_FAMELY_ID.to_int(): ports.POdin10G4S2PCombi,
        }
        self.ports: pm.PortsCombiManager[CombiTypes] = pm.PortsCombiManager(
            conn=conn, 
            resolver=functools.partial(_port_resolver,  port_map=PORTS_MAP), 
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-10G-4S-2P-Combi"""



@typing.final
class MOdin10G4S2PCombi_b(ModuleL23):
    """Test module Odin-10G-4S-2P-Combi[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        PORTS_MAP = {
            D_FAMELY_ID.to_int(): ports.POdin1G4S4PCombi_b,
            F_FAMELY_ID.to_int(): ports.POdin10G4S2PCombi_b,
        }
        self.ports: pm.PortsCombiManager[CombiTypesB] = pm.PortsCombiManager(
            conn=conn, 
            resolver=functools.partial(_port_resolver,  port_map=PORTS_MAP), 
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-10G-4S-2P-Combi[b]"""
