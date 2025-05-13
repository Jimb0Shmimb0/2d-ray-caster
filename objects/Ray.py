from abc import ABC
from matplotlib import axes, pyplot as plt
import constants
import Object


class Ray(Object):
    absorption = constants.SOURCE_SOUND_IN_DECIBELS

    def __init__(self, x1: float, y1: float, x2: float, y2: float):

        # TODO: Change this implementation:
            # Args should be (source_x, source_y, dir_x, dir_y)
            # x2 and y2 based off current distance it has left to travel before sound reaches HEARING_THRESHOLD

        super().__init__(x1, y1, x2, y2)

    def draw(self) -> None:
        # TODO: See above
        self.ax.quiver(self.x1, self.y1, self.x2, self.y2, angles='xy', scale_units='xy', scale=1, color='black')
        plt.draw()
