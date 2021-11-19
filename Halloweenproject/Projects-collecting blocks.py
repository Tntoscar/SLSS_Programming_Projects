# Pygame collecting blocks
# Author: oscar
# 2021 Version


import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (255,   0,   0)
GREEN = (0, 255,   0)
BLUE = (0,   0, 255)
BGCOLOUR = (100, 100, 255)
RUST = (148, 27, 12)
BLIZZARD_BLUE = (154, 229, 230)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Collecting Blocks"


class Block(pygame.sprite.Sprite):
    """Describes a block object
    A sub class of pygame.sprite.Sprite

    Attributes:
        image: Surface that s the visual
            representation of our block
        rect: numeral representation of
            our [x , y , width, height]

    """
    def __init__(self, colour: tuple, width: int, height: int) -> None:
        """
        Arguments:
        :param colour: 3-tuple (r, g,b)
        :param width: width in pixels
        :param height: height in pixels
        """
        # call the superclass constructor
        super().__init__()

        # create the image of the block
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        # based on the image create a Rect for the block
        self.rect = self.image.get_rect()


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()

    # Create a group of sprites to store ALL SPRITES
    all_sprites = pygame.sprite.Group()

    # Create the player block
    player = Block(BLIZZARD_BLUE, 20, 15)
    # add the player to all_sprites group
    all_sprites.add(player)

    pygame.mouse.set_visible(False)

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        # Process player movement based on mouse position
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x, player.rect.y = mouse_pos

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(RUST)      # fill with bgcolor

        # Draw all sprites
        all_sprites.draw(screen)

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
