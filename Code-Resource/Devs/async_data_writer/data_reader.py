import asyncio
import time

# function for measuring execution time
from timeit import default_timer


class Reader:
    def __init__(self, datafile):
        self.dataFile = datafile

    def read_file(self):
        """
        - read data from a file synchronously
        """

        data_size = 0

        try:
            with open(self.dataFile, 'r+') as reader:
                data = reader.readlines()
                data_size = len(data)
        except FileNotFoundError as err:
            print(f'Cannot read the file since it does not exist -> {err}')
        else:
            pass

        try:
            assert data_size > 0
        except AssertionError as err:
            print(f'The file is empty or corrupt -> size = {data_size}')
        else:
            return data_size

    async def read_file_async(self):
        """
        - read data from a file asynchronously
        """
        # await self.read_file()  # cannot await a function that is not async
        data_size = 0

        # add a safety sleep befure checking the file
        # await asyncio.sleep(5)

        try:
            with open(self.dataFile, 'r+') as reader:
                data = reader.readlines()
                data_size = len(data)
        except FileNotFoundError as err:
            print(f'Cannot read file since it does not exist ->{err}')
        else:
            pass

        try:
            assert data_size > 0
        except AssertionError as err:
            print(f'The data file is empty or corrupt -> size = {data_size}')
        else:
            print(f'Finished reading data from the file -> size = {data_size}')
            return data_size

    async def repeated_reader(self, time):
        for _ in range(time):
            await self.read_file_async()
            await asyncio.sleep(1)