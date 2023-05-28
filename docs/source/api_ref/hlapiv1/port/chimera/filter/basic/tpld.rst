TPLD
==========================

.. note::

    Applicable to Chimera port only.


TPLD ID Configuration
---------------------

.. code-block:: python

    await filter.tpld.test_payload_filters_config[idx].set_on(tpld_id_value)
    await filter.tpld.test_payload_filters_config[idx].set_off(tpld_id_value)
    await filter.tpld.test_payload_filters_config[idx].get(tpld_id_value)


Settings
-------------------

.. code-block:: python
    
    await filter.tpld.settings.set()
    await filter.tpld.settings.get()
