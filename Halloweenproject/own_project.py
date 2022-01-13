# Pygame collecting blocks
# Author: oscar
# 2021 Version

import random
import time
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
PALE_GOLD = (230, 190, 138)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Collecting Blocks"


class Player(pygame.sprite.Sprite):
    """Describes a player object
    A subclass of pygame.sprite.Sprite
    Attributes:
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]
        hp: describes how much health our
            player has

    """
    def __init__(self) -> None:
        # Call the superclass constructor
        super().__init__()

        self.image = pygame.image.load("./images/charmender.png")
        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()

        # Initial health points
        self.hp = 250


class Block(pygame.sprite.Sprite):
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

        self.coords = [
            random.randrange(0, SCREEN_WIDTH),
            random.randrange(0, SCREEN_HEIGHT)
        ]
        self.y_vel = (random.randrange(2, 4))

    def update(self):
        """Update the location of the snow"""
        # Changes the y portion of the coords
        self.coords[1] += self.y_vel

        # Reset position of snowflake if it reaches bottom
        if self.coords[1] > SCREEN_HEIGHT:
            self.coords = [
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
    num_blocks = 100
    score = 0
    time_start = time.time()
    time_invincible = 5        # Seconds
    endgame_cooldown = 5        # seconds
    time_ended = 0.0
    snowflake = []

    font = pygame.font.SysFont("Arial", 25)

    pygame.mouse.set_visible(False)

    # Create groups to hold sprites
    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()

    # Create all the block sprites and add to block_sprites
    for i in range(num_blocks):
        # Create a block ( set its parameters)
        block = Block(WHITE, 20, 15)

        # set a random location for hte block inside the screen
        block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
        block.rect.y = random.randrange(SCREEN_HEIGHT - block.rect.height)

        # Add the block to the block_sprite Group
        # Add the block to the all_sprites Group
        block_sprites.add(block)
        all_sprites.add(block)

    # Create the player block
    player = Player()
    # Block(PALE_GOLD, 20, 15)
    # add the player to all_sprites group
    all_sprites.add(player)

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # End-game listener
        # WIN CONDITION - collect 100 blocks
        if score == num_blocks:
            # Indicate to draw a message
            game_state = "won"

            # SET THE TIME THAT THE GAME WAS WON
            if time_ended == 0:
                time_ended = time.time()
            # Set parameters to keep the screen alive
            # wait 4 seconds to kill the screen
            if time.time() - time_ended >= endgame_cooldown:
                done = True

            # SET THE TIME THAT THE GAME WAS WON
            if time_ended == 0:
                time_ended = time.time()
            # Set parameters to keep the screen alive
            # wait 4 seconds to kill the screen
            if time.time() - time_ended >= endgame_cooldown:
                done = True

        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0] - player.rect.width / 2
        player.rect.y = mouse_pos[1] - player.rect.height / 2

        # set a time
        if time.time() - time_start > time_invincible:

                # Check all collisions between player and the blocks
            blocks_collided = pygame.sprite.spritecollide(player, block_sprites, True)

            for block in blocks_collided:
                score += 1

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BLIZZARD_BLUE)
        # ----------- CHANGE ENVIRONMENT
        for snow in snowflake:
            snow.update()
        # draw the snowflake
        for snow in snowflake:
            pygame.draw.circle(screen, snow.colour, snow.coords, snow.size)

        # Draw all sprites
        all_sprites.draw(screen)

        # Draw the score on the screen
        screen.blit(
            font.render(f"Score: {score}", True, BLACK),
            (5, 5)

        )


        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()