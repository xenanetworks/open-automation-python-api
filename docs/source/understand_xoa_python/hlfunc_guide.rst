.. _hl_func_label:

High-Level Functions
===================================

HL-FUNC provides high-level abstraction functions on top of the object-oriented APIs in HL-API, aiming to help you simplify code logics and increase readability and maintainability. HL-FUNC consists of sub-libraries where functions are grouped based on functionalities, such as :term:`ANLT<ANLT>`. Complex operation sequences are wrapped inside high-level functions, e.g. initiating link training, reserving ports, etc.

.. code-block:: python

    from xoa_driver.hlfuncs import anlt, mgmt

    # Regardless of who owns the port, this function makes sure you have the ownership.
    await mgmt.reserve_port(port, force=True)

    # Tells the remote link training partner to increase its emphasis register value by 1 bit.
    await anlt.lt_coeff_inc(port=port, lane=0, emphasis=LinkTrainCoeffs.PRE)

The object-oriented APIs in HL-API and the command classes in LL-API are one-to-one mapped, and there is no abstraction provided by the HL-API. As a test specialist, your focus is on building test logics and sequences, not spending unnecessary time on "logistics", such as reserving ports, releasing your ports, deleting all streams on a port without resetting, etc.

To help you simplify code complexity, speed up development, increase readability and maintainability, HL-FUNC is added as the topmost layer, providing abstract functions to the frequently used operations.

Auto-Negotiation and Link Training
------------------------------------

Auto-Negotiation and Link Training (ANLT) provides functions to help you fine-tune the protocol to its optimal state, test interoperability between different vendors, and protocol compliance for different implementations.

Auto-negotiation (AN) was originally designed for Ethernet over twisted pair up to 1G. Beyond exchanging speed capabilities for the link participants, AN has evolved for today's Ethernet to include additional configuration information for establishing reliable and consistent connections. AN allows the devices at the end points of a link to negotiate common transmission parameters capabilities like speed and duplex mode, exchange extended page information and media signaling support. At higher speeds and signaling the choice of FEC may be relevant. It is during auto negotiation the end points of a link share their capabilities and choose the highest performance transmission mode they both support.

.. figure:: ../_static/autoneg_process.png
    :scale: 70 %
    :align: center

    `Auto-Negotiation Process <https://xenanetworks.com/whitepaper/autoneg-link-training/>`_

Once the ports in the link have completed the requisite AN information exchange and reached agreement, the link partners move to the next step, link training (LT), the exchange of Training Sequences. This is essential to tune the channels for optimal transmission. During link training the two end points of the link will exchange signals.

.. figure:: ../_static/linktraining_process.png
    :scale: 70 %
    :align: center

    `Link Training Process <https://xenanetworks.com/whitepaper/autoneg-link-training/>`_

.. rubric:: No Auto Negotiation, No Link Training

In some instances, Auto negotiation and Link Training are not required to establish a communication path: High speed optical transceivers and interfaces typically only run at one speed, so there is no need the negotiate this. Link Training is only required for electrical interfaces - in some cases (e.g. when short cables are used) an electrical interface may become operational just using default settings of the terminal equipment in the communication path. The IEEE 802.3by specification allows for force connect over electrical interfaces in these instances.

.. rubric:: No Auto Negotiation, Link Training

While Link Training can be essential to make some electrical interfaces work, Auto negotiation may not be required is the link speed is fixed or if it can be manually set at both end points of a link.

.. rubric:: Auto Negotiation and Link Training

Auto negotiation and Link Training are in principle two independent processes. However, when both are done, Auto negotiation must be done first to determine the overall mode for a link and then perform the Link Training. Hereby you get the sequence shown in the figure below.

.. figure:: ../_static/aneg_lt_seq.png
    :scale: 70 %
    :align: center

    `Auto-Negotiation and Link Training Sequence <https://xenanetworks.com/whitepaper/autoneg-link-training/>`_

.. seealso::

    Read more about `Auto Negotiation and Link Training on NRZ and PAM4 based Ethernet Interfaces <https://xenanetworks.com/whitepaper/autoneg-link-training/>`_.


In HL-FUNC, you can find the following functionalities to do auto-negotiation and link training tests.

AN Functionalities
^^^^^^^^^^^^^^^^^^^^

1. Enable/disable auto-negotiation
2. Auto-negotiation trace log, provides AN trace log for debugging and troubleshooting.
3. Auto-negotiation status, provides the following AN status:

   * Received and transmitted number of Link Code Words (Base Pages), message pages, and unformatted pages
   * Number of HCD (Highest Common Denominator) failures
   * Number of FEC failures
   * Number of LOS (Loss of Sync) failures
   * Number of timeouts
   * Number of successes
   * Duration of AN in microseconds

LT Functionalities
^^^^^^^^^^^^^^^^^^^^^

1. Enable/disable link training
2. Allow/deny link training loopback
3. Enable/disable link training timeout
4. Tuning link partner TX EQ coefficient, use presets as a starting point to tune link partner TX EQ coefficients per lane, increment and decrement of coefficients c(-3), c(-2), c(-1), c(0), c(1).
5. Configure local TX EQ coefficients
6. Monitor local TX EQ coefficients
7. Link training trace log per lane
8. Link training status per lane, provides the following LT status:

   * Number of lost locks
   * Local value of coefficient (per coefficient)
   * RX number of increment/decrement requests from link partner (per coefficient)
   * RX number of EQ coefficient request limits reached from link partner (per coefficient)
   * RX number of EQ request limits reached from link partner (per coefficient)
   * RX number of coefficients not supported from link partner (per coefficient)
   * RX number of coefficients at limit from link partner (per coefficient)
   * TX number of increment/decrement requests to link partner (per coefficient)
   * TX number of EQ coefficient request limits reached to link partner (per coefficient)
   * TX number of EQ request limits reached to link partner (per coefficient)
   * TX number of coefficients not supported to link partner (per coefficient)
   * TX number of coefficients at limit to link partner (per coefficient)
   * Duration of LT in microseconds
   * PRBS total error bits
   * PRBS total error bits
   * PRBS bit error rate
   * Local frame lock status
   * Link partner frame lock status


CLI Integration
------------------------------------

The XOA Python API allows users to interact with Xena Networks test equipment using Python code, providing an object-oriented and user-friendly interface for automating network testing tasks. It enables users to create and execute test scenarios, generate traffic, and analyze network performance using Python programming language. On the other hand, the XOA CLI allows users to configure and control Xena test equipment through command-line commands. It provides a familiar and efficient way to interact with the equipment, allowing users to perform various configuration tasks, manage ports, and execute test commands.

By leveraging both the XOA Python API and XOA CLI, users can take advantage of the best of both worlds. They can harness the power of Python for automation, scripting, and advanced data analysis while utilizing the precise control and configuration options provided by the CLI commands. With the XOA Python API, users can seamlessly work with CLI commands and port configuration files from ValkyrieManager, streamlining the configuration process. Whether users prefer a programming approach or a straightforward command-line interface, both options are available to suit different requirements and preferences when working with Xena test equipment. This synergy enhances the overall testing experience, enabling users to perform complex testing tasks efficiently and effectively.

1. Send tester configuration from a configuration file
2. Send module configuration from a configuration file
3. Send port configuration from a configuration file (.xpc file)
4. Send tester configuration from a string
5. Send module configuration from a string
6. Send port configuration from a string

Test Resource Management
------------------------------------

As described in :doc:`../test_resource_mgt`, you need to reserve the test resource (chassis/module/port) to do `set` operations. In order to achieve this, you need to first check the ownership of the test resource, and relinquish it in case it is owned by someone else, and then reserve it. Such as sequence of operations can be simplified by the high-level abstraction functions in UTIL.

1. Connect to chassis
2. Reserve/Release/Reset ports
3. Reserve/Release chassis (in future release)
4. Reserve/Release module (in future release)
5. Disconnect