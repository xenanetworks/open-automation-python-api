Speed
=========================

Mode Selection
----------------
The speed mode of an autoneg port with an interface type supporting multiple speeds.

.. note::

    This is only a settable command when speed is selected at the port level. Use the M_CFPCONFIGEXT` command when speed is selected at the module level.

Corresponding CLI command: ``P_SPEEDSELECTION``

.. code-block:: python

    # Speed Mode Selection
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.AUTO)
    await port.speed.mode.selection.set_auto()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F10M)
    await port.speed.mode.selection.set_f10m()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F10M100M)
    await port.speed.mode.selection.set_f10m100m()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F10MHDX)
    await port.speed.mode.selection.set_f10mhdx()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F100M)
    await port.speed.mode.selection.set_f100m()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F100M1G)
    await port.speed.mode.selection.set_f100m1g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F100M1G10G)
    await port.speed.mode.selection.set_f100m1g10g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F100M1G2500M)
    await port.speed.mode.selection.set_f100m1g2500m()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F100MHDX)
    await port.speed.mode.selection.set_f100mhdx()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F1G)
    await port.speed.mode.selection.set_f1g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F2500M)
    await port.speed.mode.selection.set_f2500m()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F5G)
    await port.speed.mode.selection.set_f5g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F10G)
    await port.speed.mode.selection.set_f10g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F40G)
    await port.speed.mode.selection.set_f40g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F100G)
    await port.speed.mode.selection.set_f100g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.UNKNOWN)
    await port.speed.mode.selection.set_unknown()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F200G)
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F400G)
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F800G)
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F1600G)

    resp = await port.speed.mode.selection.get()
    resp.mode


Supported Modes
----------------
Read the speeds supported by the port. The speeds supported by a port depends on
the transceiver inserted into the port. A series of 0/1 values, identifying
which speeds are supported by the port.

.. note::

    Ports can support zero (in case of e.g. empty cage), one, or multiple speeds.

Corresponding CLI command: ``P_SPEEDS_SUPPORTED``

.. code-block:: python

    # Supported Speed Modes
    resp = await port.speed.mode.supported.get()
    resp.auto
    resp.f10M
    resp.f100M
    resp.f1G
    resp.f10G
    resp.f40G
    resp.f100G
    resp.f10MHDX
    resp.f100MHDX
    resp.f10M100M
    resp.f100M1G
    resp.f100M1G10G
    resp.f2500M
    resp.f5G
    resp.f100M1G2500M
    resp.f25G
    resp.f50G
    resp.f200G
    resp.f400G
    resp.f800G
    resp.f1600G


Current Speed
----------------
Obtains the current physical speed of a port's interface.

Corresponding CLI command: ``P_SPEED``

.. code-block:: python

    # Current Speed
    resp = await port.speed.current.get()
    resp.port_speed


Speed Reduction
----------------
A speed reduction applied to the transmitting side of a port, resulting in an effective traffic rate that is slightly lower than the rate of the physical interface. Speed reduction is effectuated by inserting short idle periods in the generated traffic pattern to consume part of the port's physical bandwidth. The port's clock speed is not altered.

Corresponding CLI command: ``P_SPEEDREDUCTION``

.. code-block:: python

    # Speed Reduction
    await port.speed.reduction.set(ppm=100)
    
    resp = await port.speed.reduction.get()
    resp.ppm