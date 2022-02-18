import asyncio
import aiofiles


class Read:
    def __init__(self, filename):
        self.fileName = filename

    async def ReadData(self):
        async with aiofiles.open(self.fileName, 'r') as f:
            content = await f.readlines()

        size = len(content)
        try:
            assert size > 0
        except AssertionError as error:
            print(f'The file is empty or corrupt -> size = {size}')
        else:
            return size
