import asyncio

async def work():

    print("Working")

async def main():

    task = asyncio.create_task(work())

    await task

asyncio.run(main())