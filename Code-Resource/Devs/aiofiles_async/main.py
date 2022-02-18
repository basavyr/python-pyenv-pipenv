import asyncio

import write
import data
import read

filename = 'aio_data.dat'


async def main():
    writer = write.Write(filename=filename)
    reader = read.Read(filename=filename)

    local_data = data.Data.GenerateData()

    await writer.WriteData(local_data)

    data_size = await reader.ReadData()
    print(data_size)


if __name__ == '__main__':
    asyncio.run(main())
