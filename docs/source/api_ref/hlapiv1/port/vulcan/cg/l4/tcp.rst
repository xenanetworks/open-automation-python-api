TCP
=========================

ACK Configuration
-----------------------

.. code-block:: python

    await cg.tcp.ack.duplicate_thresholds.set()
    await cg.tcp.ack.duplicate_thresholds.get()

    await cg.tcp.ack.frequency.set()
    await cg.tcp.ack.frequency.get()

    await cg.tcp.ack.timeout.set()
    await cg.tcp.ack.timeout.get()


Congestion Control
----------------------

.. code-block:: python

    await cg.tcp.cwnd.congestion_mode.set_none()
    await cg.tcp.cwnd.congestion_mode.set_new_reno()
    await cg.tcp.cwnd.congestion_mode.set_reno()
    await cg.tcp.cwnd.congestion_mode.get()


Initial CWND
----------------------

.. code-block:: python

    await cg.tcp.cwnd.icwnd_calc_method.set_fixed_factor()
    await cg.tcp.cwnd.icwnd_calc_method.set_rfc2581()
    await cg.tcp.cwnd.icwnd_calc_method.set_rfc5681()
    await cg.tcp.cwnd.icwnd_calc_method.get()


Initial Slow Slart
----------------------

.. code-block:: python

    await cg.tcp.iss_treshold.set_automatic()
    await cg.tcp.iss_treshold.set_manual()
    await cg.tcp.iss_treshold.get()


Max Segment Size - Fixed
------------------------

.. code-block:: python

    await cg.tcp.mss.fixed_value.set()
    await cg.tcp.mss.fixed_value.get()


Max Segment Size - Varying
--------------------------

.. code-block:: python

    await cg.tcp.mss.range_limits.set()
    await cg.tcp.mss.range_limits.get()

    await cg.tcp.mss.type.set_fixed()
    await cg.tcp.mss.type.set_increment()
    await cg.tcp.mss.type.set_random()
    await cg.tcp.mss.type.get()


RWND Scaling
----------------------

.. code-block:: python

    await cg.tcp.rwnd.scaling.set_yes()
    await cg.tcp.rwnd.scaling.set_no()
    await cg.tcp.rwnd.scaling.get()


RWND Size
----------------------

.. code-block:: python

    await cg.tcp.rwnd.size.set()
    await cg.tcp.rwnd.size.get()


Retransmission Timeout Prolonged Mode
--------------------------------------

.. code-block:: python

    await cg.tcp.rto.prolonged_mode.set_disable()
    await cg.tcp.rto.prolonged_mode.set_enable()
    await cg.tcp.rto.prolonged_mode.get()

Retransmission Timeout Range
--------------------------------------

.. code-block:: python

    await cg.tcp.rto.range_limits.set()
    await cg.tcp.rto.range_limits.get()

SYN Retransmission Timeout
--------------------------------------

.. code-block:: python

    await cg.tcp.rto.syn_value.set()
    await cg.tcp.rto.syn_value.get()