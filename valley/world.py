import numpy as np


class GridWorld:
    def __init__(self, size):
        self._size = size
        self._world = np.random.randint(4, size=self._size)

    def __getitem__(self, item):
        return self._world[item]
