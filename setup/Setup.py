import math
import matplotlib.pyplot as plt
import config
from objects.Panel import Panel
from objects.Ray import Ray
from objects.Source import Source
from objects.Wall import Wall


class Setup:
    """
    Setup class for setting up simulation environment.

    Attributes:
        INF: float - Positive infinity value.

    Methods:
        __init__: Initialize Setup object with default attributes.
        set_wall: Add a wall to the setup.
        set_panel: Add a panel to the setup.
        set_source: Add a source to the setup.
        run: Run the simulation and display output.

    Private Methods:
        _draw: Draw the setup elements on the plot.
        _draw_rays: Draw rays emitted from sources.
        _resize_window_with_line: Adjust window boundaries with a line input.
        _resize_window_with_circle: Adjust window boundaries with a circular input.
        _apply_panels: Apply panels to the setup.
        _get_data_iteration_1: Get data from iteration 1.
        _get_data_iteration_2: Get data from iteration 2.
    """
    INF = math.inf

    def __init__(self):
        """
        Initialize the Setup object.

        Parameters:
            None

        Return type:
            None
        """
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
        """
        :param x1: x-coordinate of the starting point of the wall
        :param y1: y-coordinate of the starting point of the wall
        :param x2: x-coordinate of the ending point of the wall
        :param y2: y-coordinate of the ending point of the wall
        :return: None
        """
        # Add a wall to the setup. Resize the window appropriately, append it to the list of walls
        self._resize_window_with_line(x1, y1, x2, y2)
        self.walls.append(Wall(x1, y1, x2, y2, self.ax))
        self.obj_count += 1

    def set_panel(self, x1: float, y1: float, x2: float, y2: float):
        """
        :param x1: The x-coordinate of the top-left corner of the panel.
        :param y1: The y-coordinate of the top-left corner of the panel.
        :param x2: The x-coordinate of the bottom-right corner of the panel.
        :param y2: The y-coordinate of the bottom-right corner of the panel.
        :return: None

        """
        # Add a panel to the setup. Resize the window appropriately, append it to the list of panels.
        self._resize_window_with_line(x1, y1, x2, y2)
        self.panels.append(Panel(x1, y1, x2, y2, self.ax))
        self.obj_count += 1

    def set_source(self, x1: float, y1: float):
        """
        :param x1: The x-coordinate of the source
        :param y1: The y-coordinate of the source
        :return: None

        """
        # Add
        self._resize_window_with_circle(x1, y1)
        self.sources.append(Source(x1, y1, self.ax))
        self.obj_count += 1

    def run(self):
        """
        Run the setup


        :return: A tuple containing the data from running two iterations and the list of panels that have been added to
        the setup
        """
        # Draw the plot and the first set of rays
        self._draw()
        self._draw_rays()
        print(self.panel_addition_queue)

        self._get_data_iteration_1()
        plt.show()
        return self.return_data_iteration_1, self.return_data_iteration_2, self.panel_addition_queue

    # Private methods
    def _draw(self) -> None:
        """
        Draw the setup, including axes, all panels, walls and sources

        :return: None
        """
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
        """
        Draws rays from each source point in the simulation environment.

        :return: None
        """
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
        """
        Given a new line added to the setup, resize the window

        :param x1: The x-coordinate of the first point
        :param y1: The y-coordinate of the first point
        :param x2: The x-coordinate of the second point
        :param y2: The y-coordinate of the second point
        :return: None

        """
        if min(x1, x2) < self.X_MIN:
            self.X_MIN = min(x1, x2)
        if max(x1, x2) > self.X_MAX:
            self.X_MAX = max(x1, x2)
        if min(y1, y2) < self.Y_MIN:
            self.Y_MIN = min(y1, y1)
        if max(y1, y2) > self.Y_MAX:
            self.Y_MAX = max(y1, y2)

    def _resize_window_with_circle(self, x1: float, y1: float) -> None:
        """
        Given a new circle added to the setup, resize the window

        :param x1: The x-coordinate of the center of the circle to resize the window with.
        :param y1: The y-coordinate of the center of the circle to resize the window with.
        :return: None
        """
        if x1 - constants.SOURCE_CIRCLE_RADIUS < self.X_MIN:
            self.X_MIN = x1 - constants.SOURCE_CIRCLE_RADIUS
        if x1 + constants.SOURCE_CIRCLE_RADIUS > self.X_MAX:
            self.X_MAX = x1 + constants.SOURCE_CIRCLE_RADIUS
        if y1 - constants.SOURCE_CIRCLE_RADIUS < self.Y_MIN:
            self.Y_MIN = y1 - constants.SOURCE_CIRCLE_RADIUS
        if y1 + constants.SOURCE_CIRCLE_RADIUS > self.Y_MAX:
            self.Y_MAX = y1 + constants.SOURCE_CIRCLE_RADIUS

    def _apply_panels(self) -> None:
        """
        Apply panels to the setup

        :return: None
        """
        if self.panel_addition_queue:
            for panel_x1, panel_y1, panel_x2, panel_y2 in self.panel_addition_queue:
                self.set_panel(panel_x1, panel_y1, panel_x2, panel_y2)

        [panel.draw() for panel in self.panels] if self.panels else None
        plt.draw()

    def _get_data_iteration_1(self) -> None:
        """
        Get recorded sound levels for each source in interation 1
        :return: None
        """
        for source in self.sources:
            self.return_data_iteration_1.append((source.x1, source.y1, source.sound_record_array))
            # TODO: Fix this. Also, generalise

    def _get_data_iteration_2(self) -> None:
        """
        Get recorded sound levels for each source in interation 1
        :return: None
        """
        for source in self.sources:
            self.return_data_iteration_2.append((source.x1, source.y1, source.sound_record_array))
            # TODO: Fix this. Also, generalise



