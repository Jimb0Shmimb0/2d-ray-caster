from matplotlib import axes, pyplot as plt
import matplotlib.patches as patches
import constants
import Object


class Source(Object):
    absorption = constants.WALL_ABSORPTION

    def __init__(self, x1: float, y1: float, x2: float, y2: float, ax: axes.Axes):
        super().__init__(x1, y1, x2, y2, ax)

    def draw(self) -> None:
        self.ax.add_patch(patches.Circle((0, 0), radius=1.5, fill=False, edgecolor='blue', linewidth=2))
        self.ax.plot([self.x1, self.x1 + self.x2], [self.y1, self.y1 + self.y2], color='black')
        plt.draw()
