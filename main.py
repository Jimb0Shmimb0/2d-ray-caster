from setup.Setup import Setup

def config_1():
    setup = Setup()

    # Define walls
    setup.set_wall(-3, 0, -3, 2)
    setup.set_wall(-3, 0, 3, 0)
    setup.set_wall(-3, 2, 3, 2)
    setup.set_wall(3, 0, 3, 2)

    setup.set_wall(-4, -1, -4, 3)
    setup.set_wall(-4, -1, 4, -1)
    setup.set_wall(-4, 3, 4, 3)
    setup.set_wall(4, -1, 4, 3)

    setup.set_wall(-1.5, 1, 1.5, 1)

    setup.set_source(-2.25, 1.5)
    setup.set_source(2.25, 0.5)

    setup.draw()
    setup.run()

def config_2():
    setup = Setup()

    # Outer jagged enclosure
    setup.set_wall(-6, -3, -2, -3)
    setup.set_wall(-2, -3, -1, -2)
    setup.set_wall(-1, -2, 1, -2)
    setup.set_wall(1, -2, 2, -3)
    setup.set_wall(2, -3, 5, -3)
    setup.set_wall(5, -3, 5, 3)
    setup.set_wall(5, 3, 3, 4)
    setup.set_wall(3, 4, 0, 3.5)
    setup.set_wall(0, 3.5, -2, 4.2)
    setup.set_wall(-2, 4.2, -5, 3)
    setup.set_wall(-5, 3, -6, 0)
    setup.set_wall(-6, 0, -6, -3)

    # Internal triangle structure
    setup.set_wall(-1, 0, 1, 1)
    setup.set_wall(1, 1, 0, 2.5)
    setup.set_wall(0, 2.5, -1, 0)

    # Tiny vertical divider near bottom
    setup.set_wall(3, -2, 3, -1)

    # Sources in different regions
    setup.set_source(-5.5, -2.5)
    setup.set_source(2.5, 2.5)

    setup.draw()
    setup.run()

def config_3():
    setup = Setup()
    # Outer boundary (rectangle)
    setup.set_wall(-6, -3, 6, -3)
    setup.set_wall(6, -3, 6, 4)
    setup.set_wall(6, 4, -6, 4)
    setup.set_wall(-6, 4, -6, -3)

    # Internal walls – forming a double room with some angled passages
    setup.set_wall(-2, -3, -2, 2)
    setup.set_wall(-2, 2, 0, 2)
    setup.set_wall(0, 2, 1.5, 1)
    setup.set_wall(1.5, 1, 3, 2.5)
    setup.set_wall(3, 2.5, 4, 2.5)
    setup.set_wall(4, 2.5, 4, -1)
    setup.set_wall(4, -1, 2, -1)
    setup.set_wall(2, -1, 1, -2)
    setup.set_wall(1, -2, -1, -1)

    # Sources inside the rooms
    setup.set_source(-5, 0)
    setup.set_source(2, 0)

    setup.draw()
    setup.run()

def config_4():
    setup = Setup()

    # Outer bounding rectangle (scaled from -6..6 to -12..12 and -2..2 to -4..4)
    setup.set_wall(-12, -4, 12, -4)
    setup.set_wall(12, -4, 12, 4)
    setup.set_wall(12, 4, -12, 4)
    setup.set_wall(-12, 4, -12, -4)

    # Vertical dividers (scaled x = -2, 2 → -4, 4)
    setup.set_panel(-1.5, -2, -1.5, 2)
    setup.set_panel(1.5, -2, 1.5, 2)

    # Horizontal divider (scaled y = 0 → 0)
    setup.set_panel(-4.5, 0, 4.5, 0)

    # Sources in all 6 cells (scaled positions)
    setup.set_source(-3, 1)  # top-left
    setup.set_source(0, 1)  # top-center
    setup.set_source(3, 1)  # top-right
    setup.set_source(-3, -1)  # bottom-left
    setup.set_source(0, -1)  # bottom-center
    setup.set_source(3, -1)  # bottom-right

    setup.draw()
    setup.run()

def main():
    number_of_configurations = 4
    choice = input(f"Choose configuration (1 - {number_of_configurations}): ").strip()
    configs = {"1": config_1, "2": config_2, "3": config_3, "4": config_4}
    configs.get(choice, config_1)()

if __name__ == "__main__":
    main()