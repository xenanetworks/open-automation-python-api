.. _getting-started-label:

Getting Started
==================================

Installation
--------------------------------

Prerequisites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python
''''''''''''''''

XOA Python API requires that you `install Python <https://realpython.com/installing-python/>`_  on your system.

.. note:: 

    XOA Python API requires Python >= 3.8.

pip
''''''''''''''''

Make sure ``pip`` is installed on your system. ``pip`` is the `package installer for Python <https://packaging.python.org/guides/tool-recommendations/>`_ . You can use it to install packages from the `Python Package Index <https://pypi.org/>`_  and other indexes.

Usually, ``pip`` is automatically installed if you are:

* working in a `virtual Python environment <https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments>`_ (`virtualenv <https://virtualenv.pypa.io/en/latest/#>`_ or `venv <https://docs.python.org/3/library/venv.html>`_ ). It is not necessary to use ``sudo pip`` inside a virtual Python environment.
* using Python downloaded from `python.org <https://www.python.org/>`_ 

If you don't have ``pip`` installed, you can:

* Download the script, from https://bootstrap.pypa.io/get-pip.py.
* Open a terminal/command prompt, ``cd`` to the folder containing the ``get-pip.py`` file and run:

.. tab:: Windows

    .. code-block:: doscon
        :caption: Install pip in Windows environment.

        > py get-pip.py

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install pip in macOS/Linux environment.

        $ python3 get-pip.py

.. seealso::

    Read more details about this script in `pypa/get-pip <https://github.com/pypa/get-pip>`_.

    Read more about installation of ``pip`` in `pip installation <https://pip.pypa.io/en/stable/installation/>`_.


Installing from PyPi using pip
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``pip`` is the recommended installer for XOA Python API. The most common usage of ``pip`` is to install from the `Python Package Index <https://pypi.org/>`_ using `Requirement Specifiers <https://pip.pypa.io/en/stable/cli/pip_install/#requirement-specifiers>`_.

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Install XOA Python API in Windows environment from PyPi.

        > pip install xoa-driver            # latest version
        > pip install xoa-driver==1.0.3     # specific version
        > pip install xoa-driver>=1.0.3     # minimum version

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install XOA Python API in macOS/Linux environment from PyPi.

        $ pip install xoa-driver            # latest version
        $ pip install xoa-driver==1.0.3     # specific version
        $ pip install xoa-driver>=1.0.3     # minimum version


Upgrading from PyPi using pip
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To upgrade XOA Python API package from PyPI:

.. tab:: Windows
    :new-set:
    
    .. code-block:: doscon
        :caption: Upgrade XOA Python API in Windows environment from PyPi.

        > pip install xoa-driver --upgrade

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Upgrade XOA Python API in macOS/Linux environment from PyPi.

        $ pip install xoa-driver --upgrade


Installing Manually From Source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If for some reason you need to install XOA Python API manually from source, the steps are:

First, make sure Python packages `wheel <https://wheel.readthedocs.io/en/stable/>`_ and  `setuptools <https://setuptools.pypa.io/en/latest/index.html>`_ are installed on your system. Install ``wheel`` and ``setuptools`` using ``pip``:

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Install ``wheel`` and ``setuptools`` in Windows environment.

        > pip install wheel setuptools

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install ``wheel`` and ``setuptools`` in macOS/Linux environment.

        $ pip install wheel setuptools

Then, download the XOA Python API source distribution from `XOA Python API Releases <https://github.com/xenadevel/xena-open-automation-python-api/releases>`_. Unzip the archive and run the ``setup.py`` script to install the package:

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Install XOA Python API in Windows environment from source.

        [xoa_driver]> python setup.py install

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install XOA Python API in macOS/Linux environment from source.

        [xoa_driver]$ python3 setup.py install


If you want to distribute, you can build ``.whl`` file for distribution from the source:

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Build XOA Python API wheel in Windows environment for distribution.

        [xoa_driver]> python setup.py bdist_wheel

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Build XOA Python API wheel in macOS/Linux environment for distribution.

        [xoa_driver]$ python3 setup.py bdist_wheel


Uninstall using pip
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Uninstall XOA Python API in Windows environment.

        > pip uninstall xoa-driver

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Uninstall XOA Python API in macOS/Linux environment.

        $ pip uninstall xoa-driver

.. seealso::

    For more information, see the `pip uninstall <https://pip.pypa.io/en/stable/cli/pip_uninstall/#pip-uninstall>`_ reference.


Code Example
-------------------

The simple code example below demonstrates how to use XOA Python API to:

* Establish connection to a Valkyrie tester.
* Reserve a port.
* Create a stream on the port.
* Configure the stream.
* Start traffic.
* Collect statistics.
* Stop traffic

.. literalinclude:: /code_example/manage_tester.py
    :language: python
    :linenos:
