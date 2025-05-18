import math
import matplotlib.pyplot as plt
import constants
from objects.Panel import Panel
from objects.Ray import Ray
from objects.Source import Source
from objects.Wall import Wall


class Setup:
    INF = math.inf

    def __init__(self):
        self.ax = plt.subplot()
        self.walls = []
        self.sources = []
        self.panels = []
        self.panel_addition_queue = []
        self.return_data_iteration_1 = []
        self.return_data_iteration_2 = []

        # Counting
        self.obj_count = 0

        # For window sizing
        self.X_MAX = -Setup.INF
        self.Y_MAX = -Setup.INF
        self.X_MIN = Setup.INF
        self.Y_MIN = Setup.INF

        # Bools
        self.drawn = False

    def set_wall(self, x1: float, y1: float, x2: float, y2: float):
        self._resize_window_with_line(x1, y1, x2, y2)
        self.walls.append(Wall(x1, y1, x2, y2, self.ax))
        self.obj_count += 1

    def set_panel(self, x1: float, y1: float, x2: float, y2: float):
        self._resize_window_with_line(x1, y1, x2, y2)
        self.panels.append(Panel(x1, y1, x2, y2, self.ax))
        self.obj_count += 1

    def set_source(self, x1: float, y1: float):
        self._resize_window_with_circle(x1, y1)
        self.sources.append(Source(x1, y1, self.ax))
        self.obj_count += 1



    def run(self):
        # Draw the plot and the first set of rays
        self._draw()
        self._draw_rays()
        print(self.panel_addition_queue)

        self._get_data_iteration_1()

        # If panels have been added, apply them in the new configuration.
        self._apply_panels()

        input("Enter to run new configuration")

        # Clear the plot, redraw the graph with new panels, draw the second set of rays then record the data
        self.ax.cla()
        self._draw()
        self._draw_rays()

        self._get_data_iteration_2()
        input("Enter to end")
        return self.return_data_iteration_1, self.return_data_iteration_2, self.panel_addition_queue

    # Private methods
    def _draw(self) -> None:

        if self.obj_count > 0:
            #self.ax.set_axis_off()

            # Set limits and aspect
            self.ax.set_xlim(self.X_MIN - constants.WINDOW_MARGIN, self.X_MAX + constants.WINDOW_MARGIN)
            self.ax.set_ylim(self.Y_MIN - constants.WINDOW_MARGIN, self.Y_MAX + constants.WINDOW_MARGIN)
            self.ax.set_aspect('equal')

            self.ax.axhline(y=self.Y_MIN - constants.WINDOW_MARGIN, color='lightgray', linewidth=1, linestyle='--')
            self.ax.axvline(x=self.X_MIN - constants.WINDOW_MARGIN, color='lightgray', linewidth=1, linestyle='--')
            self.ax.set_xticks(range(math.floor(self.X_MIN - constants.WINDOW_MARGIN), math.ceil(self.X_MAX + constants.WINDOW_MARGIN) + 1, 1))
            self.ax.set_yticks(range(math.floor(self.Y_MIN - constants.WINDOW_MARGIN), math.ceil(self.Y_MAX + constants.WINDOW_MARGIN) + 1, 1))

            [wall.draw() for wall in self.walls] if self.walls else None
            [panel.draw() for panel in self.panels] if self.panels else None
            [source.draw() for source in self.sources] if self.sources else None

            plt.draw()
            self.drawn = True
            return

    def _draw_rays(self) -> None:
        for source in self.sources:
            source.is_currently_a_sink = False
            for i in range(constants.NUM_RAYS):
                angle = i * ((2 * math.pi) / constants.NUM_RAYS)
                ray = Ray(source.x1 + source.radius * math.cos(angle), source.y1 + source.radius * math.sin(angle),
                          math.cos(angle), math.sin(angle), constants.SOURCE_SOUND,
                          constants.PANELS_TO_PLACE_AFTER_EACH_REBOUND, self.ax, self.walls, self.panels, self.sources,
                          self)
                ray.draw()
            source.is_currently_a_sink = True

    def _resize_window_with_line(self, x1: float, y1: float, x2: float, y2: float) -> None:
        if min(x1, x2) < self.X_MIN:
            self.X_MIN = min(x1, x2)
        if max(x1, x2) > self.X_MAX:
            self.X_MAX = max(x1, x2)
        if min(y1, y2) < self.Y_MIN:
            self.Y_MIN = min(y1, y1)
        if max(y1, y2) > self.Y_MAX:
            self.Y_MAX = max(y1, y2)

    def _resize_window_with_circle(self, x1: float, y1: float) -> None:
        if x1 - constants.SOURCE_CIRCLE_RADIUS < self.X_MIN:
            self.X_MIN = x1 - constants.SOURCE_CIRCLE_RADIUS
        if x1 + constants.SOURCE_CIRCLE_RADIUS > self.X_MAX:
            self.X_MAX = x1 + constants.SOURCE_CIRCLE_RADIUS
        if y1 - constants.SOURCE_CIRCLE_RADIUS < self.Y_MIN:
            self.Y_MIN = y1 - constants.SOURCE_CIRCLE_RADIUS
        if y1 + constants.SOURCE_CIRCLE_RADIUS > self.Y_MAX:
            self.Y_MAX = y1 + constants.SOURCE_CIRCLE_RADIUS

    def _apply_panels(self) -> None:
        if self.panel_addition_queue:
            for panel_x1, panel_y1, panel_x2, panel_y2 in self.panel_addition_queue:
                self.set_panel(panel_x1, panel_y1, panel_x2, panel_y2)

        [panel.draw() for panel in self.panels] if self.panels else None
        plt.draw()

    def _get_data_iteration_1(self) -> None:
        for source in self.sources:
            self.return_data_iteration_1.append((source.x1, source.y1, source.sound_record_array))
            source.sound_record_array.clear()

    def _get_data_iteration_2(self) -> None:
        for source in self.sources:
            self.return_data_iteration_2.append((source.x1, source.y1, source.sound_record_array))




