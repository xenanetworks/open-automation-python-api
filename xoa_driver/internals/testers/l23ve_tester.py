from typing import Type
from xoa_driver.internals.core.commands import (
    C_PORTCOUNTS,
    C_MULTIUSER,
    C_TRAFFIC,
    C_TRAFFICSYNC,
    C_VERSIONNO_MINOR,
)
from xoa_driver.internals.utils.modules_manager import ModulesManager
from ._base_tester import BaseTester


from xoa_driver import modules
from xoa_driver.internals.state_storage import testers_state


TypeL23Manager = ModulesManager["modules.ModuleL23VE"]

def get_module_type(revision: str) -> Type:
    return modules.ModuleL23VE

class L23VeTester(BaseTester["testers_state.TesterLocalState"]):
    """
    Representation of a virtual Xena Valkyrie Tester.
    """
    
    def __init__(self, host: str, username: str, password: str = "xena", port: int = 22606, *, debug: bool = False) -> None:
        super().__init__(host=host, username=username, password=password, port=port, debug=debug)
        
        self._local_states = testers_state.TesterLocalState(host, port)

        self.multiuser = C_MULTIUSER(self._conn)
        """
        Representation of C_MULTIUSER
        """

        self.traffic = C_TRAFFIC(self._conn)
        """
        Representation of C_TRAFFIC
        """

        self.traffic_sync = C_TRAFFICSYNC(self._conn)
        """
        Representation of C_TRAFFICSYNC
        """
        
        self.version_no_minor = C_VERSIONNO_MINOR(self._conn)
        """
        Representation of C_VERSIONNO_MINOR
        """
        
        self.modules: TypeL23Manager = ModulesManager(self._conn, get_module_type)
        """
        Module index manager of the L23 tester.
        """
    
    @property
    def info(self) -> testers_state.TesterLocalState:
        return self._local_states
    
    async def _setup(self):
        await super()._setup()
        await self._local_states.initiate(self)
        self._local_states.register_subscriptions(self)
        
        ft_pc = await C_PORTCOUNTS(self._conn).get()
        port_counts = ft_pc.port_counts
        await self.modules.fill_l23(port_counts)
        return self

