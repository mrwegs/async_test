# import requests
# from time import time
#
# def get_file(url):
#     r = requests.get(url, allow_redirects=True)
#     return r
#
#
# def save_file(response):
#     name = response.url.split('/')[-1]
#
#     with open(name, 'wb') as file:
#         file.write(response.content)
#
#
# def main():
#     start = time()
#     url = "https://loremflickr.com/320/240"
#
#     for _ in range(10):
#         save_file(get_file(url))
#
#     print(time() - start)
#
#
# if __name__ == '__main__':
#     main()

#######################################################################
import asyncio
import aiohttp
from time import time


def write_file(data):
    name = f'file-{int(time() * 1000)}.jpeg'
    with open(name, 'wb') as file:
        file.write(data)


async def fetch_file(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_file(data)


async def main():
    url = "https://loremflickr.com/320/240"

    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_file(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time()

    asyncio.run(main())

    print(time() - start)