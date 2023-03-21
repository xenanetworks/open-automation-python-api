import asyncio
from xoa_driver.hlfuncs import mgmt

async def main():
    known_hosts = [
        "192.168.1.200",
        "192.168.1.201"
        ]
        
    my_tester_pool = mgmt.get_testers( known_hosts, "xoa")
    # now we can do ``await testers_pool[0]`` which establishes the connection

    # we also can use asyncio.gather for await all testers at once in concurrent mode
    await asyncio.gather(*my_tester_pool) 
    print(my_tester_pool[0].session.is_online)
    print(my_tester_pool[0].session.owner_name)
    

if __name__ == "__main__":
    asyncio.run(main())