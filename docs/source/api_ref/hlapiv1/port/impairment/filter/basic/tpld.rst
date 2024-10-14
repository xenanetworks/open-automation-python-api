TPLD
==========================

.. note::

    Applicable to Chimera port only.


TPLD ID Configuration
---------------------
Defines the TPLD filter configuration. There are only 16 TPLD filter, thus the index values are from 0 to 15.

.. note::

    For SET, the only allowed ``_filter_type`` is ``shadow-copy``.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_TPLDCONFIG`

.. code-block:: python

    await filter.tpld.test_payload_filters_config[0].set(use=enums.OnOff.ON, id = 2)
    await filter.tpld.test_payload_filters_config[0].set(use=enums.OnOff.OFF, id = 2)
    await filter.tpld.test_payload_filters_config[1].set(use=enums.OnOff.ON, id = 4)
    await filter.tpld.test_payload_filters_config[1].set(use=enums.OnOff.OFF, id = 4)
    await filter.tpld.test_payload_filters_config[2].set(use=enums.OnOff.ON, id = 6)
    await filter.tpld.test_payload_filters_config[2].set(use=enums.OnOff.OFF, id = 6)
    await filter.tpld.test_payload_filters_config[3].set(use=enums.OnOff.ON, id = 8)
    await filter.tpld.test_payload_filters_config[3].set(use=enums.OnOff.OFF, id = 8)
    await filter.tpld.test_payload_filters_config[4].set(use=enums.OnOff.ON, id = 10)
    await filter.tpld.test_payload_filters_config[4].set(use=enums.OnOff.OFF, id = 10)
    await filter.tpld.test_payload_filters_config[5].set(use=enums.OnOff.ON, id = 20)
    await filter.tpld.test_payload_filters_config[5].set(use=enums.OnOff.OFF, id = 20)
    await filter.tpld.test_payload_filters_config[6].set(use=enums.OnOff.ON, id = 40)
    await filter.tpld.test_payload_filters_config[6].set(use=enums.OnOff.OFF, id = 40)
    await filter.tpld.test_payload_filters_config[7].set(use=enums.OnOff.ON, id = 60)
    await filter.tpld.test_payload_filters_config[7].set(use=enums.OnOff.OFF, id = 60)
    await filter.tpld.test_payload_filters_config[8].set(use=enums.OnOff.ON, id = 80)
    await filter.tpld.test_payload_filters_config[8].set(use=enums.OnOff.OFF, id = 80)
    await filter.tpld.test_payload_filters_config[9].set(use=enums.OnOff.ON, id = 100)
    await filter.tpld.test_payload_filters_config[9].set(use=enums.OnOff.OFF, id = 100)
    await filter.tpld.test_payload_filters_config[10].set(use=enums.OnOff.ON, id = 102)
    await filter.tpld.test_payload_filters_config[10].set(use=enums.OnOff.OFF, id = 102)
    await filter.tpld.test_payload_filters_config[11].set(use=enums.OnOff.ON, id = 104)
    await filter.tpld.test_payload_filters_config[11].set(use=enums.OnOff.OFF, id = 104)
    await filter.tpld.test_payload_filters_config[12].set(use=enums.OnOff.ON, id = 106)
    await filter.tpld.test_payload_filters_config[12].set(use=enums.OnOff.OFF, id = 106)
    await filter.tpld.test_payload_filters_config[13].set(use=enums.OnOff.ON, id = 108)
    await filter.tpld.test_payload_filters_config[13].set(use=enums.OnOff.OFF, id = 108)
    await filter.tpld.test_payload_filters_config[14].set(use=enums.OnOff.ON, id = 110)
    await filter.tpld.test_payload_filters_config[14].set(use=enums.OnOff.OFF, id = 110)
    await filter.tpld.test_payload_filters_config[15].set(use=enums.OnOff.ON, id = 200)
    await filter.tpld.test_payload_filters_config[15].set(use=enums.OnOff.OFF, id = 200)

    resp = await filter.tpld.test_payload_filters_config[0].get()
    resp.use
    resp.id


Settings
-------------------
Defines if filtering on TPLD field in a packet is used for flow filtering. The
TPLD filter allows filtering based on the Xena TPLD ID. The TPLD
ID is meta data, which can be inserted into the Ethernet packets by Xena traffic
generators. For each flow filter, can the filter be based on 16 TPLD ID values.

.. note::

    For SET, the only allowed ``_filter_type`` is ``shadow-copy``.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_TPLDSETTINGS`

.. code-block:: python
    
    await filter.tpld.settings.set(action=enums.InfoAction.EXCLUDE)
    await filter.tpld.settings.set(action=enums.InfoAction.INCLUDE)

    resp = await filter.tpld.settings.get()
    resp.action
