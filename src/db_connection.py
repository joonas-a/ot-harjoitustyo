import os
import sqlite3

FOLDER = os.path.dirname(__file__)

CONNECTION = sqlite3.connect(os.path.join(
    FOLDER, "data", "database.sqlite"))


def get_database_connection():
    return CONNECTION
