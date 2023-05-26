Configuration
=========================

Impairment On/OFF
-------------------------

.. code-block:: python

    await port.emulate.set_on()
    await port.emulate.set_off()
    await port.emulate.get()
    port.on_emulate_change(_callback_func)


FCS Error Action
-------------------------

.. code-block:: python

    await port.emulation.drop_fcs_errors.set_on()
    await port.emulation.drop_fcs_errors.set_off()
    await port.emulation.drop_fcs_errors.get()


TPLD Mode
-------------------------

.. code-block:: python

    await port.emulation.tpld_mode.set_normal()
    await port.emulation.tpld_mode.set_micro()
    await port.emulation.tpld_mode.get()
