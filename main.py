import pygame
import random
from enemy import Enemy
from spaceship import Spaceship
from laser import Laser

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load("backgroundmusic.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
my_font = pygame.font.SysFont('Arial', 30)
pygame.display.set_caption("Space Shooter")

# set up variables for the display
SCREEN_HEIGHT = 600 * 1.2
SCREEN_WIDTH = 700 * 1.2
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

# set up intro background display
intro_screen_image = pygame.image.load("space_shooter.png")
intro_screen_image = pygame.transform.scale(intro_screen_image, (700*1.2, 600*1.2))

# set up start button
start_button_image = pygame.image.load("start_button.png")
start_button_image = pygame.transform.scale(start_button_image, (150, 80))
start_button_image_size = start_button_image.get_size()
start_button_rect = pygame.Rect(500, 500, start_button_image_size[0], start_button_image_size[1])

# set up game background
background_image = pygame.image.load("space_background.png")
background_image = pygame.transform.scale(background_image, (700*1.2, 600*1.2))


r = 50
g = 0
b = 100
user = Spaceship(350*1.2, 500*1.2)
laser = Laser(999, 999)
a = Enemy(200, 200)
enemies = []
destroyed = []
moving_x = a.direction_x()
moving_y = a.direction_y()
x_start = random.randint(0, 650*1.2)
run = True
start_screen = True
shoot_laser = False
game_end = False
display_score = my_font.render("Score: " , True, (255, 255, 255))


def keep_score(x):   # recursive method
    if x >= len(destroyed):
        return 1
    return 1 + keep_score(x+1)
    

while run:
    display_score = my_font.render("Score: " + str(keep_score(0)-1), True, (255, 255, 255))
    # screen.blit(display_score, (300, 400))
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(event.pos):
            start_screen = False
    if len(enemies) < 3:
        x_pos = random.randint(50*1.2, 600*1.2)
        a1 = Enemy(x_pos, 0)
        enemies.append(a1)
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d] and not start_screen:
        user.move("right")
    if keys[pygame.K_a] and not start_screen:
        user.move("left")
    if keys[pygame.K_w] and not start_screen:
        user.move("up")
    if keys[pygame.K_s] and not start_screen:
        user.move("down")
    if keys[pygame.K_SPACE] and not start_screen:
        laser.set_location(user.x + 30, user.y - 30)
        shoot_laser = True

    if shoot_laser:
        laser.shoot()

    for a in enemies:
        moving_x = a.direction_x()
        moving_y = a.direction_y()
        if not laser.rect.colliderect(a.rect) and ((a.x > 0 or a.x < 700*1.2) or (a.y < 600*1.2)) and not start_screen:
            a.obstacle_move(moving_x, moving_y)

    for a in enemies:
        if laser.rect.colliderect(a.rect):
            moving_x = a.direction_x()
            moving_y = a.direction_y()
            x_start = random.randint(50*1.2, 600*1.2)
            a.set_location(x_start, 0)
            laser.set_location(-999, -999)
            enemies.remove(a)
            destroyed.append(a)
            # score += 1

    if laser.y < 0:
        laser.set_location(-999, -999)

    for a in enemies:
        if user.rect.colliderect(a.rect):
            game_end = True
    for a in enemies:
        if (a.x < 0 or a.x > 700*1.2) or (a.y > 600*1.2):
            game_end = True

    screen.fill((0, 0, 0))
    if start_screen:
        intro_font = pygame.font.SysFont('Arial', 100)
        display_intro = intro_font.render("Shooting Game", True, (255, 255, 255))
        screen.blit(display_intro, (100*1.2, 200*1.2))
        # screen.blit(intro_screen_image, (0, 0))
        screen.blit(start_button_image, start_button_rect)
    if not start_screen and not game_end:
        screen.blit(background_image, (0, 0))
        screen.blit(user.image, user.rect)
        for a in enemies:
            screen.blit(a.image, a.rect)
        screen.blit(laser.image, laser.rect)
        screen.blit(display_score, (300*1.2, 0))

    if game_end:
        screen.blit(background_image, (0, 0))
        screen.blit(display_score, (300*1.2, 400*1.2))
    pygame.display.update()

pygame.quit()
