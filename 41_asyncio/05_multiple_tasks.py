import asyncio

async def task(name):

    print(name)

async def main():

    await asyncio.gather(
        task("Task 1"),
        task("Task 2")
    )

asyncio.run(main())