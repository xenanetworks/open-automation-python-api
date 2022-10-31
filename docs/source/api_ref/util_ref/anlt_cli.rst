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

``anlt-status``

.. rubric:: Options


an
-------------

.. rubric:: Description

Enable of disable auto-negotiation on a Freya port.

.. rubric:: Synopsis

.. code-block:: shell

    an 
    --enable <value> 
    --allow-loopback <value>


.. rubric:: Options

``--enable <value>`` (bool)
Specifies whether auto-negotiation should be enabled or disabled.

    **true** will enable auto-negotiation.

    **false** will disable auto-negotiation.


``--allow-loopback <value>`` (bool)
Specifies whether loopback is allowed or not.

    **true** will allow loopback.

    **false** will deny loopback.



.. code-block:: shell

    connect --host <host> --user <username> --password <password>       - Connect to tester
    disconnect --host <host>	                                        - Disconnect from tester
    port-reserve --module <module id> --port <port id>			        - Reserve the port to configure
    port-reset --module <module id> --port <port id>                    - Reset the port 
    help <command>					                                    - Show documentation of <command>

    anlt-status					                                        - The current status of AN/LT

    an --enable < true | false > 			                            - Enable or disable autonegotiation
    --loopback < allow | deny >                                         - Should loopback be allowed in autonegotiation

    an-log              						                        - Show the autonegotiation trace log
    an-status					                                        - Show the autonegotiation status


    lt --enable < true | false > --timeout < enable | disable > -–mode < auto | interactive >
    
    - Enable or disable link training with or without timeout in auto or interactive mode

    lt-clear --lane <lane>	                                        - Clear the command sequence for the lane. 
                                                                    Lane is relative to the port and start with 0
    lt-nop --lane <lane>	                                          - No operation for the lane, used to indicate interactive use
    lt-coeff-inc --lane <lane> --coeff <coeff> --count <count>	    - Increase coeff with <count>, coeff 0 = c(-3) ... coeff 4 = c(1)
    lt-coeff-dec --lane <lane> --coeff <coeff> --count <count>	    - Decrease coeff with <count>, coeff 0 = c(-3) ... coeff 4 = c(1)
    lt-preset --lane <lane> --preset <preset> [--use < existing | standard >] 	                      
                                                                    - Select a preset for the lane, <preset> = 1-5, 
                                                                    and should the preset0 (out-of-sync) use existing tap values or standard values
                                                                    the option --use is ONLY applicable to preset0.

    lt-trained --lane <lane>	                                      - The current lane is trained

    lt-log --lane <lane>				                                    - Show the link training trace log per lane
    lt-status --lane <lane>			                                    - Show the link training status per lane

    txtap-get --lane <lane>                                         - Get the taps of the local transceiver
    txtap-set --lane <lane> --coeff c(-3) c(-2) c(-1) c(0) c(1)     - Set the taps of the local transceiver


.. currentmodule:: xoa_driver.cli


.. autofunction:: anlt_status
    :members:

.. autofunction:: an_status
    :members:

.. autofunction:: anlt_status
    :members:

.. autofunction:: anlt_status
    :members:

.. autofunction:: anlt_status
    :members: