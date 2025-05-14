from Setup import Setup

def main():
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
    setup.set_source(2.25,0.5)

    setup.draw()
    setup.run()

if __name__ == "__main__":
    main()