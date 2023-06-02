Speed
=========================

Mode Selection
----------------

.. code-block:: python

    await port.speed.mode.selection.set_auto()
    await port.speed.mode.selection.set_f10m()
    await port.speed.mode.selection.set_f10m100m()
    await port.speed.mode.selection.set_f10mhdx()
    await port.speed.mode.selection.set_f100m()
    await port.speed.mode.selection.set_f100m1g()
    await port.speed.mode.selection.set_f100m1g10g()
    await port.speed.mode.selection.set_f100m1g2500m()
    await port.speed.mode.selection.set_f100mhdx()
    await port.speed.mode.selection.set_f1g()
    await port.speed.mode.selection.set_f2500m()
    await port.speed.mode.selection.set_f5g()
    await port.speed.mode.selection.set_f10g()
    await port.speed.mode.selection.set_f40g()
    await port.speed.mode.selection.set_f100g()
    await port.speed.mode.selection.set_unknown()
    await port.speed.mode.selection.get()

    port.on_speed_change(_callback_func)
    port.on_speed_selection_change(_callback_func)


Supported Modes
----------------

.. code-block:: python

    await port.speed.mode.supported.get()


Current Speed
----------------

.. code-block:: python

    await port.speed.current.get()


Speed Reduction
----------------

.. code-block:: python

    await port.speed.reduction.set()
    await port.speed.reduction.get()