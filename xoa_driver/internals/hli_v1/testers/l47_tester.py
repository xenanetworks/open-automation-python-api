from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    Type
)
from typing_extensions import Self
from xoa_driver.internals.commands import (
    C_REMOTEPORTCOUNTS,
    C_BUILDSTRING,
)
from xoa_driver.internals.core.transporter.logger import CustomLogger
from xoa_driver.internals.utils.managers import modules_manager as mm
from xoa_driver.internals.hli_v1 import revisions
from xoa_driver.internals import exceptions
if TYPE_CHECKING:
    from xoa_driver.internals.hli_v1.modules import module_l47 as ml47

from xoa_driver.internals.state_storage import testers_state
from ._base_tester import BaseTester
from .genuine import management_interface as mi


def get_module_type(revision: str) -> "Type":
    module_type = revisions.VULCAN_MODULES.get(revision)
    if not module_type:
        raise exceptions.WrongModuleError(
            revision,
            set(revisions.VULCAN_MODULES.keys()),
        )
    return module_type


class L47Tester(BaseTester["testers_state.GenuineTesterLocalState"]):
    """
    This is a conceptual class of Xena Vulcan Tester.
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

        self.build_string = C_BUILDSTRING(self._conn)
        """
        Identify the hostname of the PC that builds the xenaserver. It uniquely identifies the build of a xenaserver.

        :type: C_BUILDSTRING
        """

        self.management_interface = mi.ManagementInterface(self._conn)
        """
        The management interface address configuration includes IP address, DHCP settings, MAC address and hostname.

        :type: ManagementInterface
        """

        self.modules: mm.ModulesManager["ml47.ModuleL47"] = mm.ModulesManager(self._conn, get_module_type)
        """
        Module Index Manager of the tester.

        :type: ModulesManager
        """

    @property
    def info(self) -> testers_state.GenuineTesterLocalState:
        """Return tester's local state

        :return: tester's local state
        :rtype: GenuineTesterLocalState
        """
        return self._local_states

    async def _setup(self) -> Self:
        await super()._setup()
        await self._local_states.initiate(self)
        self._local_states.register_subscriptions(self)

        ft_pc = await C_REMOTEPORTCOUNTS(self._conn).get()
        port_counts = ft_pc.port_counts
        await self.modules.fill_l47(port_counts)
        return self
