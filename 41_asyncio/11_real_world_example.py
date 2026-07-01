import asyncio

async def download(file):

    print(file,"Downloading")

    await asyncio.sleep(2)

    print(file,"Completed")

async def main():

    await asyncio.gather(

        download("image.jpg"),

        download("video.mp4")
    )

asyncio.run(main())