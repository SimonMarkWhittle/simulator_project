
try:
    from modproj.numberstreamator import Numberstreamator

    NUMBERSTREAMATOR_IMPORT = True
except ImportError:
    NUMBERSTREAMATOR_IMPORT = False

from typing import List


class NumberstreamatorAdaptor:

    def __init__(self, minrange=0, maxrange=100):

        if not NUMBERSTREAMATOR_IMPORT:
            raise ImportError("Attempting to construct NumberstreamatorAdaptor when modproj package is not installed!")

        self.minrange = minrange
        self.maxrange = maxrange

        self._numberstreamator = Numberstreamator(
            1,
            self.maxrange - self.minrange
        )

    def get_numbers(self, count: int) -> List[int]:
        return [self._numberstreamator.stream_numbers()[0] + self.minrange for _ in range(count)]
