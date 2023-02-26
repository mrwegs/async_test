import asyncio


async def print_numbers():
    num = 0
    while num < 1000:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while count < 1000:
        print(f'прошло {count} секунд')
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task2, task1)


if __name__ == '__main__':
    asyncio.run(main())
