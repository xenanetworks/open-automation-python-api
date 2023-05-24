High-Speed Port Classes
=================================

This module contains the **L23 high-speed port classes** that provide configuration and status for the Gigabit Attachment Unit Interface (CAUI) physical coding sublayer used by 40G, 50G, 100G, 200G, 400G and 800G ports. The data is broken down into a number of lower-speed lanes. For 40G there are 4 lanes of 10 Gbps each. For 100G there are 20 lanes of 5 Gbps each. Within each lane the data is broken down into 66-bit code-words.

During transport, the lanes may be swapped and skewed with respect to each other. To deal with this, each lane contains marker words with a virtual lane index id. The commands are indexed with a physical lane index that corresponds to a fixed numbering of the underlying fibers or wavelengths.

The lanes can also be put into :term:`Pseudorandom Binary Sequence (PRBS)<PRBS>` mode where they transmit a bit pattern used for diagnosing fiber-level problems, and the receiving side can lock to these patterns.

Errors can be injected both at the CAUI level and at the bit level.

The high-speed port command names all have the form ``PP_<xxx>`` and require a module index id and a port index id, and most also require a physical lane index id.


-------

.. automodule:: xoa_driver.internals.commands.pp_commands
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr, __init__
