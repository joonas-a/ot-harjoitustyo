import os
import sqlite3

folder = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(
    folder, "..", "data", "database.sqlite"))


def get_database_connection():
    return connection
