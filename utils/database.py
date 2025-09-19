import sqlite3
from datetime import datetime


def today():
    return datetime.now().strftime("%y-%m-%d")


class DataBase:

    def __init__(self):
        self.db = sqlite3.connect('DB/habits.db')
        self.cursor = self.db.cursor()
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS timelog (
                    date TEXT,
                    tag TEXT,
                    start TEXT,
                    stop TEXT,
                    total TEXT)
            ''')

    def get_queries(self, tag=None, date=None):
        if not date:
            date = today()

        if not tag:
            self.cursor.execute(
                "SELECT * FROM timelog WHERE date = ?", (date,))
            return self.cursor.fetchall()

        self.cursor.execute(
            'SELECT * FROM timelog WHERE date = ? AND tag = ?', (date, tag))
        return self.cursor.fetchall()

    def parse_data(self, data):
        if not data or len(data) < 1:
            return None
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

    def update(self, data: list[list[str]]) -> int | None:
        clean_data = self.parse_data(data)
        if not clean_data:
            return 1

        self.cursor.executemany(
            'INSERT INTO timelog VALUES(:date, :tag, :start, :stop, :total)',
            clean_data)
        self.db.commit()
        return None

    def get_last_entry(self):
        entries = self.get_queries()
        if entries:
            return entries[-1]
        return None

    def get_tags(self):
        self.cursor.execute('SELECT tag FROM timelog')
        tags = set(self.cursor.fetchall())
        if tags:
            return [tag_tuple[0] for tag_tuple in tags]
        else:
            return None
