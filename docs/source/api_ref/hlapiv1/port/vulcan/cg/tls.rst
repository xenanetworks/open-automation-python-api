TLS
=========================

.. note::

    Applicable to Vulcan port only.

Enable
--------------



.. code-block:: python

    await cg.tls.enable.set_yes()
    await cg.tls.enable.set_no()
    await cg.tls.enable.get()


Cipher Suites
--------------



.. code-block:: python

    await cg.tls.cipher_suites.set()
    await cg.tls.cipher_suites.get()


Close Notify
--------------



.. code-block:: python

    await cg.tls.close_notify.set_yes()
    await cg.tls.close_notify.set_no()
    await cg.tls.close_notify.get()


Certificate and Key
--------------------



.. code-block:: python

    await cg.tls.file.certificate_path.set()
    await cg.tls.file.dhparams_path.set()
    await cg.tls.file.private_key_path.set()


Max Record Size
----------------



.. code-block:: python

    await cg.tls.max_record_size.set()
    await cg.tls.max_record_size.get()


Protocol Version
----------------



.. code-block:: python

    await cg.tls.protocol.version.set_sslv3()
    await cg.tls.protocol.version.set_tls10()
    await cg.tls.protocol.version.set_tls11()
    await cg.tls.protocol.version.set_tls12()
    await cg.tls.protocol.version.get()


Minimum Required Version
------------------------



.. code-block:: python

    await cg.tls.protocol.min_required_version.get()


Server Name
------------------------



.. code-block:: python

    await cg.tls.server_name.set()
    await cg.tls.server_name.get()