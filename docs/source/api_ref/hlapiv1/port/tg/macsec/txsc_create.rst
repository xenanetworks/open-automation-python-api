MACsec TX Secure Channel Creation & Deletion
============================================

Create and Obtain
-----------------

Create a new TX Secure Channel (SC) on the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_CREATE`

.. code-block:: python

    txsc_obj = await port_obj.macsec_txscs.create()


Obtain One
-----------

Obtain an existing TX Secure Channel on the port with an explicit SC index.


.. code-block:: python

    dataset = port_obj.macsec_txscs.obtain(0)


Obtain Multiple
---------------

Obtain multiple existing TX Secure Channels on the port with explicit SC indices.


.. code-block:: python

    dataset_list = port_obj.macsec_txscs.obtain_multiple(*[0,1,2])


Remove
---------------

Delete a TX Secure Channel (SC) on the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_DELETE`

.. code-block:: python

    # txsc_obj = await port_obj.macsec_txscs.create()
    await txsc_obj.delete()
