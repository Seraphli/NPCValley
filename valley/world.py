import numpy as np


class GridWorld:
    def __init__(self, size):
        self._size = size
        self._world = np.zeros(self._size)
