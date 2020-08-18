import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(sqlite3.version)
        return connection
    except Error as e:
        print(e)

    return connection


def create_table(create_table_sql):
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


connection = create_connection(r"stonks.db")

if connection is not None:
    stonks_table = """ CREATE TABLE IF NOT EXISTS stonks (
                                        id integer PRIMARY KEY,
                                        currency text,
                                        description text,
                                        displaySymbol text,
                                        symbol text,
                                        type text
                                    ); """

    create_table(stonks_table)
else:
    print("Error! cannot create the database connection.")
