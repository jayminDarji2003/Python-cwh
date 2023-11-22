# AsyncIO in python

import aiohttp
import asyncio
import os


async def download_image(session, url, filename):
    async with session.get(url) as response:
        if response.status == 200:
            with open(filename, "wb") as f:
                f.write(await response.read())
            print(f"Downloaded {url} to {filename}")
        else:
            print(f"Failed to download {url}")


async def main():
    # URLs of the images you want to download
    image_urls = [
        "https://images.unsplash.com/photo-1671726203454-5d7a5370a9f4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w0NTg2NjV8MXwxfHNlYXJjaHwxfHxsYXB0b3B8ZW58MHx8fHwxNzAwNjMxNjI1fDA&ixlib=rb-4.0.3&q=80&w=400",
        "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w0NTg2NjV8MHwxfHNlYXJjaHwyfHxsYXB0b3B8ZW58MHx8fHwxNzAwNjMxNjI1fDA&ixlib=rb-4.0.3&q=80&w=400",
        "https://images.unsplash.com/photo-1515378960530-7c0da6231fb1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w0NTg2NjV8MHwxfHNlYXJjaHw0fHxsYXB0b3B8ZW58MHx8fHwxNzAwNjMxNjI1fDA&ixlib=rb-4.0.3&q=80&w=400",
    ]

    # Create an aiohttp ClientSession
    async with aiohttp.ClientSession() as session:
        # Create tasks for each image download
        tasks = []
        for i, url in enumerate(image_urls):
            filename = f"image_{i+1}.jpg"
            tasks.append(download_image(session, url, filename))

        # Execute the tasks concurrently
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    # Run the asyncio event loop
    asyncio.run(main())
