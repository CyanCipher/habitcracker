import matplotlib.pyplot as plt
from datetime import datetime
from typing import List, Tuple


class Plotter:

    def __init__(self):
        pass

    def parse_data(self, data: List[Tuple]) -> Tuple[List[float], List[str]] | None:
        heights = []
        timestamps = []

        if not data:
            return None

        for chunk in data:
            start, stop = datetime.strptime(chunk[2], '%H:%M:%S'), \
                datetime.strptime(chunk[3], '%H:%M:%S')
            diff = stop - start
            minutes = diff.seconds//60
            hours = minutes//60 + round((minutes % 60)/100, 2)
            if hours >= 0.2:
                heights.append(hours)
                timestamps.append(start.strftime('%H:%M'))

        return (heights, timestamps)

    def gen_graph(self, dataset):
        fig, ax = plt.subplots()

        for tag, data in dataset.items():
            try:
                heights, data = self.parse_data(data)
            except ValueError:
                heights, data = [], []
            ax.bar(data, height=heights, label=tag)
        ax.set_title('Time Tracker')
        ax.set_ylabel('Duration in hours')
        ax.legend()
        plt.savefig('temp.png')
