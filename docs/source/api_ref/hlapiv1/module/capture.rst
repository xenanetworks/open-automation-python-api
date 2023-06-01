Capture
=========================

.. note::

    For Vulcan module only.


List PCAP Files
--------------------

.. code-block:: python

    await module.capture.file_list.get()


List PCAP BSON Files
--------------------

.. code-block:: python

    await module.capture.file_list_bson.get()


Delete PCAP Files
--------------------

.. code-block:: python

    await module.capture.file_delete.set()


PCAP Parser Configuration
-------------------------

.. code-block:: python

    await module.capture.parse.parser_params.set()
    await module.capture.parse.parser_params.get()


Start PCAP Parser
--------------------

.. code-block:: python

    await module.capture.parse.start.set()


Stop PCAP Parser
--------------------

.. code-block:: python

    await module.capture.parse.stop.set()


PCAP Parser State
--------------------

.. code-block:: python

    await module.capture.parse.state.get()


Buffer Size
--------------------

.. code-block:: python

    await module.capture.size.set_full()
    await module.capture.size.set_small()
    await module.capture.size.get()