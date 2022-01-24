# Final Programming Project
# Original is "Jungle Jumpin'" by Scott Elliott
# interpretation of it "George's Jungle jam"
# Further interpretation by Oscar Yu
import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (240, 225, 48)
SKY_BLUE = (95, 165, 228)
BROWN = (138, 51, 36)
WIDTH = 1280
HEIGHT = 720
SPEED = 4
DASH_SPEED = 4
REG_SPEED = 2
TITLE = "Genshin collect"
font_name = pygame.font.match_font('impact')
pygame.mixer.init()

# Background
background_image = pygame.image.load("Background.png")
background_image = pygame.transform.scale(background_image, (1280, 800))


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BROWN)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Initialize Sprite
        self.image = pygame.image.load("Character_Keqing_Game copy.tiff")
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2 - 97.5
        self.rect.y = HEIGHT - self.rect.height - 10

        # Vector
        self.vel_x = 0
        self.monkey_speed = 2

    def update(self):
        self.rect.x += self.vel_x * self.monkey_speed


class Banana(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Initialize Sprite
        self.image = pygame.image.load("Primogem.png")
        self.image = pygame.transform.scale(self.image, (112, 84))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(25, WIDTH - self.rect.width - 25)
        self.rect.y = 0

        # Vector
        self.vel_y = 6

    def update(self):
        self.rect.y += self.vel_y


class Coconut(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Initialize Sprite
        self.image = pygame.image.load("Item_Golden_Shrimp_Balls.webp")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = 0

        # Vector
        self.vel_y = 7

    def update(self):
        self.rect.y += self.vel_y
        if self.rect.y == HEIGHT - self.rect.height:
            self.kill()


class Slime(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Initialize Sprite
        self.image = pygame.image.load("pyro_slime.webp")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(15, WIDTH - self.rect.width)
        self.rect.y = 5

        # Vector
        self.vel_y = 8

    def update(self):
        self.rect.y += self.vel_y
        if self.rect.y == HEIGHT - self.rect.height:
            self.kill()


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    banana_spawn_time = 1000
    coconut_spawn_time = random.randrange(8000, 12000)
    slime_spawn_time = 1000
    last_time_banana_spawned = pygame.time.get_ticks()
    last_time_coconut_spawned = pygame.time.get_ticks()
    last_time_Slime_spawned = pygame.time.get_ticks()
    level_up = 0
    high_score = 0
    score_value = 0
    game_over = True
    timer = 60

    font = pygame.font.SysFont("Arial", 25)

    with open("highscore.txt") as f:
        high_score = int(f.readline().strip())

    # --- Endgame message
    endgame_message = {
        "end": "Thank you for playing this game"
    }

    # ----- Sprites
    all_sprites_group = pygame.sprite.RenderUpdates()
    bananas_group = pygame.sprite.Group()
    coconuts_group = pygame.sprite.Group()
    slime_group = pygame.sprite.Group()

    # ----- Player
    player = Player()
    all_sprites_group.add(player)

    # ----- MAIN LOOP
    while not done:
        if game_over:
            # check to see if highscore was beaten
            if score_value > high_score:
                high_score = score_value
                # reset game
            banana_spawn_time = 1000
            level_up = 10
            score_value = 0
            player.vel_x = 0
            player.rect.x = WIDTH / 2 - 97.5
            player.rect.y = HEIGHT - player.rect.height - 10
            for banana in bananas_group:
                banana.kill()
            game_over = False

        # -- Event Handler
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                done = True

            if not game_over:
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_RIGHT:
                        player.vel_x = SPEED
                    elif events.key == pygame.K_LEFT:
                        player.vel_x = -SPEED
                    elif events.key == pygame.K_LSHIFT:
                        player.monkey_speed = DASH_SPEED

                elif events.type == pygame.KEYUP:
                    if events.key == pygame.K_LEFT and player.vel_x < 0:
                        player.vel_x = 0
                    if events.key == pygame.K_RIGHT and player.vel_x > 0:
                        player.vel_x = 0
                    if events.key == pygame.K_LSHIFT:
                        player.monkey_speed = REG_SPEED

        # ----- LOGIC
        all_sprites_group.update()

        # While the game is running
        if not game_over:
            # banana spawn
            if pygame.time.get_ticks() > last_time_banana_spawned + banana_spawn_time:
                # set the new time to this current time
                last_time_banana_spawned = pygame.time.get_ticks()
                # spawn banana
                banana = Banana()
                all_sprites_group.add(banana)
                bananas_group.add(banana)

            # coconut spawn
            if pygame.time.get_ticks() > last_time_coconut_spawned + coconut_spawn_time:
                last_time_coconut_spawned = pygame.time.get_ticks()
                # spawn coconut
                coconut = Coconut()
                all_sprites_group.add(coconut)
                coconuts_group.add(coconut)

            # slime spawn
            if pygame.time.get_ticks() > last_time_Slime_spawned + slime_spawn_time:
                last_time_Slime_spawned = pygame.time.get_ticks()
                # spawn slime
                slime = Slime()
                all_sprites_group.add(slime)
                slime_group.add(slime)

            # check if banana hits ground
            for banana in bananas_group:
                if banana.rect.y >= HEIGHT - banana.rect.height - 7:
                    banana.kill()

                # Player collision
                bananas_collected = pygame.sprite.spritecollide(player, bananas_group, True)
                if len(bananas_collected) > 0:
                    banana.kill()
                    score_value += 1

            # check if coconut hits ground
            for coconut in coconuts_group:
                if coconut.rect.y >= HEIGHT - coconut.rect.height - 11:
                    coconut.kill()

                # Player collision
                coconut_collected = pygame.sprite.spritecollide(player, coconuts_group, True)
                if len(coconut_collected) > 0:
                    coconut.kill()
                    score_value += 3

            # check if slime hits ground
            for slime in slime_group:
                if slime.rect.y >= HEIGHT - slime.rect.height - 11:
                    slime.kill()

                # player collision
                slime_collected = pygame.sprite.spritecollide(player, slime_group, True)
                if len(slime_collected) > 0:
                    score_value -= 1

            # decrease spawn time
            if score_value >= level_up:
                banana_spawn_time -= 60
                level_up += 12

        # ----- DRAW
        screen.blit(background_image, (0, 0))
        dirty_rectangles = all_sprites_group.draw(screen)

        # ----- UPDATE
        pygame.display.update(dirty_rectangles)
        draw_text(screen, ("Score: " + str(score_value)), 36, 95, 10)
        draw_text(screen, ("Timer: " + str(timer)), 36, 240, 40)
        draw_text(screen, "High Score: " + str(high_score), 36, 125, 70)

       # TIME COOL DOWN
        timer -= 0.015

        if timer <= 0:
            game_over = True
            screen.blit(
                font.render(endgame_message["end"], True, BLACK),
                (WIDTH / 4, HEIGHT / 4)
            )

        # Update the screen
        pygame.display.flip()

        # ---- clock tick
        clock.tick(60)

        # If the player gets near the right side, shift the world left (-x)
        # subtract 25 to add a bit of a barrier
        if player.rect.right > WIDTH - 25:
            player.rect.right = WIDTH - 25

        # If the player gets near the left side, shift the world right (+x)
        # add 25 to add a bit of a barrier
        if player.rect.left < 25:
            player.rect.left = 25

        with open("highscore.txt", "w") as f:
            if score_value > high_score:
                f.write(str(score_value))
            else:
                f.write(str(high_score))

    pygame.quit()


if __name__ == "__main__":
    main()

