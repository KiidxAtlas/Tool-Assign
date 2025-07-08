import sqlite3

class SQLiteManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None
        