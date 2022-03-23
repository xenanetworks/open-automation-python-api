Installation
===================

Install Using pip
----------------------

Make sure Python ``pip`` is installed on you system. If you are using virtualenv, then pip is already installed into environments created by virtualenv, and using sudo is not needed. If you do not have pip installed, download this file: https://bootstrap.pypa.io/get-pip.py and run ``python get-pip.py``.

To install the latest, use pip to install from pypi:

.. code-block:: shell
    
    ~/> pip install xoa-driver


To upgrade to the latest, use pip to upgrade from pypi:

.. code-block:: shell
    
    ~/> pip install xoa-driver --upgrade


Install From Source
----------------------------

Make sure packages ``wheel``, ``setuptools`` are installed  on your system.

Install ``wheel`` and ``setuptools`` using pip:

.. code-block:: shell
    
    ~/> pip install wheel setuptools


Download the source distribution first. Unzip the zip archive and run the ``setup.py`` script to install the package:

.. code-block:: shell
    
    /xoa_driver> python setup.py install


Then you can build ``.whl`` file for distribution:

.. code-block:: shell
    
    /xoa_driver> python setup.py bdist_wheel
