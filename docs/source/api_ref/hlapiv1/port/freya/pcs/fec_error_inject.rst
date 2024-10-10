FEC Error Injection
=========================

Control
--------------------

Start/stop FEC error injection

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_CWE_CONTROL``

.. code-block:: python

    await port.l1.fec_error_inject.control.set(action=enums.StartOrStop.START)
    await port.l1.fec_error_inject.control.set_start()
    await port.l1.fec_error_inject.control.set(action=enums.StartOrStop.STOP)
    await port.l1.fec_error_inject.control.set_stop()

    resp = await port.l1.fec_error_inject.control.get()
    resp.action


Cycle Configuration
--------------------

Configure the FEC codeword error injection cycle.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_CWE_CYCLE`

.. code-block:: python

    await port.l1.fec_error_inject.cycle.set(loop=0, cycle_len=8, error_len=4)
    await port.l1.fec_error_inject.cycle.set(loop=1, cycle_len=8, error_len=4)
    await port.l1.fec_error_inject.cycle.set(loop=100, cycle_len=8, error_len=4)

    resp = await port.l1.fec_error_inject.cycle.get()
    resp.loop
    resp.cycle_len
    resp.error_len

Errored Symbols Per Codeword Configuration
-------------------------------------------

Configure the positions of the errored symbols in errored codewords.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_CWE_ERR_SYM_INDICES`

.. code-block:: python

    await port.l1.fec_error_inject.err_symbols.set(error_sym_indices=[543, 542, 541, 50, 44, 76, 88])

    resp = await port.l1.fec_error_inject.err_symbols.get()
    resp.error_sym_indices

Bit Error Mask Configuration
-------------------------------------------

Configure the bit error mask for the errored symbols.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_CWE_BIT_ERR_MASK`

.. code-block:: python

    await port.l1.fec_error_inject.bit_err_mask.set(mode=enums.FecCodewordBitErrorMaskMode.STATIC, bitmask=Hex("000F"))
    await port.l1.fec_error_inject.bit_err_mask.set(mode=enums.FecCodewordBitErrorMaskMode.ROTATE_HIGH, bitmask=Hex("000F"))
    await port.l1.fec_error_inject.bit_err_mask.set(mode=enums.FecCodewordBitErrorMaskMode.INC, bitmask=Hex("000F"))
    await port.l1.fec_error_inject.bit_err_mask.set_all_bits()
    await port.l1.fec_error_inject.bit_err_mask.set_no_bits()

    resp = await port.l1.fec_error_inject.bit_err_mask.get()
    resp.mode
    resp.bitmask

FEC Engine Configuration
-------------------------------------------

Configure which FEC engines to use.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_CWE_FEC_ENGINE`

.. code-block:: python

    await port.l1.fec_error_inject.engine.set(bitmask=Hex("0F"))
    await port.l1.fec_error_inject.engine.set_all_engines()

    resp = await port.l1.fec_error_inject.engine.get()
    resp.engine_bitmask


Error Injection Statistics
-------------------------------------------

FEC error injection statistics.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_CWE_FEC_STATS`

.. code-block:: python

    resp = await port.l1.fec_error_inject.statistics.get()
    resp.total_cw
    resp.total_correctable_cw
    resp.total_uncorrectable_cw
    resp.total_error_free_cw
    resp.total_symbol_error


Clear Error Injection Statistics
-------------------------------------------

Clear FEC codeword injection TX stats.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_CWE_FEC_STATS_CLEAR`

.. code-block:: python

    await port.l1.fec_error_inject.clear_stats.set()