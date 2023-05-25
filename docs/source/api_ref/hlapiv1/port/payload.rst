Payload
=========================


Random Seed
-----------

.. code-block:: python

    await port.random_seed.set()
    await port.random_seed.get()


Checksum Offset
------------------

.. code-block:: python
    
    await port.checksum.set()
    await port.checksum.get()
    await port.checksum.set_on()
    await port.checksum.set_off()


Maximum Header Length
---------------------

.. code-block:: python

    await port.max_header_length.set()
    await port.max_header_length.get()


MIX Weights
---------------------

.. code-block:: python

    await port.mix.weights.set()
    await port.mix.weights.get()


MIX Lengths
---------------------

.. code-block:: python

    await port.mix.lengths.set()
    await port.mix.lengths.get()