import asyncio
import aiofiles


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
            for data_element in data:
                await f.write(self.stringify(data_element))
                await f.write('\n')
