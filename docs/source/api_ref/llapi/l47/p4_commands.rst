Port Classes
=================================

This module contains the **L47 port classes**.

The Xena L47 test execution engine has seven states: ``off``, ``prepare``, ``prepare_rdy``, ``prerun``, ``prerun_rdy``, ``running`` and ``stopped``. Traffic is generated in the ``prerun`` and running states only, and configuration of parameters is only valid in state ``off`` except for a few runtime options. Port traffic commands can be given with :class:`~xoa_driver.internals.commands.p4_commands.P4_TRAFFIC` and port state queried by :class:`~xoa_driver.internals.commands.p4_commands.P4_STATE`.

* ``off`` - default state. Entered from stopped or prepare on ``OFF`` command. This is the only state that allows configuration commands. :class:`~xoa_driver.internals.commands.p_commands.P_RESET` is also considered a configuration command. Upon entering off state, some internal ''house cleaning''' is done. For example: freeing TCP Connections, clearing test specific counters etc.

* ``prepare`` - this state is entered from state off on ``PREPARE`` command. Here internal data structures relevant for the test configuration are created.

* ``prepare_rdy`` - entered automatically after activities in prepare have completed successfully.

* ``prepare_fail`` - entered automatically from prepare, if an error occurs. An error could for example be failure to load a configured replay file.

* ``prerun`` - entered from ``prepare_ready`` on ``PRERUN`` command. If enabled, this is where ARP and NDP requests are sent.

* ``prerun_rdy`` - entered automatically after activities in prerun have completed.

* ``running`` - entered either from ``prepare_ready`` or ``prerun_ready`` on ``ON`` command. This is where TCP connections are established, payload is generated and connections are closed again.

* ``stopping`` - entered from ``running``, ``prerun_ready`` or ``prerun`` on ``STOP`` command. Stops Rx/Tx traffic. In the ``stopping`` state, post-test data are calculated and captured packets are saved to files.

* ``stopped`` - entered automatically after activities in ``stopping`` are complete. This is where you can read post-test statistics and extract captured packets.

-------

.. automodule:: xoa_driver.internals.commands.p4_commands
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr, __init__

