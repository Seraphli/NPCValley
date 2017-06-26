import numpy as np

TerrainType = {
    0: "grass",
    1: "water",
    2: "ice",
    3: "desert"
}

TerrainColor = {
    0: (0, 128, 0),
    1: (0, 0, 128),
    2: (255, 255, 255),
    3: (255, 255, 0)
}


class Ground(object):
    def __init__(self, altitude):
        self.altitude = altitude


def generate_terrain(size):
    chunk_size = [20, 20]
    width, height = size
    chunk_num = [width // chunk_size[0], height // chunk_size[1]]
    if width < chunk_size[0]:
        chunk_size[0] = width
        chunk_num[0] += 1
    if height < chunk_size[1]:
        chunk_size[1] = height
        chunk_num[1] += 1
    x = np.random.randint(chunk_size[0], size=chunk_num)
    y = np.random.randint(chunk_size[1], size=chunk_num)
    h = np.random.randint(-500, 2000, size=chunk_num)
    anchor = np.random.randint(-500, 2000, size=(2, 2))
    print(x, y, h, anchor)


if __name__ == '__main__':
    generate_terrain((25, 25))
