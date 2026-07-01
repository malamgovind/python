import asyncio

async def square(n):

    return n*n

async def main():

    result = await asyncio.gather(
        square(2),
        square(3),
        square(4)
    )

    print(result)

asyncio.run(main())