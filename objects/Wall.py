from abc import ABC
from matplotlib import axes, pyplot as plt
import constants
import Object


class Wall(Object):
    absorption = constants.WALL_ABSORPTION

    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        super().__init__(x1, y1, x2, y2)

    def draw(self) -> None:
        self.ax.plot([self.x1, self.x1 + self.x2], [self.y1, self.y1 + self.y2], color='black')
        #self.ax.quiver(self.x1, self.y1, self.x2, self.y2, angles='xy', scale_units='xy', scale=1, color='black')
        plt.draw()
