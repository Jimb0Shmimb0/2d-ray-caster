from matplotlib import axes
from abc import ABC, abstractmethod


class Object(ABC):
    def __init__(self, x1: float, y1: float, x2: float, y2: float, ax: axes.Axes):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.ax = ax

    @abstractmethod
    def draw(self, ax: axes.Axes) -> None:
        pass
