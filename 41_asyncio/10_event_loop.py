import asyncio

async def hello():
    print("Event Loop Running")

asyncio.run(hello())