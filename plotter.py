import matplotlib.pyplot as plt
from datetime import datetime
from typing import List, Tuple


class Plotter:

    def __init__(self):
        pass

    def parse_data(self, data: List[Tuple]) -> Tuple[List[int], List[str]] | None:
        heights = []
        timestamps = []

        if not data:
            return None

        for chunk in data:
            start, stop = datetime.strptime(
                chunk[1], '%H:%M:%S'), datetime.strptime(chunk[2], '%H:%M:%S')
            diff = stop - start
            minutes = diff.seconds//60
            if minutes >= 5:
                heights.append(minutes)
                timestamps.append(start.strftime('%H:%M'))

        return (heights, timestamps)

    def gen_graph(self, data):
        try:
            heights, data = self.parse_data(data)
        except ValueError:
            raise ValueError("can't generate plot with empty data")
        plt.bar(data, height=heights)
        plt.savefig('temp.png')

