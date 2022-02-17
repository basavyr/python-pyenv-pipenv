import data_reader
import data_writer


def main():
    FILENAME = 'data.dat'
    writer = data_writer.Writer(FILENAME)
    reader = data_reader.Reader(FILENAME)

    reader.read_file()


if __name__ == '__main__':
    main()
