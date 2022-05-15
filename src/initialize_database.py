from db_connection import get_database_connection


def drop_tables(connection):
    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS Saves;")
    connection.commit()


def create_tables(connection):
    cur = connection.cursor()
    cur.execute("CREATE TABLE Saves(id INTEGER PRIMARY KEY, name TEXT, "\
        "highest_complete INTEGER DEFAULT 0);")
    connection.commit()

def create_defaults(connection):
    cur = connection.cursor()
    cur.execute("INSERT INTO Saves (name) VALUES ('Save_1');")
    cur.execute("INSERT INTO Saves (name) VALUES ('Save_2');")
    cur.execute("INSERT INTO SAVES (name) VALUES ('Save_3');")
    cur.execute("INSERT INTO SAVES (name) VALUES ('Save_4');")
    connection.commit()

def execute():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)
    create_defaults(connection)

if __name__ == "__main__":
    execute()
