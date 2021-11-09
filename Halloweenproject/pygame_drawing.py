# Pygame_Drawing
# Author: Oscar
# 9 November 2021

# Get introduced to Pygame

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
AQUA = (66, 239, 245)
LIGHT_ORANGE = (245, 176, 66)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Pygame Drawing"


def main() -> None:
    """Driver of the python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)
    # Create the local variables that describe the environment
    done = False
    clock = pygame.time.Clock()

    # ------------ Event LISTENER
    while not done:
        # make space for the event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ------------- CHANGE ENVIRONMENT
        # ------------- Draw the environment
        screen.fill(WHITE)      # fill with background color
        pygame.draw.rect(screen, BLACK, [90, 90, 100, 100])
        pygame.draw.rect(screen, RED, [100, 100, 75, 75])
        pygame.draw.rect(screen, BLUE, [110, 110, 50, 50])
        pygame.draw.circle(screen, AQUA, (600, 255), 120)
        pygame.draw.circle(screen, BLUE, (600, 255), 100)
        pygame.draw.circle(screen, GREEN, (600, 255), 80)
        pygame.draw.circle(screen, RED, (600, 255), 60)
        pygame.draw.circle(screen, WHITE, (600, 255), 40)
        pygame.draw.circle(screen, BLACK, (600, 255), 20)
        pygame.draw.circle(screen, LIGHT_ORANGE, (600, 255), 10)

        pygame.draw.circle(screen, LIGHT_ORANGE, (300, 300), 100)
        pygame.draw.rect(screen, GREEN, [280, 400, 30, 150])
        pygame.draw.circle(screen, BLACK, (240, 250), 40)
        pygame.draw.circle(screen, BLACK, (350, 250), 40)
        pygame.draw.circle(screen, WHITE, (240, 250), 20)
        pygame.draw.circle(screen, WHITE, (350, 250), 20)
        pygame. draw.circle(screen, RED, (350, 250), 10)
        # Update the screen
        pygame.display.flip()

        # ------------- clock tick
        clock.tick(75)


if __name__ == "__main__":
    main()
