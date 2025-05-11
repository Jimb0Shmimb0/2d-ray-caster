import matplotlib.pyplot as plt


class Boundary:

    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self) -> None:
        """self.ax.quiver(self.x1, self.y1, self.x2, self.y2, angles='xy', scale_units='xy', scale=1, color='black')
        plt.draw()"""