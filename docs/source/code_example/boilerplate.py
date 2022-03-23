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