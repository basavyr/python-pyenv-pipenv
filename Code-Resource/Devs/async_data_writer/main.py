import data_reader
import data_writer


def main():
    FILENAME = 'data.dat'
    writer = data_writer.Writer(FILENAME)
    print(writer.dataFile)


if __name__ == '__main__':
    main()
