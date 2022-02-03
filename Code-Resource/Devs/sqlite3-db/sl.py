import sqlite3 as db

from sqlite3 import Error


def create_connection(database):
    """
    Establish a database connection to a (new) SQLite database
    """
    connection = None

    try:
        connection = db.connect(database)
        # print(db.version)
    except Error as err:
        print(
            f'There was an issue while trying to connect to the database\n{err}')
    finally:
        # close the connection
        if connection:
            connection.close()


def main():
    db_file = 'sqlite_0.db'
    create_connection(db_file)


if __name__ == '__main__':
    main()
