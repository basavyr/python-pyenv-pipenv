import asyncio
import aiofiles
import data


class Write:
    def __init__(self, filename):
        self.fileName = filename

    def stringify(self, data):
        return str(data)

    async def WriteData(self, data):
        if(len(data) == 0):
            print(f'Cannot write to file since data is empty')
            await asyncio.sleep(1)
            return
        async with aiofiles.open(self.fileName, 'w+') as f:
            # https://www.twilio.com/blog/working-with-files-asynchronously-in-python-using-aiofiles-and-asyncio
            for data_element in data:
                await f.write(self.stringify(data_element))
                await f.write('\n')

    async def BatchWrite(self, no_batches):
        for idx in range(no_batches):
            print(f'Writing data element to the file...')

            await self.WriteData(data.Data.GenerateData())
            await asyncio.sleep(1)

            print(f'Finished writing data element to the file...')
            print(f'*********')
