MACsec RX Secure Channel Configuration
======================================

Description
-----------

The description of the port’s RX SC.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_RXSC_DESCR`

.. code-block:: python

    await rxsc_obj.config.description.set(description="RX SC Description")

    resp = await rxsc_obj.config.description.get()
    resp.description



SCI Value
-----------

The SCI of the port’s RX SC.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_RXSC_SCI`

.. code-block:: python

    await rxsc_obj.config.sci.set(sci=Hex("0102030405060001"))
    
    resp = await rxsc_obj.config.sci.get()
    resp.sci


Confidentiality Offset
-----------------------

The confidentiality offset of the port’s RX SC.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_RXSC_CONF_OFFSET`

.. code-block:: python

    await rxsc_obj.config.confidentiality_offset.set(offset=5)
    
    resp = await rxsc_obj.config.confidentiality_offset.get()
    resp.offset


Cipher Suite
-----------------------

The cipher suite of the port’s RX SC.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_RXSC_CIPHERSUITE`

.. code-block:: python

    await rxsc_obj.config.cipher_suite.set(cipher_suite=enums.MACSecCipherSuite.GCM_AES_128)
    await rxsc_obj.config.cipher_suite.set(cipher_suite=enums.MACSecCipherSuite.GCM_AES_256)
    await rxsc_obj.config.cipher_suite.set(cipher_suite=enums.MACSecCipherSuite.GCM_AES_XPN_128)
    await rxsc_obj.config.cipher_suite.set(cipher_suite=enums.MACSecCipherSuite.GCM_AES_XPN_256)

    resp = await rxsc_obj.config.cipher_suite.get()
    resp.cipher_suite


Test Payload ID
-----------------------

Associate a TPLD ID with the RX SC.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_RXSC_TPLDID`

.. code-block:: python

    await rxsc_obj.config.tpld_id.set(tpld_id=0)
    
    resp = await rxsc_obj.config.tpld_id.get()
    resp.tpld_id



SAK Key Value
-----------------------

Configure the value of a SAK key on the port’s RX SC.

The number and values of SAK keys depend on the cipher suite used.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_RXSC_SAK_VALUE`

.. code-block:: python

    # For GCM_AES_128 and GCM_AES_128_XPN
    await rxsc_obj.access_sak_value(0).set(sak_key_value=Hex("00010203040506070001020304050607"))
    await rxsc_obj.access_sak_value(1).set(sak_key_value=Hex("00010203040506070001020304050607"))
    await rxsc_obj.access_sak_value(2).set(sak_key_value=Hex("00010203040506070001020304050607"))
    await rxsc_obj.access_sak_value(3).set(sak_key_value=Hex("00010203040506070001020304050607"))

    # For GCM_AES_256 and GCM_AES_256_XPN
    await rxsc_obj.access_sak_value(0).set(sak_key_value=Hex("0001020304050607000102030405060700010203040506070001020304050607"))
    await rxsc_obj.access_sak_value(1).set(sak_key_value=Hex("0001020304050607000102030405060700010203040506070001020304050607"))