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
    # Enclosing boundary — irregular polygon-like outer walls
    setup.set_wall(-8, -5, 8, -5)
    setup.set_wall(8, -5, 8, 6)
    setup.set_wall(8, 6, -7, 6)
    setup.set_wall(-7, 6, -8, 4)
    setup.set_wall(-8, 4, -8, -5)

    # Interior madness

    # Central cross chaos
    setup.set_wall(-2, -1, 2, -1)
    setup.set_wall(0, -3, 0, 2)
    setup.set_wall(-2, 1, 2, 1)
    setup.set_wall(-1, -3, -1, -1)
    setup.set_wall(1, -1, 1, 3)

    # Jagged zigzag snake in bottom left
    setup.set_wall(-7, -4, -6, -3)
    setup.set_wall(-6, -3, -7, -2)
    setup.set_wall(-7, -2, -6, -1)
    setup.set_wall(-6, -1, -7, 0)

    # Triangular dead zone
    setup.set_wall(3, 1, 5, 2)
    setup.set_wall(5, 2, 4, 4)
    setup.set_wall(4, 4, 3, 1)

    # Random floating walls
    setup.set_wall(6, -2, 7, 1)
    setup.set_wall(-3, 3, -1, 4)
    setup.set_wall(1.5, 4.5, 3, 5)
    setup.set_wall(-4, 5, -3.5, 3)

    # Left-top blocking box
    setup.set_wall(-6, 3, -5, 5)
    setup.set_wall(-5, 5, -4, 4)
    setup.set_wall(-4, 4, -6, 3)

    # Narrow tunnel to nowhere
    setup.set_wall(6, 4.5, 7.5, 4.8)
    setup.set_wall(7.5, 4.8, 6.5, 5.5)

    # Sources scattered for max chaos
    setup.set_source(-7.5, -1.5)
    setup.set_source(0.5, 0.5)
    setup.set_source(6.5, 1.5)
    setup.set_source(-2.5, 4.5)

    setup.draw()
    setup.run()

def main():
    number_of_configurations = 4
    choice = input(f"Choose configuration (1 - {number_of_configurations}): ").strip()
    configs = {"1": config_1, "2": config_2, "3": config_3, "4": config_4}
    configs.get(choice, config_1)()

if __name__ == "__main__":
    main()