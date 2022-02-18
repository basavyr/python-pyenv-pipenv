import asyncio
import aiofiles


class Read:
    def __init__(self, filename):
        self.fileName = filename

    async def ReadData(self):
        async with aiofiles.open(self.fileName, 'r') as f:
            # https://www.twilio.com/blog/working-with-files-asynchronously-in-python-using-aiofiles-and-asyncio
            content = await f.readlines()

        size = len(content)
        try:
            assert size > 0
        except AssertionError as error:
            print(f'The file is empty or corrupt -> size = {size}')
        else:
            return size

    async def BatchRead(self, no_batches):
        for idx in range(no_batches):
            # for the first iteration, wait 2 seconds to make sure the writer module has properly added data in the file
            print(f'Reading the data from the file')
            if(idx == 0):
                await asyncio.sleep(1)
            size = await self.ReadData()
            print(f'File size -> {size}')
            await asyncio.sleep(1)
            print(f'Finished reading the data from the file')
