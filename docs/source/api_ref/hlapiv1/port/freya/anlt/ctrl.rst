Control
=======

Enable/disable AN and LT

.. code-block:: python

    await port.l1.anlt.ctrl.enable_an_lt_auto()
    await port.l1.anlt.ctrl.disable_anlt()
    await port.l1.anlt.ctrl.enable_an_lt_interactive()
    await port.l1.anlt.ctrl.enable_an_only()
    await port.l1.anlt.ctrl.enable_an_lt_auto()
    await port.l1.anlt.ctrl.enable_lt_interactive_only()