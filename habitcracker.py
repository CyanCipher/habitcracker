from utils.timew import Timew
from utils.database import DataBase
from utils.plotter import Plotter
from datetime import datetime


class HabitTracker:
    def __init__(self):
        self.timew = Timew()
        self.db = DataBase()
        self.plt = Plotter()
        self.colors = ['lightgreen', 'lightblue', 'blue', 'red', 'black']

    def today(self):
        return datetime.now().strftime("%y-%m-%d")

    def update(self):
        data = self.timew.get_data()
        last_entry = self.db.get_last_entry()

        if not last_entry:
            err = self.db.update(data)
            if err:
                print("Empty Dataset!")
                return

        if last_entry[0] == self.today():
            if last_entry[1:] in data:
                if data[-1] == last_entry[1:]:
                    return
                self.db.update(data[data.index(last_entry[1:])+1:])
                return

    def get_queries(self, tag=None, date=None):
        return self.db.get_queries(tag=tag, date=date)

    def get_tags(self):
        return self.db.get_tags()

    def plot_data(self):
        dataset = {}
        tags = self.get_tags()
        if not tags:
            print("No plottable data found")
            return
        for tag in tags:
            data_list = self.db.get_queries(tag=tag)
            data_list = sorted(
                data_list, key=lambda x: datetime.strptime(x[2], '%H:%M:%S'))
            dataset[tag] = data_list
        self.plt.gen_graph(dataset)
