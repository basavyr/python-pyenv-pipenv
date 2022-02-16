import time
import asyncio


async def timedPrint(name):
    await asyncio.sleep(2)
    print(f'Hi {name}')


async def showprints():
    for _ in range(3):
        name = 'test'
        await timedPrint(name)


async def computesum(n):
    summ = 0
    for i in range(n):
        print(f'adding {i} to the summation')
        time.sleep(1)
        summ = summ + i
    return summ


async def main():
    task = asyncio.create_task(showprints())
    task2 = asyncio.create_task(computesum(5))
    task_value = await task
    task2_value = await task2
    print(task)
    print(task2_value)

if __name__ == '__main__':
    asyncio.run(main())
