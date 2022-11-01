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

None

.. rubric:: Example

.. tab:: Windows
    
    .. code-block:: shell
        :caption: ``anlt-status`` in Windows environment.

        > anlt-status

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``anlt-status`` in macOS/Linux environment.

        $ anlt-status


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

``--enable <value=true|false>`` (boolean)
Specifies whether auto-negotiation should be enabled or disabled.

    **true** will enable auto-negotiation.

    **false** will disable auto-negotiation.


``--allow-loopback <value=true|false>`` (boolean)
Specifies whether loopback is allowed or not.

    **true** will allow loopback.

    **false** will deny loopback.


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``an`` in Windows environment.

        > an --enable true --allow-loopback true

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``an`` in macOS/Linux environment.

        $ an --enable true --allow-loopback true


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

None

.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``an-status`` in Windows environment.

        > an-status 

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``an-status`` in macOS/Linux environment.

        $ an-status


lt
-------------

.. rubric:: Description

Configure link training settings on a Freya port.

.. rubric:: Synopsis

.. code-block:: shell

    an 
    --enable <value> 
    --with-timeout <value>
    --mode <value>


.. rubric:: Options

``--enable <value=true|false>`` (boolean)
Specifies whether link training should be enabled or disabled.

    **true** will enable link training.

    **false** will disable link training.


``--with-timeout <value=true|false>`` (boolean)
Specifies whether link training timeout is enabled or disabled.

    **true** will enable link training timeout.

    **false** will disable link training timeout.


``--mode <value='auto' | 'interactive'>`` (string)
Specifies whether link training timeout is enabled or disabled.

    **'auto'** will enable link training in auto mode.

    **'interactive'** will enable link training in interactive mode.


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``lt`` in Windows environment.

        > lt --enable true --timeout false --mode 'interactive'

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``lt`` in macOS/Linux environment.

        $ lt --enable true --timeout false --mode 'interactive'


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


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``lt-clear`` in Windows environment.

        > lt-clear

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``lt-clear`` in macOS/Linux environment.

        $ lt-clear



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


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``lt-nop`` in Windows environment.

        > lt-nop

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``lt-nop`` in macOS/Linux environment.

        $ lt-nop



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
Specifies the coefficient index. 0 = c(-3), 1 = c(-2), 2 = c(-1), 3 = c(0), 4 = c(1).


``--value <value>`` (int)
Specifies the increase value.



.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``lt-coeff-inc`` in Windows environment.

        > lt-coeff-inc --lane 1 --coeff 3 --value 56

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``lt-coeff-inc`` in macOS/Linux environment.

        $ lt-coeff-inc --lane 1 --coeff 3 --value 56


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
Specifies the coefficient index. 0 = c(-3), 1 = c(-2), 2 = c(-1), 3 = c(0), 4 = c(1).


``--value <value>`` (int)
Specifies the decrease value.


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``lt-coeff-dec`` in Windows environment.

        > lt-coeff-dec --lane 1 --coeff 3 --value 56

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``lt-coeff-dec`` in macOS/Linux environment.

        $ lt-coeff-dec --lane 1 --coeff 3 --value 56



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


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``lt-preset`` in Windows environment.

        > lt-preset --lane 1 --preset 1

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``lt-preset`` in macOS/Linux environment.

        $ lt-preset --lane 1 --preset 1


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

``--lane <value=lane index>`` (int)
Specifies the lane index. Lane is relative to the port and start with 0


``--use <value='standard' | 'existing'>`` (string)
Should the preset0 (out-of-sync preset) use existing tap values or standard values.


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``lt-preset0`` in Windows environment.

        > lt-preset0 --lane 1 --use 'standard'

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``lt-preset`` in macOS/Linux environment.

        $ lt-preset0 --lane 1 --use 'standard'


lt-trained
-------------

.. rubric:: Description

The current lane is trained

.. rubric:: Synopsis

.. code-block:: shell

    lt-trained
    --lane <value>


.. rubric:: Options

``--lane <value=lane index>`` (int)
Specifies the lane index. Lane is relative to the port and start with 0


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``lt-trained`` in Windows environment.

        > lt-trained --lane 1

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``lt-trained`` in macOS/Linux environment.

        $ lt-trained --lane 1


lt-log
-------------

.. rubric:: Description

Show the link training trace log per lane.

.. rubric:: Synopsis

.. code-block:: shell

    lt-log
    --lane <value>


.. rubric:: Options

``--lane <value=lane index>`` (int)
Specifies the lane index. Lane is relative to the port and start with 0


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``lt-log`` in Windows environment.

        > lt-log --lane 1

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``lt-log`` in macOS/Linux environment.

        $ lt-log --lane 1


lt-status
-------------

.. rubric:: Description

Show the link training status per lane.

.. rubric:: Synopsis

.. code-block:: shell

    lt-status
    --lane <value>


.. rubric:: Options

``--lane <value=lane index>`` (int)
Specifies the lane index. Lane is relative to the port and start with 0


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``lt-status`` in Windows environment.

        > lt-status --lane 1

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``lt-status`` in macOS/Linux environment.

        $ lt-status --lane 1


txtap-get
-------------

.. rubric:: Description

Get the taps of the local transceiver.

.. rubric:: Synopsis

.. code-block:: shell

    txtap-get
    --lane <value>


.. rubric:: Options

``--lane <value=lane index>`` (int)
Specifies the lane index. Lane is relative to the port and start with 0


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``txtap-get`` in Windows environment.

        > txtap-get --lane 1

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``txtap-get`` in macOS/Linux environment.

        $ txtap-get --lane 1


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

``--lane <value=lane index>`` (int)
Specifies the lane index. Lane is relative to the port and start with 0

``--coeff <value= list of coefficient values>`` (list of int)
Specifies the values for c(-3), c(-2), c(-1), c(0), c(1), e.g. ``--coeff -1 -2 0 56 3``.

.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``txtap-set`` in Windows environment.

        > txtap-set --lane 1 --coeff -1 -2 0 56 3

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``txtap-set`` in macOS/Linux environment.

        $ txtap-set --lane 1 --coeff -1 -2 0 56 3


link-recovery
--------------

.. rubric:: Description

Enable or disable xenaserver's auto link recovery function.

.. rubric:: Synopsis

.. code-block:: shell

    link-recovery
    --enable <value>


.. rubric:: Options

``--enable <value=true|false>`` (boolean)
Specifies whether xenaserver should enable its auto link recovery function.

.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``link-recovery`` in Windows environment.

        > link-recovery --enable false

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``link-recovery`` in macOS/Linux environment.

        $ link-recovery --enable false


connect
-------------

.. rubric:: Description

Connect to tester.

.. rubric:: Synopsis

.. code-block:: shell

    connect
    --host <value>
    --username <value>
    [--password <value>]
    [--port <value>]


.. rubric:: Options

``--host <value>`` (string)
Specifies the IP address or host name of the chassis.


``--username <value>`` (string)
Specifies the username.


``--password <value>`` (string)
Specifies the login password of the chassis, default to ``'xena'``.


``--port <value>`` (int)
Specifies the port number for establishing the TCP connection, default to ``22606``.

.. rubric:: Example

.. tab:: Windows
    :new-set:

    .. code-block:: shell
        :caption: ``connect`` in Windows environment.

        > connect --host 192.168.1.6 --username peter --password xena --port 22606

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``connect`` in macOS/Linux environment.

        $ connect --host 192.168.1.6 --username peter --password xena --port 22606


disconnect (planned)
---------------------

.. rubric:: Description

Disconnect from tester.

.. rubric:: Synopsis

.. code-block:: shell

    disconnect
    --host <value>


.. rubric:: Options

``--host <value>`` (string)
Specifies the IP address or host name of the chassis.


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``disconnect`` in Windows environment.

        > disconnect --host 192.168.1.6

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``disconnect`` in macOS/Linux environment.

        $ disconnect --host 192.168.1.6


quit
---------------------

.. rubric:: Description

Quit the current session

.. rubric:: Synopsis

.. code-block:: shell

    quit


.. rubric:: Options

None


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``quit`` in Windows environment.

        > quit

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``quit`` in macOS/Linux environment.

        $ quit


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

``--module <value>`` (int)
Specifies module index, starting from 0.


``--port <value>`` (int)
Specifies port index, starting from 0.


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``port-reserve`` in Windows environment.

        > port-reserve --module 0 --port 1

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``port-reserve`` in macOS/Linux environment.

        $ port-reserve --module 0 --port 1


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

``--module <value>`` (int)
Specifies module index, starting from 0.


``--port <value>`` (int)
Specifies port index, starting from 0.


.. rubric:: Example

.. tab:: Windows
    :new-set:
    
    .. code-block:: shell
        :caption: ``port-reset`` in Windows environment.

        > port-reset --module 0 --port 1

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: ``port-reset`` in macOS/Linux environment.

        $ port-reset --module 0 --port 1