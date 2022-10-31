ANLT CLI
=================================

CLI of ANLT Utility for Interactive Mode.

.. important:: 

    Beta version. The functions are subject to changes in the official release of XOA UTIL.

anlt-status
-------------

.. rubric:: Description

Show the current status of auto-negotiation and link training of a Freya port.

.. rubric:: Synopsis

.. code-block:: shell
    
    anlt-status

.. rubric:: Options


an
-------------

.. rubric:: Description

Configure auto-negotiation settings on a Freya port.

.. rubric:: Synopsis

.. code-block:: shell

    an 
    --enable <value> 
    --allow-loopback <value>


.. rubric:: Options

``--enable <value=true|false>`` (bool)
Specifies whether auto-negotiation should be enabled or disabled.

    **true** will enable auto-negotiation.

    **false** will disable auto-negotiation.


``--allow-loopback <value=true|false>`` (bool)
Specifies whether loopback is allowed or not.

    **true** will allow loopback.

    **false** will deny loopback.


an-log
-------------

.. rubric:: Description

Show the autonegotiation trace log.

.. rubric:: Synopsis

.. code-block:: shell
    
    an-log

.. rubric:: Options


an-status
-------------

.. rubric:: Description

Show the autonegotiation status.

.. rubric:: Synopsis

.. code-block:: shell
    
    an-status

.. rubric:: Options



lt
-------------

.. rubric:: Description

Configure link training settings on a Freya port.

.. rubric:: Synopsis

.. code-block:: shell

    an 
    --enable <value> 
    --timeout <value>
    --mode <value>


.. rubric:: Options

``--enable <value=true|false>`` (bool)
Specifies whether link training should be enabled or disabled.

    **true** will enable link training.

    **false** will disable link training.


``--timeout <value=true|false>`` (bool)
Specifies whether link training timeout is enabled or disabled.

    **true** will enable link training timeout.

    **false** will disable link training timeout.


``--mode <value='auto' | 'interactive'>`` (string)
Specifies whether link training timeout is enabled or disabled.

    **'auto'** will enable link training in auto mode.

    **'interactive'** will enable link training in interactive mode.


lt-clear
-------------

.. rubric:: Description

Clear the command sequence for the lane. Lane is relative to the port and start with 0.

.. rubric:: Synopsis

.. code-block:: shell

    lt-clear 
    --lane <value>

.. rubric:: Options

``--lane <value=lane index>`` (int)
Specifies the lane index. Lane is relative to the port and start with 0


lt-nop
-------------

.. rubric:: Description

No operation for the lane, used to indicate interactive use.

.. rubric:: Synopsis

.. code-block:: shell

    lt-nop 
    --lane <value>

.. rubric:: Options

``--lane <value=lane index>`` (int)
Specifies the lane index. Lane is relative to the port and start with 0


lt-coeff-inc
-------------

.. rubric:: Description

Increase coeff of a lane.

.. rubric:: Synopsis

.. code-block:: shell

    lt-coeff-inc 
    --lane <value>
    --coeff <value>
    --value <value>


.. rubric:: Options

``--lane <value=lane index>`` (int)
Specifies the lane index. Lane is relative to the port and start with 0


``--coeff <value=coefficient index>`` (int)
Specifies the coefficient index. coeff 0 = c(-3) ... coeff 4 = c(1).


``--value <value>`` (int)
Specifies the increase value.



lt-coeff-dec
-------------

.. rubric:: Description

Decrease coeff of a lane.

.. rubric:: Synopsis

.. code-block:: shell

    lt-coeff-dec 
    --lane <value>
    --coeff <value>
    --value <value>


.. rubric:: Options

``--lane <value=lane index>`` (int)
Specifies the lane index. Lane is relative to the port and start with 0


``--coeff <value=coefficient index>`` (int)
Specifies the coefficient index. coeff 0 = c(-3) ... coeff 4 = c(1).


``--value <value>`` (int)
Specifies the decrease value.


lt-preset
-------------

.. rubric:: Description

Select a preset for the lane.

.. rubric:: Synopsis

.. code-block:: shell

    lt-preset 
    --lane <value>
    --preset <value>
    [--use <value>]


.. rubric:: Options

``--lane <value=lane index>`` (int)
Specifies the lane index. Lane is relative to the port and start with 0


``--preset <value=preset index>`` (int)
Specifies the preset, value = 1, 2, 3, 4, 5.


lt-preset0
-------------

.. rubric:: Description

Should the preset0 (out-of-sync preset) use existing tap values or standard values.

.. rubric:: Synopsis

.. code-block:: shell

    lt-preset0 
    --lane <value>
    --use <value>


.. rubric:: Options

``--lane <value=lane index>`` (integer)
Specifies the lane index. Lane is relative to the port and start with 0


``--use <value='standard' | 'existing'>`` (string)
Should the preset0 (out-of-sync preset) use existing tap values or standard values.



lt-trained
-------------

.. rubric:: Description

The current lane is trained

.. rubric:: Synopsis

.. code-block:: shell

    lt-trained
    --lane <value>


.. rubric:: Options

``--lane <value=lane index>`` (integer)
Specifies the lane index. Lane is relative to the port and start with 0


lt-log
-------------

.. rubric:: Description

Show the link training trace log per lane.

.. rubric:: Synopsis

.. code-block:: shell

    lt-log
    --lane <value>


.. rubric:: Options

``--lane <value=lane index>`` (integer)
Specifies the lane index. Lane is relative to the port and start with 0


lt-status
-------------

.. rubric:: Description

Show the link training status per lane.

.. rubric:: Synopsis

.. code-block:: shell

    lt-status
    --lane <value>


.. rubric:: Options

``--lane <value=lane index>`` (integer)
Specifies the lane index. Lane is relative to the port and start with 0



txtap-get
-------------

.. rubric:: Description

Get the taps of the local transceiver.

.. rubric:: Synopsis

.. code-block:: shell

    txtap-get
    --lane <value>


.. rubric:: Options

``--lane <value=lane index>`` (integer)
Specifies the lane index. Lane is relative to the port and start with 0



txtap-set
-------------

.. rubric:: Description

Get the taps of the local transceiver.

.. rubric:: Synopsis

.. code-block:: shell

    txtap-get
    --lane <value>
    --coeff <value>


.. rubric:: Options

``--lane <value=lane index>`` (integer)
Specifies the lane index. Lane is relative to the port and start with 0

``--coeff <value= list of coefficient values>`` (list of integer)
Specifies the values for c(-3), c(-2), c(-1), c(0), c(1), e.g. ``--coeff -1 -2 0 56 3``.



connect
-------------

.. rubric:: Description

Connect to tester.

.. rubric:: Synopsis

.. code-block:: shell

    connect
    --host <value>
    --user <value>
    --password <value>


.. rubric:: Options

``--host <value>`` (string)
Specifies the IP address or host name of the chassis.


``--user <value>`` (string)
Specifies the username.


``--password <value>`` (string)
Specifies the login password of the chassis, default to ``'xena'``.


disconnect
-------------

.. rubric:: Description

Disconnect from tester.

.. rubric:: Synopsis

.. code-block:: shell

    disconnect
    --host <value>


.. rubric:: Options

``--host <value>`` (string)
Specifies the IP address or host name of the chassis.


port-reserve
-------------

.. rubric:: Description

Reserve the port for the current use.

.. rubric:: Synopsis

.. code-block:: shell

    port-reserve
    --module <value>
    --port <value>


.. rubric:: Options

``--module <value>`` (integer)
Specifies module index, starting from 0.


``--port <value>`` (integer)
Specifies port index, starting from 0.


port-reset
-------------

.. rubric:: Description

Reset the port.

.. rubric:: Synopsis

.. code-block:: shell

    port-reset
    --module <value>
    --port <value>


.. rubric:: Options

``--module <value>`` (integer)
Specifies module index, starting from 0.


``--port <value>`` (integer)
Specifies port index, starting from 0.