
from typing import List
from random import randint


class BasicNumberstream:

    def __init__(self, minrange=0, maxrange=100):
        self.minrange = minrange
        self.maxrange = maxrange

    def get_numbers(self, count: int) -> List[int]:
        return [randint(self.minrange, self.maxrange) for _ in range(count)]
