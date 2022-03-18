# Xena OpenAutomation Python API
Xena OpenAutomation (XOA) Python API is a driver providing user-friendly communication interfaces to Xena's physical and virtual Traffic Generation and Analysis (TGA) testers. It provides a rich collection of programming interfaces that can be used to either write test scripts or develop applications.

## Table of Content
* [Xena OpenAutomation Python API](#xena-openautomation-python-api)
  * [Table of Content](#table-of-content)
  * [Introduction](#introduction)
  * [Key Benefits](#key-benefits)
  * [Installation](#installation)
    * [From Source Code](#from-source-code)
    * [From Python Package Installer](#from-python-package-installer)
  * [API Structure](#api-structure)
  * [Test Resource Structure and Management Rules](#test-resource-structure-and-management-rules)
    * [L23 Valkyrie Tester (Physical)](#l23-valkyrie-tester-physical)
    * [L47 Vulcan Tester (Physical and Virtual)](#l47-vulcan-tester-physical-and-virtual)
    * [Network Impairment Chimera Emulator (Physical)](#network-impairment-chimera-emulator-physical)
    * [Rules for Test Resource Management](#rules-for-test-resource-management)
  * [Commands Grouping](#commands-grouping)
    * [Parallel Grouping](#parallel-grouping)
    * [Sequential Grouping](#sequential-grouping)
    * [Sending Command One by One](#sending-command-one-by-one)
  * [High-Level API User Guide](#high-level-api-user-guide)
    * [Code API Notation and Namings](#code-api-notation-and-namings)
    * [Attributes and Methods](#attributes-and-methods)
    * [Event Subscription and Push Notification](#event-subscription-and-push-notification)
      * [Under the tester level](#under-the-tester-level)
      * [Under the Module level](#under-the-module-level)
      * [Under the Port level](#under-the-port-level)
    * [Resource Managers](#resource-managers)
      * [Module and Port Managers](#module-and-port-managers)
      * [Index Manager](#index-manager)
    * [Session](#session)
      * [Session Identification](#session-identification)
      * [Session Recovery and Resource Reallocation](#session-recovery-and-resource-reallocation)
      * [Handling Multiple Same-Username Sessions](#handling-multiple-same-username-sessions)
    * [Local State](#local-state)
    * [High-Level Code Examples](#high-level-code-examples)
      * [Tester Instance](#tester-instance)
        * [Creating a tester instance from one of the available tester types](#creating-a-tester-instance-from-one-of-the-available-tester-types)
        * [Create a tester instance by using context manager](#create-a-tester-instance-by-using-context-manager)
        * [Create multiple tester instances](#create-multiple-tester-instances)
      * [Obtain Resources](#obtain-resources)
        * [Obtain one module](#obtain-one-module)
        * [Obtain multiple modules](#obtain-multiple-modules)
        * [Process operation on all modules](#process-operation-on-all-modules)
      * [Obtain multiple ports](#obtain-multiple-ports)
      * [Data Exchange](#data-exchange)
        * [Querying parameters](#querying-parameters)
        * [Setting parameters](#setting-parameters)
      * [Statistics Collection](#statistics-collection)
  * [Coding Differences between XOA Python HL-API and CLI](#coding-differences-between-xoa-python-hl-api-and-cli)
    * [CLI Code Example](#cli-code-example)
    * [XOA Python API Example](#xoa-python-api-example)
  * [Low-Level API User Guide](#low-level-api-user-guide)


## Introduction
Recently, we have observed that many of our customers choose to develop their own test scripts, where they automate performance verification, regression test, development verification, and so on.

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
### From Source Code
Make sure these packages are installed: ``wheel``, ``setuptools``
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

### From Python Package Installer
``` shell
~/> pip install xoa-driver
```

## API Structure
XOA Python API consists of two layers on top of the tester proprietary binary commands, as shown in the diagram below.

The High-Level API layer provides abstraction that helps the developer to quickly develop scripts or program in an object-oriented fashion and explicit defenition of commads which applicable or not by different `tester`, `module`, `port` types. In addition it's handling: `Auto Keep alive queryes`, `resources Identification tracking for Push notification` and other helping methods.  
For example, to change the description of a tester, the high-level API is:
```python
await tester.comment.set(comment="my tester")
```

The Low-Level API Layer gives the developer the complete direct control of the tester since the name of the API is the same as what is defined in the CLI. But it will require more work around for: `keep connection alive`, `manage indices of <modules>, <ports>, <streams>, etc.`

For example, to change the description of a tester by, the low-level API is:
```python
await C_COMMENT(handler).set(comment="my tester")
```

```
+---------------------------------+
|           High-Level API        |
+---------------------------------+
+---------------------------------+
|           Low-Level API         |
+---------------------------------+
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx       
+---------------------------------+
|    Binary Xena Management       |
|      Protocol (proprietary)     |
+---------------------------------+
+---------------------------------+
|    Xena Physical and Virtual    |
|            Testers              |
+---------------------------------+
```


## Test Resource Structure and Management Rules
### L23 Valkyrie Tester (Physical)
Valkyrie Tester (physical) has the following hierarchical structure.

Valkyrie Tester, Valkyrie Module, and Valkyrie Port are physical resources that correspond to the physical configuration. They cannot be created or deleted.

Everything below Valkyrie Port is virtual resources that can be created, deleted, and configured as needed.
```
---------------------
|  Valkyrie Tester  |
---------------------
    |
    |   -----------------------
    |---|   Valkyrie Module   |
    |   -----------------------
    |        |
    |        |    ------------------- 
    |        |----|  Valkyrie Port  | 
    |        |    ------------------- 
    |        |        |
    |        |        |    ************************* 
    |        |        |----|  Port Statistics      | 
    |        |        |    ************************* 
    |        |        |    ************************* 
    |        |        |----|  Stream               | 
    |        |        |    ************************* 
    |        |        |        |
    |        |        |        |    **********************  
    |        |        |        |----|  Filter            | 
    |        |        |        |    **********************  
    |        |        |        |    **********************  
    |        |        |        |----|  Modifier          | 
    |        |        |        |    ********************** 
    |        |        |        |    **********************  
    |        |        |        |----|  Histogram         | 
    |        |        |        |    ********************** 
    |        |        |        |    ********************** 
    |        |        |        |----|  Length Term       | 
    |        |        |        |    ********************** 
    |        |        |        |    ********************** 
    |        |        |        |----|  Match Term        | 
    |        |        |        |    ********************** 
    |        |        |        |    ********************** 
    |        |        |        |----|  Test Payload      | 
    |        |        |        |    ********************** 
    |        |        |        |    ********************** 
    |        |        |        |----|  Stream Statistics | 
    |        |        |        |    ********************** 
```

### L47 Vulcan Tester (Physical and Virtual)
Vulcan Tester (physical) has the following hierarchical structure.

Vulcan Tester, Vulcan Module, and Vulcan Port are physical resources that correspond to the physical configuration. They cannot be created or deleted.

Everything below Vulcan Port is virtual resources that can be created, deleted, and configured as needed.
```
------------------
|  Vulcan Tester |
------------------
    |
    |   -------------------
    |---|  Vulcan Module  |
    |   -------------------
    |        |
    |        |    ------------------ 
    |        |----|  Vulcan Port   | 
    |        |    ------------------ 
    |        |        |
    |        |        |    ************************ 
    |        |        |----|  Port Statistics     | 
    |        |        |    ************************
    |        |        |    ************************ 
    |        |        |----|  Connection Group    | 
    |        |        |    ************************
```
```
-------------------
|  Vulcan VE Tester  |
-------------------
    |
    |   ----------------------
    |---|  Vulcan VE Module  |
    |   ----------------------
    |        |
    |        |    -------------------- 
    |        |----|  Vulcan VE Port  | 
    |        |    -------------------- 
    |        |        |
    |        |        |    ************************ 
    |        |        |----|  Port Statistics     | 
    |        |        |    ************************ 
    |        |        |    ************************ 
    |        |        |----|  Connection Group    | 
    |        |        |    ************************
```

### Network Impairment Chimera Emulator (Physical)
Chimera Emulator (physical) has the following hierarchical structure.

Chimera Emulator, Chimera Module, and Chimera Port are physical resources that correspond to the physical configuration. They cannot be created or deleted.

Everything below Chimera Port is virtual resources that can be created, deleted, and configured as needed.
```
------------------------
|  Chimera Emulator    |
------------------------
    |
    |   ----------------------
    |---|  Chimera Module    |
    |   ----------------------
    |        |
    |        |    ----------------------
    |        |----|  Chimera Port      | 
    |        |    ----------------------
    |        |        |
    |        |        |    ************************* 
    |        |        |----|  Port Statistics      | 
    |        |        |    ************************* 
    |        |        |    *************************
    |        |        |----|  Flow                 | 
    |        |        |    *************************
    |        |        |        |
    |        |        |        |    ****************************
    |        |        |        |----|  Filter                  | 
    |        |        |        |    ****************************
    |        |        |        |    ****************************
    |        |        |        |----|  Impairment Config       | 
    |        |        |        |    ****************************
    |        |        |        |    ****************************
    |        |        |        |----|  Impairment Distribution | 
    |        |        |        |    ****************************
    |        |        |        |    ****************************
    |        |        |        |----|  Flow Statistics         | 
    |        |        |        |    ****************************
```

### Rules for Test Resource Management
1. To do `set` on a test resource, i.e. `Tester`, `Module`, or `Port`, you must reserve the resource under your username.
2. To do `get` on a test resource or configuration, you don't need to reserve.
3. To reserve a tester, you must make sure all the modules and ports are either released or under your ownership.
4. To reserve a module, you must make sure all the ports are either released or under your ownership.

## Commands Grouping
Sending commands one by one using CLI is extremely slow in terms of execution speed. This is because the program needs to wait for the response from the tester. More, using CLI it is difficult to group commands together and send them in one round.

XOA Python API provides two ways to group commands together to send to testers, which greatly increase commands execution speed. This is very useful, when the developer has many ports and many streams to configure, as well as querying the port and stream statistics as quickly as possible.

### Parallel Grouping
```python
await asyncio.gather(
    command_1,
    command_2,
    command_3,
    ...
)
```
`asyncio.gather` groups commands in a parallel way. Commands are sent out in parallel (with neglectable delay between each other). This is very useful when you want to send commands to different test resources, e.g. two different ports on the same tester, or two different ports on different testers.

### Sequential Grouping
```python
await utils.apply(
    command_1,
    command_2,
    command_3,
    ...
)
```
`utils.apply` groups commands in a sequential way. Commands are sent out in one large batch to the tester. This is very useful when you want to send many commands to the same test resource, e.g. a port on a tester.

However, abusing this function can cause memory issue on your computer. This is because the computer needs to store all the grouped commands in the memory until the responses from the testers arrive.

Thus, we have set a limit to the number of ``200`` commands that you can group sequentially.

``` python
commands = [
    command_1,
    command_2,
    command_3,
    ...
]
async for response in utils.apply_iter(*commands):
    print(response)
```

`utils.apply_iter` do exactly the same thing as `utils.apply` just its not aggrigate responses and return them one by one as soon as it's ready. This allows us to send batches of the bigger commands number without big memory use.

### Sending Command One by One
If you prefer sending commands in the old fashion like using CLI, you can certainly have only one command in the grouping, for example:
``` python
await command_1
await command_2
await command_3
```

> **IMPORTANT**: Remember to use `await` before the command. This is because all command classes support `asyncio` and if you want your code to be non-blocking, then use `await`. If a previous command is not responded due to network problem, the next command can still be sent (non-blocking). Otherwise, the next command will wait for the previous command to finish, which usually end up timing out and all the rest commands are not sent.

Read more about Python [`awaitable object`](https://docs.python.org/3/library/asyncio-task.html#id2).


## High-Level API User Guide
### Code API Notation and Namings
High-level API aims to be semantic in function name patterns to avoid expectation conflicts, as well as avoiding methods which can return values of a different kind. The key rule is: **One Method One Action**:

> **IMPORTANT**: If there is a method that returns a single item or a collection of items, it is considered a BUG.

`<resource>` - representing `Tester` | `Module` | `Port` | `<indices>` | `<namespace_class>`

`<indices>` - representing `Streams` | `Connection Groups` indices etc.

`<namespace_class>` - a group of commands that manage the resources of the same kind but still stays at the same level as others

`<command_oo_name>` - the name of the command modified to adapt to the object-oriented concept. Commands of the same access level, which access or modify parameters of the same kind, are grouped under one `<namespace_class>` as shown in the example below:
```
 P_SPEEDSELECTION
 P_SPEEDS_SUPPORTED
```
are represented as
```
 <resource>.speed.selection
 <resource>.speed.supported
 ```

### Attributes and Methods
There are only two types of methods for each command, `get` and/or `set`. `get` is used to query values, status, configuration of the command. `set` is the change.

To use `get` and `set` methods, you need to use `await` because they are all made asynchronous. Read more about Python [`awaitable object`](https://docs.python.org/3/library/asyncio-task.html#id2).

`await <resource>.<command_oo_name>.get()`

`await <resource>.<command_oo_name>.set(<values>)`

`await <resource>.<command_oo_name>.set_<variation__name>()`

`await <resource>.<command_oo_name>.set_<variation__name>(<extra_value>)`

### Event Subscription and Push Notification
Structure: `<resource>.on_<command_oo_name>_change(<async_callback_function>)`

The `<async_callback_function>` must be an [`coroutine`](https://docs.python.org/3/library/asyncio-task.html#id1) function. Parameters, which can be passed to `<async_callback_function>`, depend on what resource it is affiliated. Examples are shown below:
#### Under the tester level
    `<ref_tester>, <new_value>`

#### Under the Module level
    `<ref_module>, <new_value>`

#### Under the Port level
    `<ref_port>, <new_value>`

**Exception from the rule is only for the event ``on_disconnected`` the parameters which will pass to it will be ``tuple(<tester_ip: str>, <tester_port: int>)``**

> **IMPORTANT**: A subscription to an event only provides a tool for notifying the external code. It is unnecessary to update the library instance state manually, because it is automatically handled by the library code.

> **IMPORTANT**: It is allowed to subscribe multiple callback functions to one event.

### Resource Managers
Most of the sublevel resources, which are organized into collections, are handled by resource managers.

The most commonly used resource managers are `Module Manager` | `Port Manager` | `Index Manager`
> **IMPORTANT**: Each resource manager is an [`iterable object`](https://wiki.python.org/moin/Iterator)

An illustration of the the resource managers and test resources are shown below:

```
------------
|  Tester  |
------------
    |
*******************
|  module manager |
*******************
    |
    |   --------------
    |---|  Module 0  |
    |   --------------
    |        |
    |    *******************
    |    |   port manager  |
    |    *******************
    |        |
    |        |    --------------   *****************
    |        |----|  Port 0    | - | index manager |
    |        |    --------------   *****************
    |        |    --------------   *****************
    |        |----|  Port 1    | - | index manager |
    |        |    --------------   *****************
    |        |    --------------   *****************
    |        |----|  Port N-1  | - | index manager |
    |             --------------   *****************
    |
    |   --------------
    |---|  Module 1  |
    |   --------------
    |        |
    |    *******************
    |    |   port manager  |
    |    *******************
    |        |
    |        |    --------------   *****************
    |        |----|  Port 0    | - | index manager |
    |        |    --------------   *****************
    |        |    --------------   *****************
    |        |----|  Port 1    | - | index manager |
    |        |    --------------   *****************
    |        |    --------------   *****************
    |        |----|  Port N-1  | - | index manager |
    |             --------------   *****************
    |
    |   --------------
    |---| Module N-1 |
        --------------
```

#### Module and Port Managers
Each tester contains a  `Module Manager`, which can be accessed through attribute `modules`. Each module contains a `Port Manager`.

> **IMPORTANT**: a `Module Manager` can contain modules of different **Module Types**. This is because there can be various test modules installed in a physical tester. On the other hand, a `Port Manager` contains ports of the same **Port Type**. This is because the ports on a module are of the same type.

Methods to retrieve a module or a port from a resource manager:
`obtain(<module_slot_number> | <port_index>)`.

Code example:
```python
### Obtaining one module

# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_test_module = tester.modules.obtain(0) # get reference to instance of module under slot 0
    if not isinstance(my_test_module, modules.ModuleChimera): # check if module is of types which we are suspecting
        print(module.info.media_info_list)
    # other code ...
```

Methods to retrieve _multiple_ resources from a resource manager:
`obtain_multiple(<module_index> | <port_index>, ...)`

Code example:
```python
### Obtain multiple modules

# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_test_modules = tester.modules.obtain_multiple(0, 2) # get reference to instance of module under slot 0
    for module in my_test_modules:
        if not isinstance(module, modules.ModuleChimera): # check if module is of types which we are suspecting
            print(module.info.media_info_list)
    # other code ...
```


#### Index Manager
`Index Manager` manages the sub-port-level resource indices such as stream indices, filter indices, connection group indices, etc. It automatically ensures correct and conflict-free index assignment.

> **IMPORTANT**: It is the user's responsibility to create, retrieve, and remove those sub-port-level indices.

Thanks to the index manager of a port, users don't necessarily need to handle the index assignment.

To create an index, use method `create()`.
To remove an index, use method `remove()`. An index also can be removed without accessing the manager but by calling `<index_instance>.delete()`.

The call of the function `<index_instance>.delete()` will remove a resource index from the port, and will automatically notify the index manager of the port about the removal. The index manager will make sure the freed index is used when the user creates again next time.

### Session
A `session` will be created automatically after a TCP connection is established between the client and the tester.

Three attributes of a `session` are exposed:
- `is_online` - property to validate if the TCP connection is alive.
- `logoff()` - async method for gracefully closing the TCP connection to the tester.
- `sessions_info()` - async method for getting information of the current active sessions on a tester.

#### Session Identification
* A tester does not use the tuple (source IP, source port, destination IP, destination port) to identify a session. Instead, it uses the username as the identification of a session. For instance, `tester = await testers.L23Tester("192.168.1.200", "JonDoe")`, where the username is `JonDoe`.

#### Session Recovery and Resource Reallocation
* To recover the session, the client only needs to establish a new TCP connection with the same username as the dropped session.
* All resources of the broken session will be automatically transferred to the new session because they have the same username.

#### Handling Multiple Same-Username Sessions
* If multiple sessions use the same username to connect to a tester after a broken session, the tester will give the control of the resources to a session in a first-come-first-served manner, and the others will be treated as observers. Thus, duplicated username should be avoided at the session level.
* If the controlling session is disconnected, the tester will automatically pass the control of the resources to the next session in the queue.

### Local State
The access to the local state of a resource is done through property `<resource>.info`. The info contains current status of the resource and information of its attributes, which cannot be changed during a running `session`.


### High-Level Code Examples

The boilerplate code that is used to run all of the examples.

```python
import asyncio
async def my_awesome_script():
    # my code goes here...

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_script())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
```

#### Tester Instance

Each tester class is represented as an [awaitable object](https://docs.python.org/3/library/asyncio-task.html#id2). When awaited, it establishes a TCP connection to the tester.

A tester instance also can be created without awaiting the connection establishment for more flexible manipulation of instances in user code.

##### Creating a tester instance from one of the available tester types
Available tester types are  `L23Tester` | `L47Tester` | `L47VeTester`
```python
# import available testers
from xoa_driver import testers

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection using username "JonDoe".

    # other code ...

    await tester.session.logoff() # gracefully close connection
```

##### Create a tester instance by using context manager
```python
# import available testers
from xoa_driver import testers

async def my_awesome_script():
    async with testers.L23Tester("192.168.1.200", "JonDoe") as tester: # create tester instance and establish connection
        print(tester.session.is_online)
        # other code ...
        # when leaving this block, the TCP connection will be closed.
```

##### Create multiple tester instances
```python
import typing
# import available testers
from xoa_driver import testers

def create_testers(hosts: typing.List[str], username: str) -> typing.List["testers.GenericAnyTester"]:
    return [ testers.L23Tester(host, username) for host in hosts ]


async def my_awesome_script():
    known_hosts = [
        "192.168.1.195",
        "192.168.1.196",
        "192.168.1.197",
        "192.168.1.198",
        "192.168.1.199",
        "192.168.1.200",
    ]
    testers_pool = create_testers( known_hosts, "JonDoe")
    # now we can do ``await testers_pool[0]`` which establishes the connection

    await asyncio.gather(*testers_pool) # we also can use asyncio.gather for await all testers at once in concurrent mode
    print(testers_pool[0].session.is_online)
    # other code ...
```
Read more about [`await asyncio.gather`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather).


#### Obtain Resources
##### Obtain one module
```python
# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_test_module = tester.modules.obtain(0) # get reference to instance of module under slot 0
    if not isinstance(my_test_module, modules.ModuleChimera): # check if module is of types which we are suspecting
        print(module.info.media_info_list)
    # other code ...
```

##### Obtain multiple modules
```python
# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_test_modules = tester.modules.obtain_multiple(0, 2) # get reference to instance of module under slot 0
    for module in my_test_modules:
        if not isinstance(module, modules.ModuleChimera): # check if module is of types which we are suspecting
            print(module.info.media_info_list)
    # other code ...
```

##### Process operation on all modules
```python
# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    for module in tester.modules:
        if not isinstance(my_test_module, modules.ModuleChimera): # check if module is of types which we are suspecting
            print(module.info.media_info_list)
        else:
            print("Is chimera module")
    # other code ...
```

#### Obtain multiple ports
The interface of obtaining multiple ports is equivalent to obtaining multiple modules with the following exceptions:
- **all ports are of the same type**
- **all ports are aligned from index 0 to `max_port_count-1`**

```python
# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_test_module = tester.modules.obtain(0)
    ( tx_port, rx_port ) = resources = my_test_module.ports.obtain_multiple(0, 1)
    # other code ...
```

#### Data Exchange
##### Querying parameters

> **IMPORTANT**: resource reservation is not required to query information from the tester.


```python
# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_test_module = tester.modules.obtain(0)
    if isinstance(my_test_module, modules.ModuleChimera):
        return None # commands which used in this example are not supported by Chimera Module
    ( tx_port, rx_port ) = resources = my_test_module.ports.obtain_multiple(0, 1)
    for port in resources:
        print(await port.speed.supported.get()) # Querying port supported speeds
    # other code ...
```

##### Setting parameters

> **IMPORTANT**: reservation is required to set parameter to: `Tester` | `Module` | `Port`.

```python
# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_test_module = tester.modules.obtain(0)
    if isinstance(my_test_module, modules.ModuleChimera):
        return None # commands which used in this example are not supported by Chimera Module
    ( tx_port, rx_port ) = resources = my_test_module.ports.obtain_multiple(0, 1)
    for port in resources:
        if port.is_reserved_by_me(): # check if we can set parameters to selected port
            continue
        if not port.is_released():
            await port.reservation.set_relinquish() # send relinquish the port
        await port.reservation.set_reserve() # set reservation , means port will be controlled by our session
    await tx_port.comment.set("My Tx port") # set an comment to the Tx port
    await rx_port.comment.set("My Rx port") # set an comment to the Rx port
    # other code ...
```

#### Statistics Collection
Statistics collection, such as latency and jitter, TX/RX rate, frame count, etc., can be done by Python standard library `asyncio`. In case you are new to `asyncio`, the example below may help you understand how to use `asyncio` to query counters.
```python
import asyncio

async def background_task(tx_port: "ports.GenericL23Port", rx_port: "ports.GenericL23Port"):
   while True:
       print(await tx_port.statistics.tx.total.get())
       print(await rx_port.statistics.rx.total.get())
       await async.sleep(1)

async def my_awesome_script():
    # my code ...
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_test_module = tester.modules.obtain(0)
    if isinstance(my_test_module, modules.ModuleChimera):
        return None # commands which used in this example are not supported by Chimera Module
    ( tx_port, rx_port ) = resources = my_test_module.ports.obtain_multiple(0, 1)
    
    asyncio.create_task(background_task(tx_port, rx_port)) # put function to work in the background
    print("Task working in background")

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_script())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

```

## Coding Differences between XOA Python HL-API and CLI

If you are already very familiar with Xena CLI, the code comparison below will help you understand the coding differences between a XOA Python script and a Xena CLI script, which are doing the same thing.

- The CLI Script consists of two files: `cli_script.py` and `config.txt`. Click to download the dependencies [`TestUtilsL23`](https://github.com/xenadevel/xenascriptlibs/blob/master/layer23/python3/testutils/TestUtilsL23.py) and [`SocketDrivers`](https://github.com/xenadevel/xenascriptlibs/blob/master/layer23/python3/testutils/SocketDrivers.py)
- The XOA Python API script consists of three files: `xoa_script.py`, `config.py`, and `config.txt`.


Both scripts result in the same port/stream configuration.

### CLI Code Example
`cli_script.py`
```python
# coding=UTF-8
import time, json, random, queue, types, sys, socket, math, os
from binascii import hexlify
from TestUtilsL23 import XenaScriptTools

def runtest(xm, ports, rate, size, duration):
	print("Start the scripting...")
	##RELEASE THE ports, relinquish other users.
	xm.Send(ports[0] + ' P_RESERVATION RELEASE')
	xm.Send(ports[0] + ' P_RESERVATION relinquish')
	xm.Send(ports[1] + ' P_RESERVATION RELEASE')
	xm.Send(ports[1] + ' P_RESERVATION relinquish')


	##Release the port and then Reserve the ports
	print ("Resever the port...")
	xm.Send(ports[0] + ' P_RESERVATION RESERVE')	
	xm.Send(ports[1] + ' P_RESERVATION RESERVE')
	##RESET PORTS
	xm.Send(ports[0] + ' P_RESET')
	xm.Send(ports[1] + ' P_RESET')
	time.sleep(3)


	MAC1= '000000000002'
	MAC2= '000000000001'
	IP1 = '192.168.100.100'
	IP2 = '192.168.100.101'
	IP1 = hexlify(socket.inet_aton(IP1)).decode()
	IP2 = hexlify(socket.inet_aton(IP2)).decode()
	hearder1 = '0x' + str(MAC2) + str(MAC1) + '08004500002E000000007FFFF0B6' + str(IP1) + str(IP2) 
	hearder2 = '0x' + str(MAC1) + str(MAC2) + '08004500002E000000007FFFF0B6' + str(IP2) + str(IP1) 

	print("Start to configure the streams...")
	##Create the streams in port 0
	##Create the SID index of stream
	xm.SendExpectOK(ports[0] + " PS_CREATE [0]")
	##Create the TPLD index of stream
	xm.SendExpectOK(ports[0] + " PS_TPLDID [0] 0")
	##Configure the packet size
	xm.SendExpectOK(ports[0] + " PS_PACKETLENGTH [0]" + size)
	##Configure the packet type
	xm.SendExpectOK(ports[0] + " PS_HEADERPROTOCOL [0] ETHERNET IP")
	##Configure the packet header
	xm.SendExpectOK(ports[0] + " PS_PACKETHEADER [0] "+ str(hearder1))
	##Enable streams
	xm.SendExpectOK(ports[0] + " PS_ENABLE [0] on")
	##Configure the stream rate
	xm.SendExpectOK(ports[0] + " PS_RATEFRACTION [0] " + str(int(rate)*10000))

	##Create the streams in port 1
	xm.SendExpectOK(ports[1] + " PS_CREATE [1]")
	xm.SendExpectOK(ports[1] + " PS_TPLDID [1] 1")
	xm.SendExpectOK(ports[1] + " PS_PACKETLENGTH [1]" + size)
	xm.SendExpectOK(ports[1] + " PS_HEADERPROTOCOL [1] ETHERNET IP")
	xm.SendExpectOK(ports[1] + " PS_PACKETHEADER [1] "+ str(hearder2))
	xm.SendExpectOK(ports[1] + " PS_ENABLE [1] on")
	xm.SendExpectOK(ports[1] + " PS_RATEFRACTION [1] " + str(int(rate)*10000))

	print("Start the traffic...")
	#####START TRAFFIC
	xm.SendExpectOK(ports[0] + ' P_TRAFFIC ON')
	xm.SendExpectOK(ports[1] + ' P_TRAFFIC ON')
	time.sleep(2)
	xm.SendExpectOK(ports[0] + ' P_TRAFFIC OFF')
	xm.SendExpectOK(ports[1] + ' P_TRAFFIC OFF')
	xm.SendExpectOK(ports[0] + ' PT_CLEAR')
	xm.SendExpectOK(ports[1] + ' PT_CLEAR')
	xm.SendExpectOK(ports[0] + ' PR_CLEAR')
	xm.SendExpectOK(ports[1] + ' PR_CLEAR')
	time.sleep(1)

	xm.SendExpectOK(ports[0] + ' P_TRAFFIC ON')
	xm.SendExpectOK(ports[1] + ' P_TRAFFIC ON')
	time.sleep(int(duration))
	xm.SendExpectOK(ports[0] + ' P_TRAFFIC OFF')
	xm.SendExpectOK(ports[1] + ' P_TRAFFIC OFF')
	print("Stop the traffic and collect the result...")
	xm.Send(ports[0] + ' P_RESERVATION RELEASE')
	xm.Send(ports[1] + ' P_RESERVATION RELEASE')
	time.sleep(2)

	####Get traffic result
	##Get the TX and RX result
	TX1 = (filter(xm, ports[0] + ' PT_STREAM [0] ?'))[3]
	TX2 = (filter(xm, ports[1] + ' PT_STREAM [1] ?'))[3]
	RX1 = (filter(xm, ports[1] + ' PR_TPLDTRAFFIC [0] ?'))[3]
	RX2 = (filter(xm, ports[0] + ' PR_TPLDTRAFFIC [1] ?'))[3]
	print('TX1: %s, TX2: %s, RX1: %s, RX2: %s,'%(TX1, TX2, RX1, RX2))

	##Get the latency 
	latency1 = (filter(xm, ports[1] + ' PR_TPLDLATENCY [0] ?'))[1]
	latency2 = (filter(xm, ports[0] + ' PR_TPLDLATENCY [1] ?'))[1]

	##Get the error
	error1 = filter(xm, ports[1] + ' PR_TPLDERRORS[1] ?')
	error2 = filter(xm, ports[0] + ' PR_TPLDERRORS[0] ?')

	##Get the FCS
	FCS1 = (filter(xm, ports[0] + ' PR_EXTRA ?'))[0]
	FCS2 = (filter(xm, ports[1] + ' PR_EXTRA ?'))[0]

	##Caculate the lost
	Lost1 = int(TX1) - int(RX1)
	Lost2 = int(TX2) - int(RX2)

	##print the result
	print()
	print ('----------------------------------------------------------------------------------------------------')
	print ('Stream1 |  TX: ' + str(TX1) + '  |  RX: ' + str(RX1) + '  |  Lost :' + str(Lost1) + ' |  FCS: ' + str(FCS2) + '  |  Misoder Error: ' + error1[2] + '  |  Payload Errors: ' + error1[3])
	print ('----------------------------------------------------------------------------------------------------')
	print ('Stream2 |  TX: ' + str(TX2) + '  |  RX: ' + str(RX2) + '  |  Lost :' + str(Lost2) + ' |  FCS: ' + str(FCS1) + ' |  Misoder Error: ' + error2[2] + '  |  Payload Errors: ' + error2[3])
	print ('----------------------------------------------------------------------------------------------------')
	print ('Ending.......')


def filter(xm, cmd):
	getvalue = xm.Send(cmd)
	getvalue1 = getvalue.split('  ')[-1]
	getvalue2 = getvalue1.split(' ')
	return getvalue2

def main(argv):
	with open('config.txt','r+') as f:
		configs = f.readlines()
	config_dict = {}
	for conf in configs:
		parsed = conf.strip('\n').split(':')
		if len(parsed) > 1:
			config_dict[parsed[0]] = parsed[1]

	ip_address = config_dict.get('ip_address')
	print(ip_address)
	ports = config_dict.get('ports').split(' ')
	print(ports)
	rate = config_dict.get('rate')
	size = config_dict.get('size')
	duration = config_dict.get('duration')
	xm = XenaScriptTools(ip_address)
	print('Start to connect to the chassis...')
	xm.LogonSetOwner("xena", "python_test_1")
	print('Logon successful...')
	runtest(xm, ports, rate, size, duration)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
```

`config.txt`
```
ip_address:192.168.1.198
ports:2/4 2/5
rate:100
size:FIXED 64 1518
duration:10
```

### XOA Python API Example
`xoa_script.py`
``` python
import asyncio
import socket
import typing
import dataclasses
from binascii import hexlify
from xoa_driver import testers
from xoa_driver import ports
from xoa_driver import utils
from xoa_driver import enums

from config import read_config, Config

class ResultError(typing.NamedTuple):
    dummy: int
    non_incre_seq_event_count: int
    swapped_seq_misorder_event_count: int
    non_incre_payload_packet_count: int

class Results(typing.NamedTuple):
    tx: int
    rx: int
    latency: int
    error: ResultError
    fcs: int

    @classmethod
    def from_data(cls, data):
        tx, rx, latency, error, fcs = data
        return cls(
            tx.packet_count_since_cleared, 
            rx.packet_count_since_cleared,
            latency.avg_val,
            ResultError(*dataclasses.astuple(error)),
            fcs.fcs_error_count
        )

async def prepare_port(port: "ports.GenericL23Port") -> None:
    if port.is_reserved_by_me():
        await port.reservation.set_release()
    elif not port.is_released():
        await port.reservation.set_relinquish()
    await utils.apply(
        port.reservation.set_reserve(),
        port.reset.set()
    )

async def set_stream(port: "ports.GenericL23Port", size: tuple, header: str, rate: int) -> None:
    stream = await port.streams.create() # Create one stream at the port
    header_protocol = [ enums.ProtocolOption.ETHERNET, enums.ProtocolOption.IP]
    await utils.apply(
        stream.tpld_id.set(0), # Create the TPLD index of stream
        stream.packet.length.set(*size), # Configure the packet size
        stream.packet.header.protocol.set(header_protocol), # Configure the packet type
        stream.packet.header.data.set(header), # Configure the packet header
        stream.enable.set_on(), # Enable streams
        stream.rate.fraction.set(rate*10000) # Configure the stream rate
    )

async def clear_statistics(port: "ports.GenericL23Port") -> None:
    await utils.apply(
        port.statistics.tx.clear.set(),
        port.statistics.rx.clear.set()
    )

async def start_traffic(ports: typing.List["ports.GenericL23Port"]) -> None:
    await utils.apply(*[p.traffic.state.set_start() for p in ports])

async def stop_traffic(ports: typing.List["ports.GenericL23Port"]) -> None:
    await utils.apply(*[p.traffic.state.set_stop() for p in ports])


async def fetch_result(port: "ports.GenericL23Port") -> "Results":
    stream = port.streams.obtain(0) # Retrieve stream which we created for port
    tpld = port.statistics.rx.access_tpld(0) # before was port.reception_statistics.access_tpld(0)
    return Results.from_data(
        await utils.apply(
            port.statistics.tx.obtain_from_stream(stream).get(),
            tpld.traffic.get(), 
            tpld.latency.get(),
            tpld.errors.get(),
            port.statistics.rx.extra.get()
        )
    )


async def run_test(test_ports: typing.List["ports.GenericL23Port"], config: "Config") -> None:
    print("Start the scripting...")
    
    print ("Reserve the port...")
    await asyncio.gather(*[ prepare_port(p) for p in test_ports ])
    await asyncio.sleep(3)
    
    MAC1= '000000000002'
    MAC2= '000000000001'
    IP1 = '192.168.100.100'
    IP2 = '192.168.100.101'
    IP1 = hexlify(socket.inet_aton(IP1)).decode()
    IP2 = hexlify(socket.inet_aton(IP2)).decode()
    header1 = f'0x{MAC2}{MAC1}08004500002E000000007FFFF0B6{IP1}{IP2}' 
    header2 = f'0x{MAC1}{MAC2}08004500002E000000007FFFF0B6{IP2}{IP1}'
    
    print("Start to configure the streams...")
    await asyncio.gather(
        set_stream(test_ports[0], config.size, header1, config.rate),
        set_stream(test_ports[1], config.size, header2, config.rate)
    )
    
    print("Start the traffic...")
    await start_traffic(test_ports)
    await asyncio.sleep(2)
    
    await stop_traffic(test_ports)
    await asyncio.gather(*[clear_statistics(p) for p in test_ports]) # Sort of clear ports in parallel
    await asyncio.sleep(1)
    
    await start_traffic(test_ports)
    await asyncio.sleep(config.duration)
    
    await stop_traffic(test_ports)
    await utils.apply(*[p.reservation.set_release() for p in test_ports])
    
    await asyncio.sleep(2)
    
    ports_results = list(await asyncio.gather(*[ fetch_result(p) for p in test_ports ]))
    TX1 = ports_results[0].tx
    TX2 = ports_results[1].tx
    RX1 = ports_results[1].rx
    RX2 = ports_results[0].rx
    
    print('TX1: %s, TX2: %s, RX1: %s, RX2: %s,'%(TX1, TX2, RX1, RX2))

    Lost1 = TX1 - RX1
    Lost2 = TX2 - RX2
    
    output = (
        "----------------------------------------------------------------------------------------------------",
        f"Stream1 |  TX: {TX1}  |  RX: {RX1}  |  Lost : {Lost1} |  FCS: {ports_results[1].fcs}  |  Misoder Error: { ports_results[1].error.swapped_seq_misorder_event_count}  |  Payload Errors: {ports_results[1].error.non_incre_payload_packet_count}",
        "----------------------------------------------------------------------------------------------------",
        f"Stream2 |  TX: {TX2}  |  RX: {RX2}  |  Lost : {Lost2} |  FCS: {ports_results[0].fcs} |  Misoder Error: { ports_results[0].error.swapped_seq_misorder_event_count}  |  Payload Errors: {ports_results[0].error.non_incre_payload_packet_count}",
        "----------------------------------------------------------------------------------------------------",
        "Ending......."
    )
    print("\n".join(output))



async def start() -> None:
    config = read_config("./config.txt")
    print(config.ip_address)
    print(config.ports)
    print('Start to connect to the chassis...')
    async with testers.L23Tester(config.ip_address, "python_test_1", debug=True) as tester:
        test_ports = [ tester.modules.obtain(p.module_id).ports.obtain(p.port_id) for p in config.ports ]
        if any(isinstance(p, ports.PortChimera) for p in test_ports):
            raise ValueError("Please select other port. Chimera Ports can't be used in this test.")
        await run_test(test_ports, config) # type: ignore

def main():
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
```

`config.py`
``` python
import typing
from xoa_driver import enums

class PortInfo(typing.NamedTuple):
    module_id: int
    port_id: int
    
    def __repr__(self):
        return f"{self.module_id}/{self.port_id}"

class PacketLength(typing.NamedTuple):
    length_type: enums.LengthType
    min_val: int 
    max_val: int
    
    @classmethod
    def from_string(cls, data: str):
        length_type, min_val, max_val = data.split()
        return cls(
            enums.LengthType[length_type],
            int(min_val),
            int(max_val)
        )
        
class Config(typing.NamedTuple):
    ip_address: str
    ports: typing.List[PortInfo]
    rate: int
    size: PacketLength
    duration: int

def read_config(path: str) -> "Config":
    config_dict = {}
    with open(path,'r+') as f:
        for conf in f:
            parsed = conf.strip('\n').split(':')
            if len(parsed) <= 1:
                continue
            config_dict[parsed[0]] = parsed[1]
        return Config(
            ip_address=config_dict["ip_address"],
            ports=[ 
                PortInfo(*map(int, port.split('/'))) 
                for port in config_dict['ports'].split(' ') 
            ],
            rate=int(config_dict["rate"]),
            size=PacketLength.from_string(config_dict["size"]),
            duration=int(config_dict["duration"])
        )
```

`config.txt`
```
ip_address:192.168.1.198
ports:2/4 2/5
rate:100
size:FIXED 64 1518
duration:10
```

## Low-Level API User Guide
For users who want to use the low-level API, you can read more from [here](LLAPI.md).




***

Uɴɪғɪᴇᴅ. Oᴘᴇɴ. Iɴᴛᴇɢʀᴀᴛɪᴏɴ.