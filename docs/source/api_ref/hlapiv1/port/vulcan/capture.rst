Capture
=======

Start
--------------



.. code-block:: python

    await port.capture.start.set_on()
    await port.capture.start.set_off()
    await port.capture.start.get()


Read PCAP
----------------



.. code-block:: python

    await port.capture.get_first_frame.get()
    await port.capture.get_next_frame.get()