High-Speed Port
=================================

This module contains the **L23 high-speed port commands** that provide configuration and status for the Gigabit Attachment Unit Interface (CAUI) physical coding sublayer used by 40G, 50G, 100G, 200G, 400G and 800G ports. The data is broken down into a number of lower-speed lanes. For 40G there are 4 lanes of 10 Gbps each. For 100G there are 20 lanes of 5 Gbps each. Within each lane the data is broken down into 66-bit code-words.

During transport, the lanes may be swapped and skewed with respect to each other. To deal with this, each lane contains marker words with a virtual lane index id. The commands are indexed with a physical lane index that corresponds to a fixed numbering of the underlying fibers or wavelengths.

The lanes can also be put into :term:`Pseudorandom Binary Sequence (PRBS)<PRBS>` mode where they transmit a bit pattern used for diagnosing fiber-level problems, and the receiving side can lock to these patterns.

Errors can be injected both at the CAUI level and at the bit level.

The high-speed port command names all have the form ``PP_<xxx>`` and require a module index id and a port index id, and most also require a physical lane index id.


.. currentmodule:: xoa_driver.internals.core.commands.pp_commands

PP_ALARMS_ERRORS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_ALARMS_ERRORS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_TXLANECONFIG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_TXLANECONFIG
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_TXLANEINJECT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_TXLANEINJECT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_TXPRBSCONFIG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_TXPRBSCONFIG
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_TXERRORRATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_TXERRORRATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_TXINJECTONE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_TXINJECTONE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_RXTOTALSTATS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_RXTOTALSTATS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_RXFECSTATS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_RXFECSTATS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_LINKFLAP_PARAMS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_LINKFLAP_PARAMS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_LINKFLAP_ENABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_LINKFLAP_ENABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_PMAERRPUL_PARAMS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_PMAERRPUL_PARAMS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_RXLANELOCK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_RXLANELOCK
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_RXLANESTATUS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_RXLANESTATUS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_RXLANEERRORS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_RXLANEERRORS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_RXPRBSSTATUS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_RXPRBSSTATUS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_RXCLEAR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_RXCLEAR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_RXLASERPOWER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_RXLASERPOWER
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_TXLASERPOWER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_TXLASERPOWER
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_PMAERRPUL_ENABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_PMAERRPUL_ENABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_EYEMEASURE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_EYEMEASURE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_EYERESOLUTION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_EYERESOLUTION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_EYEREAD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_EYEREAD
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_EYEINFO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_EYEINFO
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_PHYTXEQ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_PHYTXEQ
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_PHYRETUNE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_PHYRETUNE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_PHYAUTOTUNE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_PHYAUTOTUNE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_EYEBER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_EYEBER
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_PHYAUTONEG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_PHYAUTONEG
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_TXPRBSTYPE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_TXPRBSTYPE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_RXPRBSTYPE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_RXPRBSTYPE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_FECMODE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_FECMODE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_EYEDWELLBITS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_EYEDWELLBITS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_PHYSIGNALSTATUS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_PHYSIGNALSTATUS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_PRBSTYPE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_PRBSTYPE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_PHYSETTINGS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_PHYSETTINGS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_PHYRXEQ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_PHYRXEQ
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_AUTONEG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_AUTONEG
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_AUTONEGSTATUS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_AUTONEGSTATUS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_LINKTRAIN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_LINKTRAIN
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PP_LINKTRAINSTATUS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PP_LINKTRAINSTATUS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr

