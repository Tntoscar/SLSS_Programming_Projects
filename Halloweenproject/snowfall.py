# snowfall
# Author: Oscar
# 2021 Version

import random
import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (255,   0,   0)
GREEN = (0, 255,   0)
BLUE = (0,   0, 255)
BGCOLOUR = (100, 100, 255)

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Snowfall "


class Snowflake:
    """Represents a snow flake on screen

    Attributes:
        size: the radius of the snow flake in px
        x, y: coordinates of random area on the screen
        y_vel: falling velocity in px/sec
        colour = (r, g,b)
    """
    def __init__(self):
        self.size = 2
        self.coords = [
            random.randrange(0, SCREEN_WIDTH),
            random.randrange(0, SCREEN_HEIGHT)
        ]
        self.y_vel = (random.randrange(2, 4))
        self.colour = WHITE

    def update(self):
        """Update the location of the snow"""
        # Changes the y portion of the coords
        self.coords[1] += self.y_vel

        # reset positions of snowflake if it reaches bottom
        if self.coords[1] > SCREEN_HEIGHT:
            coords = [
                random.randrange(0, SCREEN_WIDTH),
                random.randrange(-25, 0)
            ]


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_snowflakes = 250
    snowflake = []

    # create snow flake in fore background
    for i in range(num_snowflakes):
        close_snowflake = Snowflake()
        close_snowflake.size = 6
        close_snowflake.y_vel = 2
    # create a hundred snowflakes
    snowflake = []
    for i in range(num_snowflakes):
        snowflake.append(snowflake())
    # creating the SnowFlake
    snow = Snowflake()

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        for snow in snowflake:
            snow.update()
        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BLACK)      # fill with bgcolor

        # draw the snowflake
        pygame.draw.circle(screen, snow.colour, snow.coords, snow.size)

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
