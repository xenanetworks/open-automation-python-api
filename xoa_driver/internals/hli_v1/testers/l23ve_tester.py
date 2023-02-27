from typing import Type
from xoa_driver.internals.commands import (
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
    This is a conceptual class of Xena ValkyrieVE Tester.
    It is essentially an extended :class:`BaseTester`.


    :param host: tester's address/hostname
    :type host: str
    :param username: username of the user
    :type username: str
    :param password: login password of the tester, defaults to "xena"
    :type password: str, optional
    :param port: the port number for connection establishment, default to 22606
    :type port: int, optional
    :param debug: `True` if debug log output from the tester is needed, and `False` otherwise
    :type debug: int, optional
    """

    def __init__(self, host: str, username: str, password: str = "xena", port: int = 22606, *, debug: bool = False) -> None:
        super().__init__(host=host, username=username, password=password, port=port, debug=debug)

        self._local_states = testers_state.TesterLocalState(host, port)

        self.multiuser = C_MULTIUSER(self._conn)
        """
        Enable or disable the ability to control one resource from several different TCP connections.
        
        :type:  C_MULTIUSER
        """

        self.traffic = C_TRAFFIC(self._conn)
        """
        Starts or stops the traffic on a number of ports on the chassis simultaneously.
        The ports are identified by pairs of integers (module port).

        :type: C_TRAFFIC
        """

        self.traffic_sync = C_TRAFFICSYNC(self._conn)
        """
        This can be used to start traffic simultaneously on multiple chassis. The ports are identified by pairs of integers (module port).

        :type: C_TRAFFICSYNC
        """

        self.version_no_minor = C_VERSIONNO_MINOR(self._conn)
        """
        Get the minor version number of the tester firmware.

        :type: C_VERSIONNO_MINOR
        """

        self.modules: TypeL23Manager = ModulesManager(self._conn, get_module_type)
        """
        Module Index Manager of the L23 VE tester.

        :type: ModulesManager
        """

    @property
    def info(self) -> testers_state.TesterLocalState:
        """Return tester's local state

        :return: tester's local state
        :rtype: GenuineTesterLocalState
        """
        return self._local_states

    async def _setup(self):
        await super()._setup()
        await self._local_states.initiate(self)
        self._local_states.register_subscriptions(self)

        ft_pc = await C_PORTCOUNTS(self._conn).get()
        port_counts = ft_pc.port_counts
        await self.modules.fill_l23(port_counts)
        return self
