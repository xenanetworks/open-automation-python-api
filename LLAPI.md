## Low-Level API User Guide
Low-level API gives the developer the complete direct control of the tester since the name of the API is the same as what is defined in the CLI. But sometimes it is difficult to remember all the arguments, resulting a waste of time reading the length class definition. 

However, if the developer needs to migrate a CLI script to XOA Python API script, the low-level API can explicitly show the command name, which may speed up the migration process.

### Code API Notation and Namings
The API trying to be semantic in function name patterns to avoid expectation conflicts, as well as avoiding methods which can return values of a different kind. The key rule is: **One Method One Action**:

> **IMPORTANT**: If there is a method that returns a single item or a collection of items, it is considered a BUG.

`<indices>` - representing `Streams` | `Connection Groups` indices etc.

`<prefix_command_group>` - a group of commands that manage the resources of the same kind but still stays at the same level as others

`<command_name>` - the name of the command's unmodified name. Commands of the same access level, which access or modify parameters of the same kind, are grouped under one `p_commands` group as shown in the example below:
```
 P_SPEEDSELECTION
 P_SPEEDS_SUPPORTED

 are represented as

P_SPEEDSELECTION(TransportationHandler, indices)
P_SPEEDS_SUPPORTED(TransportationHandler, indices)
 ```

### Attributes and Methods
There are only two types of methods for each command, `get` and/or `set`. `get` is used to query values, status, configuration of the command. `set` is the change.

To use `get` and `set` methods, you need to use `await` because they are all made asynchronous. Read more about Python [`awaitable object`](https://docs.python.org/3/library/asyncio-task.html#id2).

`await <command_name>(TransportationHandler, indices).get()`

`await <command_name>(TransportationHandler, indices).set(<values>)`

### Low-Level Code Examples
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


#### Tester Connection

Each tester class is represented as an [awaitable object](https://docs.python.org/3/library/asyncio-task.html#id2). When awaited, it establishes a TCP connection to the tester.

A tester instance also can be created without awaiting the connection establishment for more flexible manipulation of instances in user code.

##### Creating a connection to the tester

```python
# import available module
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection

async def my_awesome_script():
    handler = TransportationHandler(debug=False)
    await establish_connection(handler, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler).set("xena"),
        cmd.C_OWNER(handler).set("JonDoe"),
    ) # establish connection using username "JonDoe".

    # other code ...
```

##### Create multiple connections
```python
# import available module
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection

handler1 = TransportationHandler(debug=False)
await establish_connection(handler1, "192.168.1.198")
await utils.apply(
    cmd.C_LOGON(handler1).set("xena"),
    cmd.C_OWNER(handler1).set("JonDoe"),
) # establish connection using username "JonDoe".

handler2 = TransportationHandler(debug=False)
await establish_connection(handler2, "192.168.1.198")
await utils.apply(
    cmd.C_LOGON(handler2).set("xena"),
    cmd.C_OWNER(handler2).set("Alice"),
) # establish connection using username "Alice".

handler3 = TransportationHandler(debug=False)
await establish_connection(handler3, "192.168.1.198")
await utils.apply(
    cmd.C_LOGON(handler3).set("xena"),
    cmd.C_OWNER(handler3).set("Bob"),
) # establish connection using username "Bob".
```


#### Obtain Resources
##### Obtain one module
```python
# import available module
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection

async def my_awesome_script():
    handler1 = TransportationHandler(debug=False)
    await establish_connection(handler1, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler1).set("xena"),
        cmd.C_OWNER(handler1).set("JonDoe"),
    ) # establish connection using username "JonDoe".

    print(await M_PORTCOUNT(handler, 0).get()) # get test module 0 port count

    # other code ...
```

##### Obtain multiple modules
```python
# import available module
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection

async def my_awesome_script():
    handler1 = TransportationHandler(debug=False)
    await establish_connection(handler1, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler1).set("xena"),
        cmd.C_OWNER(handler1).set("JonDoe"),
    ) # establish connection using username "JonDoe".

    print(await cmd.M_PORTCOUNT(handler, 0).get()) # get test module 0 port count
    print(await cmd.M_PORTCOUNT(handler, 1).get()) # get test module 1 port count
    print(await cmd.M_PORTCOUNT(handler, 2).get()) # get test module 2 port count

    # other code ...
```

#### Data Exchange
##### Querying parameters

> **IMPORTANT**: resource reservation is not required to query information from the tester.

```python
# import available module
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection

async def my_awesome_script():
    handler = TransportationHandler(debug=False)
    await establish_connection(handler1, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler).set("xena"),
        cmd.C_OWNER(handler).set("JonDoe"),
    ) # establish connection using username "JonDoe".

    print(await cmd.P_SPEED_SUPPORTED(handler, 0, 0).get()) # get speeds supported of port 0/0
    print(await cmd.P_SPEED_SUPPORTED(handler, 0, 1).get())# get speeds supported of port 0/1

    # other code ...
```

##### Setting parameters

> **IMPORTANT**: reservation is required to set parameter to `Tester`, `Module`, and `Port`.

```python
# import available module
from xoa_driver import utils
from xoa_driver import enums
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection

async def my_awesome_script():
    handler = TransportationHandler(debug=False)
    await establish_connection(handler1, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler).set("xena"),
        cmd.C_OWNER(handler).set("JonDoe"),
    ) # establish connection using username "JonDoe".

    reservation = await cmd.P_RESERVATION(handler, 0, 0).get() # port 0/0
    if not reservation == enums.ReservedStatus.RELEASED:
        await cmd.P_RESERVATION(handler, 0, 0).set(enums.ReservedAction.RELINQUISH)
    await cmd.P_RESERVATION(handler, 0, 0).set(enums.ReservedAction.RESERVE)

    await cmd.P_COMMENT(handler, 0, 0).set(comment="My Port")

    # other code ...
```

#### Statistics Collection
Statistics collection, such as latency and jitter, TX/RX rate, frame count, etc., can be done by Python standard library `asyncio`. In case you are new to `asyncio`, the example below may help you understand how to use `asyncio` to query counters.

```python
import asyncio
# import available module
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection

async def background_task(handler: TransportationHandler):
   while True:
       print(await cmd.PT_STREAM(handler, 0, 0, 0).get()) # port 0/0, stream[0]
       print(await cmd.PR_STREAM(handler, 0, 1, 0).get()) # # port 0/1, stream [0]
       await async.sleep(1)

async def my_awesome_script():
    # my code ...
    handler = TransportationHandler(debug=False)
    await establish_connection(handler1, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler).set("xena"),
        cmd.C_OWNER(handler).set("JonDoe"),
    ) # establish connection using username "JonDoe".

    asyncio.create_task(background_task(handler)) # put function to work in the background
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
