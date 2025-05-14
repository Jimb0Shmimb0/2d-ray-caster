from mathutils import calculate_intersection_of_ray_and_line
from mathutils import intersection_exits_between_ray_and_line
from typing import List
from matplotlib import pyplot as plt, axes
from constants_and_enums import constants
from constants_and_enums.surface_types import SurfaceType
from .Object import Object
from .Panel import Panel
from .Source import Source
from .Wall import Wall


class Ray(Object):
    absorption = constants.SOURCE_SOUND

    def __init__(self, x1: float, y1: float, direction_x: float, direction_y: float, ax: axes.Axes, walls: List[Wall], panels: List[Panel], sources: List[Source]):

        super().__init__(x1, y1, ax)

        self.candidates = []

        for wall in walls:
            if intersection_exits_between_ray_and_line(x1, y1, x1 + direction_x, y1 + direction_y, wall.x1, wall.y1, wall.x2, wall.y2):
                t_and_u = calculate_intersection_of_ray_and_line(x1, y1, x1 + direction_x, y1 + direction_y, wall.x1, wall.y1, wall.x2, wall.y2)
                self.candidates.append((t_and_u, SurfaceType.WALL))

        for panel in panels:
            if intersection_exits_between_ray_and_line(x1, y1, x1 + direction_x, y1 + direction_y, panel.x1, panel.y1, panel.x2, panel.y2):
                t_and_u = calculate_intersection_of_ray_and_line(x1, y1, x1 + direction_x, y1 + direction_y, panel.x1, panel.y1, panel.x2, panel.y2)
                self.candidates.append((t_and_u, SurfaceType.PANEL))

        for source in sources:
            for coord in source.detection_line_coordinates:
                x3, y3, x4, y4 = coord
                if intersection_exits_between_ray_and_line(x1, y1, x1 + direction_x, y1 + direction_y, x3, y3, x4, y4):
                    t_and_u = calculate_intersection_of_ray_and_line(x1, y1, x1 + direction_x, y1 + direction_y, x3, y3, x4, y4)
                    self.candidates.append((t_and_u, SurfaceType.SOURCE))

        self.candidates.sort()

        # TODO: Add logic that picks the correct t values


    def draw(self) -> None:
        # TODO: See above
        self.ax.quiver(self.x1, self.y1, self.x2, self.y2, angles='xy', scale_units='xy', scale=1, color='black')
        plt.draw()

    def cast(self):
        pass
