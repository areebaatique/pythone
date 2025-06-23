import sqlite3
from resource_interface import Resource

class DBResource:
    def __init__(self, db_file: str):
        self.db_file = db_file
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)
        print(f"Connected to DB {self.db_file}")

    def close(self):
        if self.conn:
            self.conn.close()
            print(f"Disconnected from DB {self.db_file}")

    def read(self, query: str) -> str:
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return str(rows)

    def write(self, data: str) -> None:
        cursor = self.conn.cursor()
        cursor.executescript(data)
        self.conn.commit()
