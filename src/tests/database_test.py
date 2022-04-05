from sqlite3 import DatabaseError
import unittest
from db_connection import get_database_connection

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection()

    def test_yhteyden_luonti_onnistuu(self):
        self.assertNotEqual(self.connection, None)