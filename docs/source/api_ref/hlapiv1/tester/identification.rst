Identification
=========================

Name
----------

.. code-block:: python

    await tester.name.set(chassis_name="name")
    await tester.name.get()

Password
----------

.. code-block:: python

    await tester.password.set(password="xena")
    await tester.password.get()

Description
-----------

.. code-block:: python

    await tester.comment.set(comment="description")
    await tester.comment.get()

Model
-----------

.. code-block:: python

    await tester.model.get()

Serial Number
-------------

.. code-block:: python

    await tester.serial_no.get()

Firmeware Version
-----------------

.. code-block:: python

    await tester.version_no.get()
    await tester.version_no_minor.get()

Build String
------------

.. code-block:: python
    
    await tester.build_string.get()