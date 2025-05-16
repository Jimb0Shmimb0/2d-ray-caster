from utils.mathutils import calculate_intersection_of_ray_and_line, distance_to_threshold, decibels_after_x_meters, \
    reflected_sound_in_decibels, reflected_vector
from utils.mathutils import intersection_exits_between_ray_and_line
from typing import List
from matplotlib import pyplot as plt, axes
import constants
from utils.surface_types import SurfaceType
from .Object import Object
from .Panel import Panel
from .Source import Source
from .Wall import Wall
import numpy as np


class Ray(Object):
    absorption = constants.SOURCE_SOUND

    def __init__(self, x1: float, y1: float, direction_x: float, direction_y: float, db_level: float, num_panels_left_to_place: int, ax: axes.Axes, walls: List[Wall], panels: List[Panel], sources: List[Source], setup):

        if db_level < constants.HEARING_THRESHOLD:
            raise ValueError("Sound ray's dB level is under the hearing threshold")

        super().__init__(x1, y1, ax)
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.db_level = db_level
        self.num_panels_left_to_place = num_panels_left_to_place
        self.can_rebound = True
        self.reached_sink = False

        self.walls = walls
        self.sources = sources
        self.panels = panels
        self.candidates = []
        self.setup = setup

        closest_t, closest_u, surface_type, wall_direction_x, wall_direction_y, object_ref = self._get_closest_ray_intersection()

        self.hitting_surface_type = surface_type
        self.hitting_surface_ref = object_ref
        if self.hitting_surface_type == SurfaceType.SOURCE:
            self.reached_sink = True


        unit_direction, norm = self._get_unit_direction_and_norm()
        self.x2 = x1 + closest_t * unit_direction[0]
        self.y2 = y1 + closest_t * unit_direction[1]
        self.distance_travelled = closest_t * norm

        # self.distance_travelled = np.linalg.norm(np.array([self.x2 - x1, self.y2 - y1]))

        self.hitting_wall_direction_x = wall_direction_x
        self.hitting_wall_direction_y = wall_direction_y

        if self.distance_travelled > distance_to_threshold(db_level):
            resulting_vector = distance_to_threshold(db_level) * unit_direction

            self.x2 = x1 + resulting_vector[0]
            self.y2 = y1 + resulting_vector[1]
            self.can_rebound = False
            self.reached_sink = False
            self.hitting_surface_type = None
            self.distance_travelled = distance_to_threshold(db_level)

    def draw(self) -> None:

        # Draw the vector
        quiver = self.ax.quiver(self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1, angles='xy', scale_units='xy', scale=1, color='black', width=constants.VECTOR_SIZE)
        plt.draw()
        plt.pause(constants.TICK) # Pause for a tick before moving on

        # If the vector
        if self.can_rebound:

            db_at_x2_y2 = decibels_after_x_meters(self.distance_travelled, self.db_level)

            if db_at_x2_y2 > constants.HEARING_THRESHOLD:
                reflected_db = None
                if self.hitting_surface_type == SurfaceType.WALL:
                    reflected_db = min(self.db_level, reflected_sound_in_decibels(db_at_x2_y2, Wall.absorption))
                if self.hitting_surface_type == SurfaceType.PANEL:
                    reflected_db = min(self.db_level, reflected_sound_in_decibels(db_at_x2_y2, Panel.absorption))
                if reflected_db and reflected_db > constants.HEARING_THRESHOLD:
                    reflected_x, reflected_y = reflected_vector(self.direction_x, self.direction_y, self.hitting_wall_direction_x, self.hitting_wall_direction_y)
                    reflected_ray = Ray(self.x2, self.y2, reflected_x, reflected_y, reflected_db, self.num_panels_left_to_place - 1, self.ax, self.walls, self.panels, self.sources, self.setup)
                    reflected_ray.draw()
                    if reflected_ray.reached_sink:
                        self.reached_sink = True

        quiver.remove()
        if self.reached_sink:
            self.ax.quiver(self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1, angles='xy', scale_units='xy', scale=1, color='blue', width=constants.VECTOR_SIZE)
            if self.num_panels_left_to_place > 0 and self.hitting_surface_type == SurfaceType.WALL:
                print("Hit a wall and reached sink")
                array_index = self.hitting_surface_ref.get_segment_index_for_point(self.x2, self.y2)
                print(array_index)
                print(self.hitting_surface_ref.segments[array_index]['visited'])
                if not self.hitting_surface_ref.segments[array_index]['visited']:
                    panel_x1 = self.hitting_surface_ref.segments[array_index]['x1']
                    panel_x2 = self.hitting_surface_ref.segments[array_index]['x2']
                    panel_y1 = self.hitting_surface_ref.segments[array_index]['y1']
                    panel_y2 = self.hitting_surface_ref.segments[array_index]['y2']
                    print((panel_x1, panel_y1, panel_x2, panel_y2))
                    self.setup.panel_addition_queue.append((panel_x1, panel_y1, panel_x2, panel_y2))
                    self.hitting_surface_ref.segments[array_index]['visited'] = True



        # TODO: Implement logic to add panels at the first rebound, second rebound, etc.
        #  SINKS ALSO NEED TO RECORD SOUND RECEIVED! Refer to design doc

        # TODO: Type hinting and comments please!

    # Private methods
    def _get_closest_ray_intersection(self) -> tuple:
        for wall in self.walls:
            if intersection_exits_between_ray_and_line(self.x1, self.y1, self.x1 + self.direction_x, self.y1 + self.direction_y, wall.x1, wall.y1, wall.x2, wall.y2):
                t, u = calculate_intersection_of_ray_and_line(self.x1, self.y1, self.x1 + self.direction_x, self.y1 + self.direction_y, wall.x1, wall.y1, wall.x2, wall.y2)
                if not wall.is_point_on_visited_segment(self.x1 + t * self._get_unit_direction_and_norm()[0][0], self.y1 + t * self._get_unit_direction_and_norm()[0][0]):
                    self.candidates.append((t, u, SurfaceType.WALL, wall.x2 - wall.x1, wall.y2 - wall.y1, wall))


        for panel in self.panels:
            if intersection_exits_between_ray_and_line(self.x1, self.y1, self.x1 + self.direction_x, self.y1 + self.direction_y, panel.x1, panel.y1, panel.x2, panel.y2):
                t, u = calculate_intersection_of_ray_and_line(self.x1, self.y1, self.x1 + self.direction_x, self.y1 + self.direction_y, panel.x1, panel.y1, panel.x2, panel.y2)
                self.candidates.append((t, u, SurfaceType.PANEL, panel.x2 - panel.x1, panel.y2 - panel.y1, panel))

        for source in self.sources:
            if source.is_currently_a_sink:
                for coord in source.detection_line_coordinates:
                    x3, y3, x4, y4 = coord
                    if intersection_exits_between_ray_and_line(self.x1, self.y1, self.x1 + self.direction_x, self.y1 + self.direction_y, x3, y3, x4, y4):
                        t, u = calculate_intersection_of_ray_and_line(self.x1, self.y1, self.x1 + self.direction_x, self.y1 + self.direction_y, x3, y3, x4, y4)
                        self.candidates.append((t, u, SurfaceType.SOURCE, x4 - x3, y4 - y3, source))

        self.candidates.sort(key=lambda tup: tup[0])
        closest_t, closest_u, surface_type, wall_direction_x, wall_direction_y, object_ref = self.candidates[0]

        return closest_t, closest_u, surface_type, wall_direction_x, wall_direction_y, object_ref

    def _get_unit_direction_and_norm(self):
        direction_vector = np.array([self.direction_x, self.direction_y])
        norm = np.linalg.norm(direction_vector)
        unit_direction = direction_vector / norm
        return unit_direction, norm





