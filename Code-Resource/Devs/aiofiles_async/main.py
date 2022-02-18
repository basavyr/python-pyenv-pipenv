import asyncio

import write
import data
import read

filename = 'aio_data.dat'


async def main():
    writer = write.Write(filename=filename)
    reader = read.Read(filename=filename)

    local_data = lambda: data.Data.GenerateData()

    # await writer.WriteData(local_data)

    H = await asyncio.gather(
        writer.BatchWrite(3),
        reader.BatchRead(3),
    )


if __name__ == '__main__':
    asyncio.run(main())
