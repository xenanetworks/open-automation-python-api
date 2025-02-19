MACsec TX Secure Channel Configuration
======================================

Description
-----------

The description of the port’s TX SC.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_DESCR`

.. code-block:: python

    await txsc_obj.config.description.set(description="TX SC Description")

    resp = await txsc_obj.config.description.get()
    resp.description



SCI Mode
-----------

The mode of the port’s TX SCI in MACsec.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_SCI_MODE`

.. code-block:: python

    await txsc_obj.config.sci_mode.set(mode=enums.MACSecSCIMode.END_STATION)
    await txsc_obj.config.sci_mode.set(mode=enums.MACSecSCIMode.WITH_SCI)
    await txsc_obj.config.sci_mode.set(mode=enums.MACSecSCIMode.NO_SCI)

    resp = await txsc_obj.config.sci_mode.get()
    resp.mode


SCI Value
-----------

The SCI of the port’s TX SC.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_SCI`

.. code-block:: python

    await txsc_obj.config.sci.set(sci=Hex("0102030405060002"))
    
    resp = await txsc_obj.config.sci.get()
    resp.sci


Confidentiality Offset
-----------------------

The confidentiality offset of the port’s TX SC.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_CONF_OFFSET`

.. code-block:: python

    await txsc_obj.config.confidentiality_offset.set(offset=0)
    
    resp = await txsc_obj.config.confidentiality_offset.get()
    resp.offset


Cipher Suite
-----------------------

The cipher suite of the port’s TX SC.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_CIPHERSUITE`

.. code-block:: python

    await txsc_obj.config.cipher_suite.set(cipher_suite=enums.MACSecCipherSuite.GCM_AES_128)
    await txsc_obj.config.cipher_suite.set(cipher_suite=enums.MACSecCipherSuite.GCM_AES_256)
    await txsc_obj.config.cipher_suite.set(cipher_suite=enums.MACSecCipherSuite.GCM_AES_XPN_128)
    await txsc_obj.config.cipher_suite.set(cipher_suite=enums.MACSecCipherSuite.GCM_AES_XPN_256)

    resp = await txsc_obj.config.cipher_suite.get()
    resp.cipher_suite


Starting Packet Number
-----------------------

The starting PN number of the port’s TX SC uses.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_STARTING_PN`

.. code-block:: python

    await txsc_obj.config.starting_pn.set(start=1, mode=enums.MACSecStartingPNMode.CONTINUE)
    await txsc_obj.config.starting_pn.set(start=1, mode=enums.MACSecStartingPNMode.RESET)
    
    resp = await txsc_obj.config.starting_pn.get()
    resp.start
    resp.mode

.. 
    VLAN Mode
    -----------------------

    The VLAN mode of the port’s TX SC.

        * VLAN encrypted: The original MACsec header format encoded the 802.1Q tag as part of the encrypted payload, thus hiding it from the public Ethernet transport.

        * VLAN in clear text (WAN MACsec): With 802.1Q tag in the clear, the 802.1Q tag is encoded outside the 802.1AE encryption header, exposing the tag to the private and public Ethernet transport

    .. figure:: images/macsec_vlan_modes.png
        :align: center

    .. important::

        MACsec VLAN Mode only takes effect if the packet header has VLAN fields after MAC address fields. You can have multiple VLAN fields in the packet header definition, but it will be the outermost VLAN field that is either moved inside or outside the MACsec PDU based on the configuration of the command.  

    Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_VLAN_MODE`

    .. code-block:: python

        await txsc_obj.config.vlan_mode.set(mode=enums.MACSecVLANMode.ENCRYPTED)
        await txsc_obj.config.vlan_mode.set(mode=enums.MACSecVLANMode.CLEAR_TEXT)
        
        resp = await txsc_obj.config.vlan_mode.get()
        resp.mode


Rekey Mode
-----------------------

The rekey mode of the port’s TX SC defines when to switch to the next SAK.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_REKEY_MODE`

.. code-block:: python

    await txsc_obj.config.rekey_mode.set(mode=enums.MACSecRekeyMode.PN_EXHAUSTION)
    await txsc_obj.config.rekey_mode.set(mode=enums.MACSecRekeyMode.PACKET_CNT)
    
    resp = await txsc_obj.config.rekey_mode.get()
    resp.mode


Encryption Mode
-----------------------

The encryption mode of the port’s TX SC.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_ENCRYPT`

.. code-block:: python

    await txsc_obj.config.encryption_mode.set(mode=enums.MACSecEncryptionMode.ENCRYPT_INTEGRITY)
    await txsc_obj.config.encryption_mode.set(mode=enums.MACSecEncryptionMode.INTEGRITY_ONLY)
    
    resp = await txsc_obj.config.encryption_mode.get()
    resp.mode


SAK Key Value
-----------------------

Configure the value of a SAK key on the port’s TX SC.

The number and values of SAK keys depend on the cipher suite used.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_SAK_VALUE`

.. code-block:: python

    # For GCM_AES_128 and GCM_AES_128_XPN
    await txsc_obj.access_sak_value(0).set(sak_key_value=Hex("00010203040506070001020304050607"))
    await txsc_obj.access_sak_value(1).set(sak_key_value=Hex("00010203040506070001020304050607"))
    await txsc_obj.access_sak_value(2).set(sak_key_value=Hex("00010203040506070001020304050607"))
    await txsc_obj.access_sak_value(3).set(sak_key_value=Hex("00010203040506070001020304050607"))

    # For GCM_AES_256 and GCM_AES_256_XPN
    await txsc_obj.access_sak_value(0).set(sak_key_value=Hex("0001020304050607000102030405060700010203040506070001020304050607"))
    await txsc_obj.access_sak_value(1).set(sak_key_value=Hex("0001020304050607000102030405060700010203040506070001020304050607"))

XPN SSCI Value
--------------

The XPN SSCI of the port’s TX SC.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_XPN_SSCI`

.. code-block:: python

    await txsc_obj.config.xpn_ssci.set(sci=Hex("00000000"))
    
    resp = await txsc_obj.config.xpn_ssci.get()
    resp.ssci

XPN Salt Value
--------------

The XPN Salt of the port’s TX SC.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_XPN_SALT`

.. code-block:: python

    await txsc_obj.config.xpn_salt.set(sci=Hex("000000000000000000000000"))
    
    resp = await txsc_obj.config.xpn_salt.get()
    resp.salt