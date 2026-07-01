import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Task 1")

async def task2():
    await asyncio.sleep(2)
    print("Task 2")

async def main():

    tasks = [
        asyncio.create_task(task1()),
        asyncio.create_task(task2())
    ]

    await asyncio.wait(tasks)

asyncio.run(main())