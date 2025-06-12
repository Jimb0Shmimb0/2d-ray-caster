from matplotlib import axes, pyplot as plt
import config
from .Object import Object


class Panel(Object):
    """

    Panel class represents a panel used for drawing objects on a matplotlib Axes object.

    :param x1: The x-coordinate of the starting point of the panel.
    :type x1: float
    :param y1: The y-coordinate of the starting point of the panel.
    :type y1: float
    :param x2: The x-coordinate of the ending point of the panel.
    :type x2: float
    :param y2: The y-coordinate of the ending point of the panel.
    :type y2: float
    :param ax: The matplotlib Axes object on which the panel will be drawn.
    :type ax: axes.Axes

    :ivar absorption: The sound absorption coefficient of the panel.
    :vartype absorption: float

    __init__(self, x1: float, y1: float, x2: float, y2: float, ax: axes.Axes)
        Initializes a new Panel object with the provided coordinates and Axes object.

    draw(self) -> None
        Draws the panel on the assigned Axes object by plotting a line between the starting and ending points with a grey color and a thickness of 4.
        This method also redraws the plot.

    """
    absorption = constants.PANEL_SOUND_ABSORPTION_COEFFICIENT

    def __init__(self, x1: float, y1: float, x2: float, y2: float, ax: axes.Axes):
        """
        :param x1: float value representing the x-coordinate of the first point
        :param y1: float value representing the y-coordinate of the first point
        :param x2: float value representing the x-coordinate of the second point
        :param y2: float value representing the y-coordinate of the second point
        :param ax: axes.Axes object representing the matplotlib axes

        """
        super().__init__(x1, y1, ax)
        self.x2 = x2
        self.y2 = y2

    def draw(self) -> None:
        """
        :return: None
        """
        self.ax.plot([self.x1, self.x2], [self.y1, self.y2], color='grey', linewidth=4)
        plt.draw()
