import asyncio
import data_reader
import data_writer
import data_generator


async def main():
    # the file where the data should be written at
    FILENAME = 'data.dat'
    # a randomly generated data to be written into the file
    MY_DATA = data_generator.Data().GenerateData()

    writer = data_writer.Writer(FILENAME)
    reader = data_reader.Reader(FILENAME)

    # # ----------------------
    write_task = asyncio.create_task(writer.write_to_file_async(MY_DATA, 1))

    await write_task

    # # ----------------------
    read_task = asyncio.create_task(reader.read_file_async())

    await read_task

    # H = await asyncio.gather(
    #     writer.write_to_file_async(MY_DATA, verbose=1),
    #     reader.repeated_reader(10)
    # )
    # print(H)

if __name__ == '__main__':
    data_reader.asyncio.run(main(), debug=True)
