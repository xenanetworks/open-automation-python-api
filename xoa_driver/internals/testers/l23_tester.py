from typing import (
    Union,
    TYPE_CHECKING,
    Type,
)
from xoa_driver.internals.core.commands import (
    C_PORTCOUNTS,
    C_MULTIUSER,
    C_TRAFFIC,
    C_TRAFFICSYNC,
    C_VERSIONNO_MINOR,
    C_BUILDSTRING,
)
from xoa_driver.internals.utils.modules_manager import ModulesManager
from ._base_tester import BaseTester
from .genuine import management_interface as mi
from .genuine.l_23 import (
    upload_file,
    time_keeper,
    rest_api,
)
if TYPE_CHECKING:
    from xoa_driver import modules
    from xoa_driver.internals.state_storage import testers_state

from xoa_driver.internals import revisions
from xoa_driver.internals import exceptions


TypeL23Manager = ModulesManager[
    Union[
        "modules.MOdin1G3S6P",
        "modules.MOdin1G3S6P_b",
        "modules.MOdin1G3S6PE",
        "modules.MOdin1G3S2PT",
        "modules.MOdin5G4S6PCU",
        "modules.MOdin10G5S6PCU",
        "modules.MOdin10G5S6PCU_b",
        "modules.MOdin10G3S6PCU",
        "modules.MOdin10G3S2PCU",
        "modules.MOdin10G1S2P",
        "modules.MOdin10G1S2P_b",
        "modules.MOdin10G1S2P_c",
        "modules.MOdin10G1S6P",
        "modules.MOdin10G1S6P_b",
        "modules.MOdin10G1S2PT",
        "modules.MOdin10G1S2P_d",
        "modules.MOdin10G1S12P",
        "modules.MOdin40G2S2P",
        "modules.MLoki100G3S1P",
        "modules.MLoki100G3S1P_b",
        "modules.MLoki100G3S1PSE",
        "modules.MLoki100G5S1P",
        "modules.MLoki100G5S2P",
        "modules.MThor100G5S4P",
        "modules.MThor400G7S1P",
        "modules.MThor400G7S1P_b",
        "modules.MThor400G7S1P_c",
        "modules.MOdin1G3S6PT1RJ45",
        "modules.ModuleChimera",
    ]
]

def get_module_type(revision: str) -> Type:
    module_type = dict(
        **revisions.valkyrie_modules,
        **revisions.chimera_modules,
    ).get(revision)
    if not module_type:
        raise exceptions.WrongModuleError(
            revision,
            set.union(
                set(revisions.valkyrie_modules.keys()),
                set(revisions.chimera_modules.keys()),
            )
        )
    return module_type

class L23Tester(BaseTester["testers_state.TesterLocalState"]):
    """
    Representation of a physical Xena Valkyrie Tester.
    """
    def __init__(self, host: str, username: str, password: str = "xena", port: int = 22606, *, debug: bool = False) -> None:
        super().__init__(host=host, username=username, password=password, port=port, debug=debug)
        self.management_interface = mi.ManagementInterface(self._conn)
        """Tester management interface that includes IP address, DHCP, MAC address and hostname.
        """

        self.upload_file = upload_file.UploadFile(self._conn)
        """File upload functions of the tester.
        """

        self.rest_api_server = rest_api.RestApiServer(self._conn)
        """REST API server of the tester.
        """

        self.time_keeper = time_keeper.TimeKeeper(self._conn)
        """TimeKeeper of the tester.
        """

        self.multiuser = C_MULTIUSER(self._conn)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_MULTIUSER`
        """

        self.traffic = C_TRAFFIC(self._conn)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_TRAFFIC`
        """
        self.traffic_sync = C_TRAFFICSYNC(self._conn)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_TRAFFICSYNC`
        """
        
        self.version_no_minor = C_VERSIONNO_MINOR(self._conn)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_VERSIONNO_MINOR`
        """

        self.build_string = C_BUILDSTRING(self._conn)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_BUILDSTRING`
        """

        self.modules: TypeL23Manager = ModulesManager(self._conn, get_module_type)
        """
        Module index manager of the L23 tester.
        """

    async def _setup(self):
        await super()._setup()
        ft_pc = await C_PORTCOUNTS(self._conn).get()
        port_counts = ft_pc.port_counts
        await self.modules.fill_l23(port_counts)
        return self

