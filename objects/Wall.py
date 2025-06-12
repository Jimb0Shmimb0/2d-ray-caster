import math

from matplotlib import axes, pyplot as plt
import config
from .Object import Object


class Wall(Object):
    absorption = constants.WALL_SOUND_ABSORPTION_COEFFICIENT

    def __init__(self, x1: float, y1: float, x2: float, y2: float, ax: axes.Axes):
        super().__init__(x1, y1, ax)
        self.x2 = x2
        self.y2 = y2
        self.segments = []
        self._split_into_segments()

    def draw(self) -> None:
        self.ax.plot([self.x1, self.x2], [self.y1, self.y2], color='black')
        plt.draw()

    def get_segment_index_for_point(self, px: float, py: float) -> int:
        # Determine which segment of the wall the point lies on

        for index, segment in enumerate(self.segments):
            if self._point_lies_on_segment(segment['x1'], segment['y1'], segment['x2'], segment['y2'], px, py):
                return index

        return -1  # Point is not on any segment

    def is_point_on_visited_segment(self, px: float, py: float) -> bool:
        for segment in self.segments:
            if self._point_lies_on_segment(segment['x1'], segment['y1'], segment['x2'], segment['y2'], px, py):
                return segment['visited']
        return False

    def _point_lies_on_segment(self, x1, y1, x2, y2, px, py, tolerance=1e-6):
        # Vector along the segment
        direction_x = x2 - x1
        direction_y = y2 - y1
        length_squared = direction_x ** 2 + direction_y ** 2

        if length_squared == 0:
            return False

        # Project the point onto the segment and check bounds
        t = ((px - x1) * direction_x + (py - y1) * direction_y) / length_squared

        if t < 0 or t > 1:
            return False

        # Get the projected point
        projected_x = x1 + t * direction_x
        projected_y = y1 + t * direction_y

        # Check if point is close enough to the segment line
        distance_squared = (px - projected_x) ** 2 + (py - projected_y) ** 2
        return distance_squared <= tolerance ** 2

    def _split_into_segments(self):
        # Take the direction that the wall is travelling

        direction_x = self.x2 - self.x1
        direction_y = self.y2 - self.y1
        length = math.hypot(direction_x, direction_y)

        number_of_segments = int(length // constants.WALL_SEGMENTATION_LENGTH)
        unit_direction_x = direction_x / length
        unit_direction_y = direction_y / length

        for i in range(number_of_segments):
            segment_x1 = self.x1 + i * constants.WALL_SEGMENTATION_LENGTH * unit_direction_x
            segment_y1 = self.y1 + i * constants.WALL_SEGMENTATION_LENGTH * unit_direction_y
            segment_x2 = self.x1 + (i + 1) * constants.WALL_SEGMENTATION_LENGTH * unit_direction_x
            segment_y2 = self.y1 + (i + 1) * constants.WALL_SEGMENTATION_LENGTH * unit_direction_y
            self.segments.append({
                'x1': segment_x1,
                'y1': segment_y1,
                'x2': segment_x2,
                'y2': segment_y2,
                'visited': False
            })

        # Handle leftover segment
        if length % constants.WALL_SEGMENTATION_LENGTH != 0:
            last_segment_x = self.x1 + number_of_segments * constants.WALL_SEGMENTATION_LENGTH * unit_direction_x
            last_segment_y = self.y1 + number_of_segments * constants.WALL_SEGMENTATION_LENGTH * unit_direction_y
            self.segments.append({
                'x1': last_segment_x,
                'y1': last_segment_y,
                'x2': self.x2,
                'y2': self.y2,
                'visited': False
            })
