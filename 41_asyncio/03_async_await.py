import asyncio

async def greet():

    print("Hello")

    await asyncio.sleep(2)

    print("Python")

asyncio.run(greet())