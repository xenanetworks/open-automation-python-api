![PyPI - Python Version](https://img.shields.io/pypi/pyversions/xoa-driver) [![PyPI](https://img.shields.io/pypi/v/xoa-driver)](https://pypi.python.org/pypi/xoa-driver) ![GitHub](https://img.shields.io/github/license/xenanetworks/open-automation-python-api) [![Documentation Status](https://readthedocs.org/projects/xena-openautomation-python-api/badge/?version=stable)](https://xena-openautomation-python-api.readthedocs.io/en/stable/?badge=stable)
# Xena OpenAutomation Python API
Xena OpenAutomation (XOA) Python API is a driver providing user-friendly communication interfaces to Xena's physical and virtual Traffic Generation and Analysis (TGA) testers. It provides a rich collection of programming interfaces that can be used to either write test scripts or develop applications.

## Introduction
Many of our customers choose to develop their own test scripts, where they automate performance verification, regression test, development verification, and so on.

At Xena Networks, we have always been providing customers with the best tool for test automation. To help our customers achieve a more efficient quality control and continuous development verification, we have developed a new platform Xena OpenAutomation, overlaying various Xena hardware and virtual testers, to offer not only automated test suites but also the power to build programs from simple scripts to advanced applications with endless possibilities.

The cornerstone component of Xena OpenAutomation is its Python API, which contains more than 600 commands, from basic streams creation to advance eye diagrams measurement. With this rich collection of programming interfaces, we empower our customers to either write test scripts or develop applications with almost limitless possibilities.

Moving forward, all Xena’s automated test suites will be based on Xena OpenAutomation.

## Documentation
The user documentation is hosted:
[Xena OpenAutomation Python API Documentation](https://docs.xenanetworks.com/projects/xoa-python-api)

## Key Features
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


## Quick Start

* Get Python pip if not already installed (Download https://bootstrap.pypa.io/get-pip.py):
    `python get-pip.py`

* Install the latest xoa-driver:
    `pip install xoa-driver -U`

* Write Python code to manage with Xena testers:
    ```python
    import asyncio

    from xoa_driver import testers
    from xoa_driver import modules
    from xoa_driver import ports
    from xoa_driver import enums
    from xoa_driver import utils

    async def my_awesome_func():
        # Establish connection with a Valkyrie tester
        async with testers.L23Tester("10.10.10.10", "JonDoe") as tester:
            # Get the port 0/0 (module 0)
            port = await tester.modules.obtain(0).ports.obtain(0)

            # Reserve the port
            await port.reservation.set_reserve()

            # Reset the port
            await port.reset.set()

            # Create a stream on the port
            stream = await port.streams.create()

            # Prepare stream header protocol
            header_protocol = [enums.ProtocolOption.ETHERNET, enums.ProtocolOption.IP]

            # Batch configure the stream
            await utils.apply(
                stream.tpld_id.set(0), # Create the TPLD index of stream
                stream.packet.length.set(*size), # Configure the packet size
                stream.packet.header.protocol.set(header_protocol), # Configure the packet type
                stream.packet.header.data.set(header), # Configure the packet header
                stream.enable.set_on(), # Enable streams
                stream.rate.fraction.set(1000000) # Configure the stream rate 100%
            )

            # Clear statistics
            await utils.apply(
                port.statistics.tx.clear.set(),
                port.statistics.rx.clear.set()
            )

            # Start traffic on the port
            await port.traffic.state.set_start()

            # Test duration 10 seconds
            await asyncio.sleep(10)

            # Query TX statistics
            tx_result = await port.statistics.tx.total.get()
            print(f"bit count last second: {tx_result.bit_count_last_sec}")
            print(f"packet count last second: {tx_result.packet_count_last_sec}")
            print(f"byte count since cleared: {tx_result.byte_count_since_cleared}")
            print(f"packet count since cleared: {tx_result.packet_count_since_cleared}")

            # Stop traffic on the port
            await port.traffic.state.set_stop()

            # Release the port
            await port.reservation.set_release()

    def main():
        try:
            loop = asyncio.get_event_loop()
            loop.create_task(my_awesome_func())
            loop.run_forever()
        except KeyboardInterrupt:
            pass

    if __name__ == "__main__":
        main()
    ```


***

FOR TESTING BEYOND THE STANDARD.
