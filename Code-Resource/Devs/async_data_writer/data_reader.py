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
        with open(self.dataFile, 'r+') as reader:
            data = reader.readlines()
            data_size = len(data)

        try:
            assert data_size > 0
        except AssertionError as err:
            print(f'The file is empty or corrupt -> size={data_size}')
        else:
            return data_size
