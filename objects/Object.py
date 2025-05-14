from matplotlib import axes
from abc import ABC, abstractmethod


class Object(ABC):
    def __init__(self, x1: float, y1: float, ax: axes.Axes):
        self.x1 = x1
        self.y1 = y1
        self.ax = ax

    @abstractmethod
    def draw(self) -> None:
        pass
