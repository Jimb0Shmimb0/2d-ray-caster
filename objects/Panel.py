from matplotlib import axes, pyplot as plt
from constants_and_enums import constants
from .Object import Object


class Panel(Object):
    absorption = constants.SOUND_ABSORPTION_COEFFICIENT

    def __init__(self, x1: float, y1: float, x2: float, y2: float, ax: axes.Axes):
        super().__init__(x1, y1, ax)
        self.x2 = x2
        self.y2 = y2

    def draw(self) -> None:
        self.ax.plot([self.x1, self.x2], [self.y1, self.y2], color='black', linewidth=4)
        plt.draw()
