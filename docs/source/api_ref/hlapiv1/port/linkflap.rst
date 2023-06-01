Link Flap
=========================

Control
-------------

.. code-block:: python

    await port.pcs_pma.link_flap.enable.set_on()
    await port.pcs_pma.link_flap.enable.set_off()
    await port.pcs_pma.link_flap.enable.get()


Configuration
-------------

.. code-block:: python

    await port.pcs_pma.link_flap.params.set()
    await port.pcs_pma.link_flap.params.get()