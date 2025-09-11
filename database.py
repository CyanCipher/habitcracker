import sqlite3
from datetime import datetime


def today():
    return datetime.now().strftime("%y-%m-%d")


class DataBase:

    def __init__(self):
        self.db = sqlite3.connect('habits.db')
        self.cursor = self.db.cursor()
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS timelog (
                    date TEXT,
                    tag TEXT,
                    start TEXT,
                    stop TEXT,
                    total TEXT)
            ''')

    def get_queries(self, date=None):
        if not date:
            date = today()

        self.cursor.execute("SELECT * FROM timelog WHERE date = ?", (date,))
        return self.cursor.fetchall()

    def parse_data(self, data):
        if not data or len(data) < 1:
            raise ValueError('empty dataset provided to the database')
        result = []
        for chunk in data:
            chunk_data = {
                'date': today(),
                'tag': chunk[0],
                'start': chunk[1],
                'stop': chunk[2],
                'total': chunk[3],
            }
            result.append(chunk_data)
        return tuple(result)

    def update(self, data):
        clean_data = self.parse_data(data)
        if not clean_data:
            return None

        self.cursor.executemany(
            'INSERT INTO timelog VALUES(:date, :tag, :start, :stop, :total)', clean_data)
        self.db.commit()

    def get_last_query(self):
        entries = self.get_queries()
        if entries:
            return entries[-1]
        return None
