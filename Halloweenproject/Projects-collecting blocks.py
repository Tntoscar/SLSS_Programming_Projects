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

        # Create the image of the block
        self.image = pygame.image.load("./images/charmender.png")

        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()

        # Initial health points
        self.hp = 250

    def hp_remaining(self) -> float:
        """Return the percent of health remaining"""
        return self.hp / 250


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


class Enemy(pygame.sprite.Sprite):
    """The enemy sprites

    Attributes:
        image: Surface is the visual representation
        rect: Rect (x, y, width, height)
        x_vel = x velocity
        y_vel = y velocity
    """
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/ekans.png")
        # Resize the image (scale)
        # self.image = pygame.transform.scale(self.image, (91, 109))

        self.rect = self.image.get_rect()
        # define the initial location
        self.rect.x, self.rect.y = (
            random.randrange(SCREEN_WIDTH),
            random.randrange(SCREEN_HEIGHT)
        )

        # Define the inital velocity
        self.x_vel = random.choice([-2, -1, 1, 2])
        self.y_vel = random.choice([-2, -1, 1, 2])

    def update(self):
        """calculate movement"""
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # constrain the movement
        # X-
        if self.rect.left < 0:
            self.rect.x = 0
            self.x_vel = -self.x_vel  # bounces
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.x_vel = -self.x_vel
        # Y-
        if self.rect.y < 0:
            self.rect.y = 0
            self.y_vel = - self.y_vel
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.y_vel = -self.y_vel


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_blocks = 100
    num_enemies = 5
    score = 0
    time_start = time.time()
    time_invincible = 5        # Seconds
    game_state = "running"
    endgame_cooldown = 5        # seconds
    time_ended = 0.0

    endgame_messages = {
        "win": "Congratulations, you won!",
        "Lose": "Sorry, you are just bad. Play again!",
    }

    font = pygame.font.SysFont("Arial", 25)

    pygame.mouse.set_visible(False)

    # Create groups to hold sprites
    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

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
    # Create enemy sprites
    for i in range(num_enemies):
        # Create an enemy
        enemy = Enemy()
        # add it to the sprites list( enemy_sprites and all_sprites)
        enemy_sprites.add(enemy)
        all_sprites.add(enemy)

    # Create the player block
    player = Player()
    # Block(PALE_GOLD, 20, 15)
    # add the player to all_sprites group
    all_sprites.add(player)

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
            if time_ended > 0:
                time_ended = time.time()
            # Set parameters to keep the screen alive
            # wait 4 seconds to kill the screen
            if time.time() - time_ended >= endgame_cooldown:
                done = True
        # LOSE CONDITION - PLayer's hp goes below 0
        if player.hp_remaining() <= 0:
            done = True

        # ----------- CHANGE ENVIRONMENT
        # Process player movement based on mouse position

        mouse_pos = pygame.mouse.get_pos()
        player.rect.x, player.rect.y = mouse_pos
        # Update the location of all sprites
        all_sprites.update()

        # Update the location of all sprites
        all_sprites.update()
        # Check all collisions between player and the blocks
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites, False)
        # set a time
        if time.time() - time_start > time_invincible:
            for enemy in enemies_collided:
                player.hp -= 1

                # Check all collisions between player and the blocks
            blocks_collided = pygame.sprite.spritecollide(player, block_sprites, True)

            for block in blocks_collided:
                score += 1

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BLIZZARD_BLUE)      # fill with bgcolor

        # Draw all sprites
        all_sprites.draw(screen)

        # Draw the score on the screen
        screen.blit(
            font.render(f"Score: {score}", True, BLACK),
            (5, 5)

        )
        # Draw a health bar
        # Draw the background rectangle
        pygame.draw.rect(screen,GREEN, [580, 5, 215, 20])
        # Draw the foreground rectangle which is the remaining health
        life_remaining = 215 - int(215 * player.hp_remaining())
        pygame.draw.rect(screen, BLUE, [580, 5, life_remaining, 20])

        # If we've won, draw the text on the screen
        if game_state == "won":
            screen.blit(
                font.render(endgame_messages["win"], True, BLACK),
                (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            )

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
