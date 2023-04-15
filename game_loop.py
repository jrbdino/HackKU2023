import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f' {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(540, 75))
    screen.blit(score_surf, score_rect)


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            screen.blit(fox_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


def player_animations():
    global player_surf, player_index

    if player_rect.bottom < 465:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]


pygame.init()
screen = pygame.display.set_mode((1080, 620))
pygame.display.set_caption("Gregory's Great Game")
clock = pygame.time.Clock()
game_running = True
start_time = 0
test_font = pygame.font.Font('pygame/fonts/Pixeltype.ttf', 50)

# import image surface rectangle objects here
# player graphics
player_walk1 = pygame.image.load('chicken_graphics/Chickmen.png').convert_alpha()
player_walk2 = pygame.image.load('chicken_graphics/Chickmen.png')
player_walk = [player_walk1, player_walk2]
player_index = 0
player_surf = player_walk[player_index]
player_scaled = pygame.transform.scale(player_walk1, (175, 150))
player_rect = player_scaled.get_rect(bottomleft=(30, 465))
player_jump = pygame.image.load('chicken_graphics/Chickmen_jump.png')
player_gravity = 0

# Background and sky
back_sky = pygame.image.load('chicken_graphics/Environment/sky.png').convert()
sky_scaled = pygame.transform.scale(back_sky, (1080, 620))
back_ground = pygame.image.load('chicken_graphics/Environment/ground.png').convert()
ground_scaled = pygame.transform.scale(back_ground, (1080, 200))

# Obstacles
fox_surf = pygame.image.load('chicken_graphics/fox.png').convert_alpha()
fox_rect = fox_surf.get_rect(bottomleft=(750, 465))

obstacle_rect_list = []

# Obstacle spawner test
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# main loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and player_rect.bottom >= 465:
            if event.key == pygame.K_SPACE:
                player_gravity -= 20

        if event.type == obstacle_timer:
            obstacle_rect_list.append(fox_surf.get_rect(bottomleft=(randint(1080, 1380), 465)))

    if game_running:
        screen.blit(sky_scaled, (0, -2))
        screen.blit(ground_scaled, (0, 425))

        score = display_score()

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 465:
            player_rect.bottom = 465
            player_gravity = 0

        player_animations()
        screen.blit(player_surf, player_rect)
        # screen.blit(fox_surf, fox_rect)

        # obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collisions
        game_running = collisions(player_rect, obstacle_rect_list)

    pygame.display.update()
    clock.tick(60)
