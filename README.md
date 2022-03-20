# Xena OpenAutomation Python API
Xena OpenAutomation (XOA) Python API is a driver providing user-friendly communication interfaces to Xena's physical and virtual Traffic Generation and Analysis (TGA) testers. It provides a rich collection of programming interfaces that can be used to either write test scripts or develop applications.

## Introduction
Many of our customers choose to develop their own test scripts, where they automate performance verification, regression test, development verification, and so on.

At Xena Networks, we have always been providing customers with the best tool for test automation. To help our customers achieve a more efficient quality control and continuous development verification, we have developed a new platform Xena OpenAutomation, overlaying various Xena hardware and virtual testers, to offer not only automated test suites but also the power to build programs from simple scripts to advanced applications with endless possibilities.

The cornerstone component of Xena OpenAutomation is its Python API, which contains more than 600 commands, from basic streams creation to advance eye diagrams measurement. With this rich collection of programming interfaces, we empower our customers to either write test scripts or develop applications with almost limitless possibilities.

Moving forward, all Xena’s automated test suites will be based on Xena OpenAutomation.

## Key Benefits
* Objected-oriented, high-level abstraction, to help users save time on parsing command responses.
* Supporting sending commands in batches to increase code execution efficiency.
* Automatically matching command requests and server response, providing clear information in case a command gets an error response.
* Supporting server-to-client push notification, and event subscription, to reduce user code complexity.
* Covering commands of Xena testers, including Xena Valkyrie, Vulcan, and Chimera.
* Supporting IDE auto-complete with built-in class/function/API use manual, to increase development efficiency.

## Installation

### Install Using `pip`
Make sure Python `pip` is installed on you system. If you are using virtualenv, then pip is already installed into environments created by virtualenv, and using sudo is not needed. If you do not have pip installed, download this file: https://bootstrap.pypa.io/get-pip.py and run `python get-pip.py`.

To install the latest, use pip to install from pypi:
``` shell
~/> pip install xoa-driver
```

To upgrade to the latest, use pip to upgrade from pypi:
``` shell
~/> pip install xoa-driver --upgrade
```

### Install From Source Code
Make sure these packages are installed ``wheel``, ``setuptools`` on your system.

Install ``setuptools`` using pip:
``` shell
~/> pip install wheel setuptools
```

To install source of python packages:
``` shell
/xoa_driver> python setup.py install
```

To build ``.whl`` file for distribution:
``` shell
/xoa_driver> python setup.py bdist_wheel
```

## Documentation
The user documentation is hosted:
https://xena-openautomation-python-api.readthedocs.io/en/latest/


***

Uɴɪғɪᴇᴅ. Oᴘᴇɴ. Iɴᴛᴇɢʀᴀᴛɪᴏɴ.