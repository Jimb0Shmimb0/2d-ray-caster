import matplotlib.pyplot as plt

from objects.Wall import Wall


class Setup:

    def __init__(self):
        self.ax = plt.subplot()
        self.walls = []
        self.sources = []
        self.panels = []

    def set_wall(self, x1: float, y1: float, x2: float, y2: float):
        self.walls.append(Wall(x1, y1, x2, y2))

    # TODO: Make set_source, set_panel. Create the Source class

