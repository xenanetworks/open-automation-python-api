MACsec RX Secure Channel Creation & Deletion
============================================

Create and Obtain
-----------------

Create a new RX Secure Channel (SC) on the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_RXSC_CREATE`

.. code-block:: python

    txsc_obj = await port_obj.macsec_rxscs.create()


Obtain One
-----------

Obtain an existing RX Secure Channel on the port with an explicit SC index.


.. code-block:: python

    dataset = port_obj.macsec_rxscs.obtain(0)


Obtain Multiple
---------------

Obtain multiple existing RX Secure Channels on the port with explicit SC indices.


.. code-block:: python

    dataset_list = port_obj.macsec_rxscs.obtain_multiple(*[0,1,2])


Remove
---------------

Delete a RX Secure Channel (SC) on the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_RXSC_DELETE`

.. code-block:: python

    # rxsc_obj = await port_obj.macsec_rxscs.create()
    await rxsc_obj.delete()
