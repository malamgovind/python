import asyncio

async def task():

    print("Start")

    await asyncio.sleep(3)

    print("End")

asyncio.run(task())