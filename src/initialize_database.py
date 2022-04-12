from db_connection import get_database_connection


def drop_tables(connection):
    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS Users;")
    connection.commit()


def create_table(connection):
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE Users(id INTEGER PRIMARY KEY, username TEXT UNIQUE);")


def execute():
    connection = get_database_connection()
    drop_tables(connection)
    create_table(connection)
