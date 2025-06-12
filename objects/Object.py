from matplotlib import axes
from abc import ABC, abstractmethod


class Object(ABC):
    """
    Abstract base class for objects to be drawn on a matplotlib axes.

    :ivar x1: The x-coordinate of the object.
    :type x1: float

    :ivar y1: The y-coordinate of the object.
    :type y1: float

    :ivar ax: The matplotlib Axes object to draw the object on.
    :type ax: axes.Axes
    """
    def __init__(self, x1: float, y1: float, ax: axes.Axes):
        """
        :param x1:
        :param y1:
        :param ax:
        :type x1: float
        :type y1: float
        :type ax: axes.Axes

        """
        self.x1 = x1
        self.y1 = y1
        self.ax = ax

    @abstractmethod
    def draw(self) -> None:
        """
        :return:
            This method is used to draw an object
        """
        pass
