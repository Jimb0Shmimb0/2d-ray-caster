from mathutils import calculate_intersection_of_ray_and_line, distance_to_threshold, decibels_after_x_meters, \
    reflected_sound_in_decibels, reflected_vector
from mathutils import intersection_exits_between_ray_and_line
from typing import List
from matplotlib import pyplot as plt, axes
from constants_and_enums import constants
from constants_and_enums.surface_types import SurfaceType
from .Object import Object
from .Panel import Panel
from .Source import Source
from .Wall import Wall
import numpy as np


class Ray(Object):
    absorption = constants.SOURCE_SOUND

    def __init__(self, x1: float, y1: float, direction_x: float, direction_y: float, db_level: float, ax: axes.Axes, walls: List[Wall], panels: List[Panel], sources: List[Source]):

        if db_level < constants.HEARING_THRESHOLD:
            raise ValueError("Sound ray's dB level is under the hearing threshold")

        super().__init__(x1, y1, ax)
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.walls = walls
        self.sources = sources
        self.panels = panels
        self.db_level = db_level
        self.can_rebound = True
        self.reached_sink = False
        self.candidates = []

        print(" --- Iterating through walls")
        for wall in self.walls:
            if intersection_exits_between_ray_and_line(x1, y1, x1 + direction_x, y1 + direction_y, wall.x1, wall.y1, wall.x2, wall.y2):
                t, u = calculate_intersection_of_ray_and_line(x1, y1, x1 + direction_x, y1 + direction_y, wall.x1, wall.y1, wall.x2, wall.y2)
                print(f"Adding t_and_u: {t, u}")
                self.candidates.append((t, u, SurfaceType.WALL, wall.x2 - wall.x1, wall.y2 - wall.y1))
        print(self.candidates)

        print(" --- Iterating through panels")
        for panel in self.panels:
            if intersection_exits_between_ray_and_line(x1, y1, x1 + direction_x, y1 + direction_y, panel.x1, panel.y1, panel.x2, panel.y2):
                t, u = calculate_intersection_of_ray_and_line(x1, y1, x1 + direction_x, y1 + direction_y, panel.x1, panel.y1, panel.x2, panel.y2)
                self.candidates.append((t, u, SurfaceType.PANEL, panel.x2 - panel.x1, panel.y2 - panel.y1))
        print(self.candidates)
        print(" --- Iterating through sources")
        for source in self.sources:
            if source.is_currently_a_sink:
                for coord in source.detection_line_coordinates:
                    x3, y3, x4, y4 = coord
                    if intersection_exits_between_ray_and_line(x1, y1, x1 + direction_x, y1 + direction_y, x3, y3, x4, y4):
                        t, u = calculate_intersection_of_ray_and_line(x1, y1, x1 + direction_x, y1 + direction_y, x3, y3, x4, y4)
                        self.candidates.append((t, u, SurfaceType.SOURCE, x4 - x3, y4 - y3))
        print(self.candidates)
        print(" --- Sorting")
        self.candidates.sort()
        closest_t, closest_u, surface_type, wall_direction_x, wall_direction_y = self.candidates[0]
        print(f" --- Closest t: {closest_t}")

        direction_vector = np.array([direction_x, direction_y])
        norm = np.linalg.norm(direction_vector)
        unit_direction = direction_vector / norm

        self.x2 = x1 + closest_t * unit_direction[0]
        self.y2 = y1 + closest_t * unit_direction[1]
        print(f"x2: {self.x2}, y2: {self.y2}")
        self.distance_travelled = closest_t * norm

        """self.x2 = x1 + closest_t * direction_x
        self.y2 = y1 + closest_t * direction_y"""
        self.distance_travelled = np.linalg.norm(np.array([self.x2 - x1, self.y2 - y1]))
        self.hitting_surface_type = surface_type
        self.hitting_wall_direction_x = wall_direction_x
        self.hitting_wall_direction_y = wall_direction_y

        if self.hitting_surface_type == SurfaceType.SOURCE:
            self.reached_sink = True
        print(f"Distance_travelled: {self.distance_travelled}")
        print(f"Distance_to_threshold: {distance_to_threshold(db_level)}")
        print(f"Distance_travelled - distance_to_threshold: {self.distance_travelled - distance_to_threshold(db_level)}")
        if self.distance_travelled > distance_to_threshold(db_level):
            print("THRESHOLD REACHED!!!!")
            """direction_vector = np.array([direction_x, direction_y])
            norm_d_vector = np.linalg.norm(direction_vector)
            unit_direction = direction_vector/norm_d_vector"""
            resulting_vector = distance_to_threshold(db_level) * unit_direction

            self.new_direction_x = x1 + resulting_vector[0]
            self.new_direction_y = y1 + resulting_vector[1]
            self.can_rebound = False
            self.hitting_surface_type = None
            self.distance_travelled = distance_to_threshold(db_level)

    def draw(self) -> None:
        print(f"-----------DRAWING QUIVER{self.x1, self.x2, self.x2 - self.x1, self.y2 - self.y1}")

        quiver = self.ax.quiver(self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1, angles='xy', scale_units='xy', scale=1, color='black', width=constants.VECTOR_SIZE)
        plt.draw()
        plt.pause(constants.TICK)

        if self.can_rebound:
            print("can rebound")
            db_at_x2_y2 = decibels_after_x_meters(self.distance_travelled, self.db_level)
            if db_at_x2_y2 > constants.HEARING_THRESHOLD:
                reflected_db = None
                if self.hitting_surface_type == SurfaceType.WALL:
                    reflected_db = reflected_sound_in_decibels(self.db_level, Wall.absorption)
                if self.hitting_surface_type == SurfaceType.PANEL:
                    reflected_db = reflected_sound_in_decibels(self.db_level, Panel.absorption)
                if reflected_db and reflected_db > constants.HEARING_THRESHOLD:
                    reflected_x, reflected_y = reflected_vector(self.direction_x, self.direction_y, self.hitting_wall_direction_x, self.hitting_wall_direction_y)
                    print(f"direction_x: {self.direction_x}, direction_y: {self.direction_y}, reflection_x: {reflected_x}, reflected_y: {reflected_y}")
                    reflected_ray = Ray(self.x2, self.y2, reflected_x, reflected_y, reflected_db, self.ax, self.walls, self.panels, self.sources)
                    reflected_ray.draw()
                    # TODO: Fix this nasty bug in iteration 2
                    if reflected_ray.reached_sink:
                        self.reached_sink = True

        quiver.remove()
        if self.reached_sink:
            quiver = self.ax.quiver(self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1, angles='xy', scale_units='xy', scale=1, color='blue', width=constants.VECTOR_SIZE)








