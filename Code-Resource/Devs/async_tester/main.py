import time
import asyncio


async def timedPrint(name):
    await asyncio.sleep(2)
    print(f'Hi {name}')


async def showprints():
    for _ in range(3):
        name = 'test'
        await timedPrint(name)


async def main():
    task = asyncio.create_task(showprints())
    print(1)
    task_value = await task


if __name__ == '__main__':
    asyncio.run(main())
