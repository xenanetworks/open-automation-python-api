Identification
=========================

Name
----------
The name of the chassis, as it appears at various places in the user interface.
The name is also used to distinguish the various chassis contained within a
testbed  and in files containing the configuration for an entire test case.

Corresponding CLI command: ``C_NAME``

.. code-block:: python

    # Name
    await tester.name.set(chassis_name="name")

    resp = await tester.name.get()
    resp.chassis_name

Password
----------
The password of the chassis, which must be provided when logging on to the chassis.

Corresponding CLI command: ``C_PASSWORD``

.. code-block:: python

    # Password
    await tester.password.set(password="xena")

    resp = await tester.password.get()
    resp.password

Description
-----------
The description of the chassis.

Corresponding CLI command: ``C_COMMENT``

.. code-block:: python

    # Description
    await tester.comment.set(comment="description")
    
    resp = await tester.comment.get()
    resp.comment

Model
-----------
Gets the specific model of this Xena chassis.

Corresponding CLI command: ``C_MODEL``

.. code-block:: python

    # Model
    resp = await tester.model.get()
    resp.model

Serial Number
-------------
Gets the unique serial number of this particular Xena chassis.

Corresponding CLI command: ``C_SERIALNO``

.. code-block:: python

    # Serial Number
    resp = await tester.serial_no.get()
    resp.serial_number

Firmware Version
-----------------
Gets the major version numbers for the chassis firmware and the Xena PCI
driver installed on the chassis.

Corresponding CLI command: ``C_VERSIONNO``

.. code-block:: python

    # Firmware Version
    resp = await tester.version_no.get()
    resp.chassis_major_version
    resp.pci_driver_version

    resp = await tester.version_no_minor.get()
    resp.chassis_minor_version
    resp.reserved_1
    resp.reserved_2

Build String
------------
Identify the hostname of the PC that builds the xenaserver. It uniquely
identifies the build of a xenaserver.

Corresponding CLI command: ``C_BUILDSTRING``

.. code-block:: python
    
    # Build String
    resp = await tester.build_string.get()
    resp.build_string