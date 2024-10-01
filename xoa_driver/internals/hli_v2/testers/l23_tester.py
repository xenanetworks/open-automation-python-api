from __future__ import annotations
from typing import (
    Union,
    TYPE_CHECKING,
    Type,
)
from xoa_driver.internals.commands import (
    C_PORTCOUNTS,
    C_MULTIUSER,
    C_TRAFFIC,
    C_TRAFFICSYNC,
    C_VERSIONNO_MINOR,
    C_BUILDSTRING,
    C_VERSIONSTR,
)
from xoa_driver.internals.core.transporter.logger import CustomLogger
from xoa_driver.internals.utils.managers.modules_manager import ModulesManager
from ._base_tester import BaseTester
from .genuine import management_interface as mi
from .genuine.l_23 import (
    upload_file,
    time_keeper,
    rest_api,
    health,
)
if TYPE_CHECKING:
    from xoa_driver.v2 import modules

from xoa_driver.internals.state_storage import testers_state
from xoa_driver.internals.hli_v2 import revisions
from xoa_driver.internals import exceptions


TypeL23Manager = ModulesManager[
    Union[
        "modules.GenericL23Module",
        "modules.ModuleChimera",
    ]
]


def get_module_type(revision: str) -> Type:
    module_type = dict(
        **revisions.VALKYRIE_MODULES,
        **revisions.CHIMERA_MODULES,
    ).get(revision)
    if not module_type:
        raise exceptions.WrongModuleError(
            revision,
            set.union(
                set(revisions.VALKYRIE_MODULES.keys()),
                set(revisions.CHIMERA_MODULES.keys()),
            )
        )
    return module_type


class L23Tester(BaseTester["testers_state.GenuineTesterLocalState"]):
    """
    This is a conceptual class of Xena Valkyrie Tester.
    It is essentially an extended :class:`BaseTester`.


    :param host: tester's address/hostname
    :type host: str
    :param username: username of the user
    :type username: str
    :param password: login password of the tester, defaults to "xena"
    :type password: str, optional
    :param port: the port number for connection establishment, default to 22606
    :type port: int, optional
    :param enable_logging: `True` if debug log output from the tester is needed, and `False` otherwise
    :type enable_logging: bool
    :param custom_logger: `None` allow to specify logger with custom configurations
    :type enable_logging: CustomLogger | None
    :param session_timeout: `130` Session timeout in seconds
    :type session_timeout: int
    """

    def __init__(self, host: str, username: str, password: str = "xena", port: int = 22606, *, enable_logging: bool = False, custom_logger: CustomLogger | None = None, session_timeout: int = 130) -> None:
        super().__init__(
            host=host,
            username=username,
            password=password,
            port=port,
            enable_logging=enable_logging,
            custom_logger=custom_logger,
            session_timeout=session_timeout
        )

        self._local_states = testers_state.GenuineTesterLocalState(host, port)

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
        self.version_str = C_VERSIONSTR(self._conn)
        """
        Returns xenaserver version number in the new format.

        :type: C_VERSIONSTR
        """
        self.build_string = C_BUILDSTRING(self._conn)
        """
        Representation of C_BUILDSTRING
        """
        self.health = health.Health(self._conn)
        """
        Chassis system health information.

        :type: C_HEALTH
        """
        self.modules: TypeL23Manager = ModulesManager(self._conn, get_module_type)
        """
        Module index manager of the L23 tester.
        """

    @property
    def info(self) -> testers_state.GenuineTesterLocalState:
        return self._local_states

    async def _setup(self):
        await super()._setup()
        await self._local_states.initiate(self)
        self._local_states.register_subscriptions(self)

        ft_pc = await C_PORTCOUNTS(self._conn).get()
        port_counts = ft_pc.port_counts
        await self.modules.fill_l23(port_counts)
        return self
