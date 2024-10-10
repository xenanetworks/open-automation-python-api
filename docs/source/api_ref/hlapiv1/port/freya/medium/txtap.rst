TX Tap
=========================

mV/dB
------
Control and monitor the equalizer settings of the on-board PHY in the transmission direction (towards the transceiver cage).

* pre3 tap value in dB/10, ranges from 0 to 71. Default = 0 (neutral)
* pre2 tap value in dB/10, ranges from 0 to 71. Default = 0 (neutral)
* pre tap value in dB/10, ranges from 0 to 187. Default = 0 (neutral)
* main tap value in mV, ranges from 507 to 998.
* post tap value in dB/10, ranges from 0 to 187 Default = 0 (neutral)

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_PHYTXEQ_LEVEL`

.. code-block:: python

    await port.l1.serdes[0].medium.tx.level.set(pre3=, pre2=, pre=, main=, post=)

    resp = await port.l1.serdes[0].medium.tx.level.get()
    resp.pre3
    resp.pre2
    resp.pre
    resp.main
    resp.post

IEEE
------
Control and monitor the equalizer settings of the on-board PHY in the transmission direction (towards the transceiver cage).

* pre3 tap value, negative, scaled by 1E3. Default = 0 (neutral)
* pre2 tap value, positive, scaled by 1E3. Default = 0 (neutral)
* pre tap value, negative, scaled by 1E3. Default = 0 (neutral)
* main tap value, positive, scaled by 1E3. Default = 1000
* post tap value, negative, scaled by 1E3. Default = 0 (neutral)

The following rules apply:

    * 0.5 approx. ≤ main ≤ 1
    * -0.4 approx ≤ post ≤ 0
    * -0.4 approx ≤ pre ≤ 0
    * 0 ≤ pre2 ≤ 0.25 approx.
    * -0.25 approx ≤ pre3 ≤ 0
    * The sum of the absolute value of each coefficients must be ≤ 1.
    * A sum of 1 corresponds to a TX output voltage swing of 1000 mVpp approximately.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_PHYTXEQ_COEFF`

.. code-block:: python

    await port.l1.serdes[0].medium.tx.ieee.set(pre3=, pre2=, pre=, main=, post=)

    resp = await port.l1.serdes[0].medium.tx.ieee.get()
    resp.pre3
    resp.pre2
    resp.pre
    resp.main
    resp.post

Nativ
------
Control and monitor the equalizer settings of the on-board PHY in the transmission direction (towards the transceiver cage).

* pre3 tap value. Default = 0 (neutral)
* pre2 tap value. Default = 0 (neutral)
* pre tap value. Default = 0 (neutral)
* main tap value.
* post tap value. Default = 0 (neutral)

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_PHYTXEQ`

.. code-block:: python

    await port.l1.serdes[0].medium.tx.native.set(pre3=, pre2=, pre=, main=, post=)

    resp = await port.l1.serdes[0].medium.tx.native.get()
    resp.pre3
    resp.pre2
    resp.pre
    resp.main
    resp.post