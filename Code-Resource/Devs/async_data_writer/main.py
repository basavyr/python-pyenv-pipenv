import data_reader
import data_writer
import data_generator


def main():
    # the file where the data should be written at
    FILENAME = 'data.dat'
    # a randomly generated data to be written into the file
    MY_DATA = data_generator.Data(5, 3).GenerateData()

    writer = data_writer.Writer(FILENAME)
    reader = data_reader.Reader(FILENAME)

    # ----------------------
    data_reader.asyncio.run(writer.write_to_file_async(MY_DATA, 1))

    # ----------------------
    data_size = reader.read_file()
    print(data_size)


async def main():
    # the file where the data should be written at
    FILENAME = 'data.dat'
    # a randomly generated data to be written into the file
    MY_DATA = data_generator.Data(5, 3).GenerateData()

    writer = data_writer.Writer(FILENAME)
    reader = data_reader.Reader(FILENAME)

    # # ----------------------
    await writer.write_to_file_async(MY_DATA, 1)

    # # ----------------------
    await reader.read_file_async()
    


if __name__ == '__main__':
    data_reader.asyncio.run(main())
