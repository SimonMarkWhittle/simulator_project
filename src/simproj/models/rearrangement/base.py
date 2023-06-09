
from typing import List
from random import shuffle


class BasicRearrangement:

    def __init__(self):
        pass

    def rearrange(self, list_: List[int]) -> List[int]:
        shuffle(list_)
        return list_
