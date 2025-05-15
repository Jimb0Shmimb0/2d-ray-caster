import math

import matplotlib.pyplot as plt
from constants_enums_utils import constants
from constants_enums_utils.constants import INF
from objects.Panel import Panel
from objects.Ray import Ray
from objects.Source import Source
from objects.Wall import Wall


class Setup:

    def __init__(self):
        self.ax = plt.subplot()
        self.walls = []
        self.sources = []
        self.panels = []

        # Counting
        self.obj_count = 0

        # For window sizing
        self.X_MAX = -INF
        self.Y_MAX = -INF
        self.X_MIN = INF
        self.Y_MIN = INF

        # Bools
        self.drawn = False

    def set_wall(self, x1: float, y1: float, x2: float, y2: float):
        self.resize_window_with_line(x1, y1, x2, y2)
        self.walls.append(Wall(x1, y1, x2, y2, self.ax))
        self.obj_count += 1

    def set_panel(self, x1: float, y1: float, x2: float, y2: float):
        self.resize_window_with_line(x1, y1, x2, y2)
        self.panels.append(Panel(x1, y1, x2, y2, self.ax))
        self.obj_count += 1

    def set_source(self, x1: float, y1: float):
        self.resize_window_with_circle(x1, y1)
        self.sources.append(Source(x1, y1, self.ax))
        self.obj_count += 1

    def draw(self) -> None:

        if self.obj_count > 0:
            self.ax.set_axis_off()

            # Set limits and aspect
            self.ax.set_xlim(self.X_MIN - constants.WINDOW_MARGIN, self.X_MAX + constants.WINDOW_MARGIN)
            self.ax.set_ylim(self.Y_MIN - constants.WINDOW_MARGIN, self.Y_MAX + constants.WINDOW_MARGIN)
            self.ax.set_aspect('equal')

            [wall.draw() for wall in self.walls] if self.walls else None
            [panel.draw() for panel in self.panels] if self.panels else None
            [source.draw() for source in self.sources] if self.sources else None

            plt.draw()
            plt.pause(1)
            self.drawn = True
            return

    def run(self):

        if self.drawn:
            for source in self.sources:
                source.is_currently_a_sink = False
                for i in range(constants.NUM_RAYS):
                    angle = i * ((2 * math.pi) / constants.NUM_RAYS)
                    ray = Ray(source.x1 + source.radius * math.cos(angle), source.y1 + source.radius * math.sin(angle), math.cos(angle), math.sin(angle), constants.SOURCE_SOUND, self.ax, self.walls, self.panels, self.sources)
                    ray.draw()
                source.is_currently_a_sink = True
            plt.show()

    ####
    # PRIVATE
    ####
    def resize_window_with_line(self, x1: float, y1: float, x2: float, y2: float) -> None:
        if min(x1, x2) < self.X_MIN:
            self.X_MIN = min(x1, x2)
        if max(x1, x2) > self.X_MAX:
            self.X_MAX = max(x1, x2)
        if min(y1, y2) < self.Y_MIN:
            self.Y_MIN = min(y1, y1)
        if max(y1, y2) > self.Y_MAX:
            self.Y_MAX = max(y1, y2)

    def resize_window_with_circle(self, x1: float, y1: float) -> None:
        if x1 - constants.SOURCE_CIRCLE_RADIUS < self.X_MIN:
            self.X_MIN = x1 - constants.SOURCE_CIRCLE_RADIUS
        if x1 + constants.SOURCE_CIRCLE_RADIUS > self.X_MAX:
            self.X_MAX = x1 + constants.SOURCE_CIRCLE_RADIUS
        if y1 - constants.SOURCE_CIRCLE_RADIUS < self.Y_MIN:
            self.Y_MIN = y1 - constants.SOURCE_CIRCLE_RADIUS
        if y1 + constants.SOURCE_CIRCLE_RADIUS > self.Y_MAX:
            self.Y_MAX = y1 + constants.SOURCE_CIRCLE_RADIUS




