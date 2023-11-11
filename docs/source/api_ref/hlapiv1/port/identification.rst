Identification
=========================

Interface
----------
Obtains the name of the physical interface type of a port.

Corresponding CLI command: ``P_INTERFACE``

.. code-block:: python

    # Interface
    resp = await port.interface.get()
    resp.interface


Description
-----------
The description of a port.

Corresponding CLI command: ``P_COMMENT``

.. code-block:: python

    # Description
    await port.comment.set(comment="description")
    
    resp = await port.comment.get()
    resp.comment


Optical Signal Level
---------------------
Get the received signal level for optical ports.

Corresponding CLI command: ``P_STATUS``

.. code-block:: python
    
    # Status
    resp = await port.status.get()
    resp.optical_power