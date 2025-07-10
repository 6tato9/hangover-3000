# database.py
import sqlite3

class HangoverDatabase:
    def __init__(self, db_name="hangover.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS drinks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            drink_name TEXT,
            glasses INTEGER,
            severity INTEGER,
            story TEXT
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert(self, date, name, glasses, severity, story):
        query = '''
        INSERT INTO drinks (date, drink_name, glasses, severity, story)
        VALUES (?, ?, ?, ?, ?)
        '''
        self.conn.execute(query, (date, name, glasses, severity, story))
        self.conn.commit()
