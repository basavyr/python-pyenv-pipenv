import time
import asyncio
from timeit import default_timer


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
        # print(f'adding {i} to the summation')
        # time.sleep(1)
        await asyncio.sleep(1)
        summ = summ + i
    return summ


async def main():
    task = asyncio.create_task(showprints())
    task2 = asyncio.create_task(computesum(5))
    # task_value = await task
    # task2_value = await task2
    print(task)
    print(task2_value)


async def parallelsum():
    # https://stackoverflow.com/questions/47169474/parallel-asynchronous-io-in-pythons-coroutines
    results = await asyncio.gather(computesum(3), computesum(2),)
    print(results)

if __name__ == '__main__':
    # asyncio.run(main())
    start = default_timer()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(parallelsum())
        loop.run_until_complete(loop.shutdown_asyncgens())
    finally:
        loop.close()
    stop = default_timer()
    print(stop - start)
