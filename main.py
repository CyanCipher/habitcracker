from timew import Timew
from database import DataBase
from datetime import datetime


class HabitTracker:
    def __init__(self):
        self.timew = Timew()
        self.db = DataBase()

    def today(self):
        return datetime.now().strftime("%y-%m-%d")

    def update(self):
        data = self.timew.get_data()
        last_entry = self.db.get_last_query()

        if not last_entry:
            self.db.update(data)
            return

        if last_entry[0] == self.today():
            if last_entry[1:] in data:
                if data[-1] == last_entry[1:]:
                    return
                self.db.update(data[data.index(last_entry[1:])+1:])
                return

    def get_queries(self, date=None):
        if date:
            return self.db.get_queries(date=date)
        return self.db.get_queries()


def main():
    ht = HabitTracker()
    while True:
        usr_choice = input('Display Data(D) | Update Data(U): ')
        if usr_choice == 'd':
            for line in ht.get_queries():
                print(line)

        if usr_choice == 'u':
            ht.update()


if __name__ == "__main__":
    main()
