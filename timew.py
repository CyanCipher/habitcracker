import subprocess
from typing import Tuple, List, TypeAlias
import re


TagT: TypeAlias = str | None
TimeT: TypeAlias = Tuple[str, ...]
TimeTextT: TypeAlias = Tuple[TagT, str, str, str]


class Timew:

    def __init__(self):
        self.data = ''

    def get_tag(self, text: str) -> str | None:
        match = re.search(r'@\d+\s+(\w+)', text)
        if match:
            return match.group(1)
        return None

    def get_time(self, text: str) -> TimeT:
        match = re.search(r'\s+([\d:]+)\s+-*\s*([\d:]+)\s*([\d:]+)', text)
        if match:
            return (match.group(1), match.group(2), match.group(3))
        return tuple()

    def get_data(self) -> List[TimeTextT]:
        raw_output = subprocess.run(
            ['timew', 'summary'], capture_output=True, text=True)
        self.data = raw_output.stdout.split('\n')[3:-5]
        result = []
        for row in self.data:
            tag = self.get_tag(row)
            time = self.get_time(row)
            result.append((tag, time[0], time[1], time[2]))
        return result
