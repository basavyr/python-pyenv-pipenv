import asyncio
import time

# function for measuring execution time
from timeit import default_timer


class Writer:
    def __init__(self, datafile):
        self.dataFile = datafile

    def write_to_file(self, data, verbose):
        """
        - write data to a file synchronously
        """
        idx = 0
        with open(self.dataFile, 'w+') as writer:
            for data_element in data:
                if(verbose == 1):
                    print(f'######### ITERATION {idx+1} #########')
                if(verbose == 1):
                    print('Writing a data element into the file...')
                writer.write(data_line)
                writer.write('\n')
                idx = idx + 1
                if(verbose == 1):
                    print('Finished writing a data element to the file...')
