Signal Integrity
=================

The Signal Integrity feature offers the equivalent of an Equivalent Time oscilloscope trace of the RX PAM4 signal (later, also PAM2). The trace is done with the A/D converter in the GTM receiver also doing the data sampling / CDR function, i.e. the trace is taken after the RX equalizer.

The HW characteristics of the Versal GTM used in Freya are: Trace length = 2000 samples, sample resolution = 7 bits 2's complement, i.e. range = -64..63.

Using the sampled eye scan feature through CLI involves two steps:

Trigger the acquisition of a trace (PL1_CTRL)

Retrieve the trace data (PL1_GET_DATA)

This command is a generic function to retrieve dynamic data related to Layer 1 / SERDES. For now, only used for signal integrity scan.

For ``func==0``, sampled eye scan:

* ``result==0``: No data available.

"No data available" means that either a scan was never started, an acquisition was started and in progress, or the acquired data has become too old (e.g. older than 500 ms). The acquisition time for a trace is in the very low ms-range. If ``result==0``, ``sweep_no`` and ``age_us`` are dummy (=0), and no additional data are returned.

* ``result==1``: Data returned. In that case, the rest of the parameters apply:

``sweep_no``: per-SERDES trace acquisition counter: 1,2,3… Each trace can be returned multiple times, to different users, within its lifetime. A new trace acquisition is triggered with the PL1_CTRL command.

``age_us``: The “age” of the trace data in microseconds, i.e. the time from data acquisition from hardware was completed until the time the command reply data is generated.

``value``: The rest of the reply is a set of 16 bit signed 2-complement sample values. With present hardware, the range of each sample is -64..63. In XMP scripting, each sample value is represented as two bytes, msb first.

With present implementation, 2006 sample values (4012 bytes) are returned.

The first 6 sample values are so-called sampled levels: <p1> <p2> < p3> <m1> <m2> <m3>

Control
-------

.. code-block:: python

    await port.l1.serdes[0].medium.siv.control.set(opcode=enums.Layer1Opcode.START_SCAN)


Data
------

.. code-block:: python
    
    resp = await port.l1.serdes[0].medium.siv.data.get()
    resp.result
    resp.age_us
    resp.sweep_no
    resp.value