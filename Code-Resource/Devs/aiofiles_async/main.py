import asyncio

import write
import data

filename = 'aio_data.dat'


async def main():
    writer = write.Write(filename=filename)
    local_data = data.Data.GenerateData()
    await writer.WriteData(local_data)


if __name__ == '__main__':
    asyncio.run(main())
