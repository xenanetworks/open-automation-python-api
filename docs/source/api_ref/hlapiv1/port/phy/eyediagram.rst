Eye Diagram
=========================

Information
-----------------

.. code-block:: python

    await port.serdes[serdex_idx].eye_diagram.info.get()


Bit Error Rate
-----------------

.. code-block:: python

    await port.serdes[serdex_idx].eye_diagram.ber.get()


Dwell Bits
-----------------

.. code-block:: python

    await port.serdes[serdex_idx].eye_diagram.dwell_bits.get()


Measure
-----------------

.. code-block:: python

    await port.serdes[serdex_idx].eye_diagram.measure.get()


Resolution
-----------------

.. code-block:: python

    await port.serdes[serdex_idx].eye_diagram.resolution.get()


Data Columns
-----------------

.. code-block:: python

    await port.serdes[serdex_idx].eye_diagram.read_column