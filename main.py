from Setup import Setup

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
    setup.set_source(4.5, 2.5)
    setup.set_source(0.5, 0.5)

    setup.draw()
    setup.run()

def main():
    config_2()

if __name__ == "__main__":
    main()