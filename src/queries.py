from db_connection import get_database_connection

connection = get_database_connection()

def get_completed(save_id):
    cur = connection.cursor()
    result = cur.execute("SELECT highest_complete FROM Saves WHERE id=?;", (save_id,))
    return result.fetchone()[0]

def get_saves():
    cur = connection.cursor()
    result = cur.execute("SELECT id, name FROM Saves ORDER BY id ASC;")
    return result.fetchall()

def get_name(save_id):
    cur = connection.cursor()
    result = cur.execute("SELECT name FROM Saves WHERE id=?;", (save_id,))
    return result.fetchone()[0]

def set_highest(new_highest, save_id):
    cur = connection.cursor()
    cur.execute("UPDATE Saves SET highest_complete=? WHERE id=?;", (new_highest, save_id))
    connection.commit()
