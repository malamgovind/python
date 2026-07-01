import asyncio

async def work():

    await asyncio.sleep(5)

async def main():

    try:

        await asyncio.wait_for(
            work(),
            timeout=2
        )

    except asyncio.TimeoutError:

        print("Timeout")

asyncio.run(main())