# Pygame Boilerplate
# Author: Ubial
# 2021 Version


import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (255,   0,   0)
GREEN = (0, 255,   0)
BLUE = (0,   0, 255)
BGCOLOUR = (100, 100, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "DVD Screen Saver"


class Dvdimage:
    """Represents a dvdimage on screen

    Attributes:
        x,y: coordinates of top-left corner
        width: width of image in pixels
        height:height of image in pixels
        image: visual representation of our Dvdimage
        x-vel: x velocity in px/sec
        y-vel: y velocity in px/sec
    """
    def __init__(self):
        self.x, self.y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.width = 180
        self.height = 180
        self.image = pygame.image.load("./images/dvdimage.png")
        self.image = pygame.image.load("./images/background.jpg")
        self.x_vel = 5
        self.y_vel = 3

    def rect(self) -> pygame.rect:
        """Returns a pygame.rect that represents the dvd_image"""
        return [self.x, self.y, self.width, self.height]

    def update(self) -> None:
        """Updates the Dvdimage with every tick"""
        # update the x-coordinate
        self.x += self.x_vel
        # If Dvdimage is too far to the left
        if self.x < 0:
            # Keep the object in the canvas
            self.x = 0
            # Set the velocity to the negative
            self.x_vel = -self.x_vel
        # If Dvdimage is too far to the right
        if self.x + self.width > SCREEN_WIDTH:
            # Keep the object in the canvas
            self.x = SCREEN_WIDTH - self.width
            # Set the velocity to the negative
            self.x_vel = -self.x_vel
        # update the y- coordinate
        self.y += self.y_vel
        # If Dvdimage is too far to the top
        if self.y < 0:
            # Keep the object in the canvas
            self.y = 0
            # Set the velocity to the negative
            self.y_vel = -self.y_vel
        # If Dvdimage is too far to the bottom
        if self.y + self.height > SCREEN_HEIGHT:
            # Keep the object in the canvas
            self.y = SCREEN_HEIGHT - self.height
            # Set the velocity to the negative
            self.y_vel = -self.y_vel


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    dvd_image = Dvdimage()

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        dvd_image.update()
        print(f"x: {dvd_image.x}, y: {dvd_image.y}")
        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor
         screen.blit(dvd_image.image, (dvd_image.x, dvd_image.y))

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
