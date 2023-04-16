import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = game_font.render(f' {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(540, 75))
    screen.blit(score_surf, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 15

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
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]


pygame.init()
screen = pygame.display.set_mode((1080, 620))
pygame.display.set_caption("Gregory's Great Game")
clock = pygame.time.Clock()
game_running = False
start_time = 0
score = 0
game_font = pygame.font.Font('pygame/fonts/Pixeltype.ttf', 50)

# import image surface rectangle objects here
# player graphics
player_walk1 = pygame.image.load('chicken_graphics/Chicken_walk1.png').convert_alpha()
player_walk2 = pygame.image.load('chicken_graphics/Chicken_walk2.png')
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

# Game title
game_title = game_font.render("Game Game", False, "#A93226")
game_title_rect = game_title.get_rect(midtop=(540, 310))

# main loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_running:
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 465:
                if event.key == pygame.K_SPACE:
                    player_gravity -= 20

            if event.type == obstacle_timer:
                obstacle_rect_list.append(fox_surf.get_rect(bottomleft=(randint(1080, 1380), 465)))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_running = True
                obstacle_rect_list = []
                start_time = int(pygame.time.get_ticks() / 1000)

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
    # Game over screen, text, in the else statement
    else:
        game_name = game_font.render("Gregory's  Great  Game", False, '#693C98')
        game_name_rect = game_name.get_rect(center=(540, 150))



        over_message = game_font.render("Game Over", False, "#A93226")
        over_message_rect = over_message.get_rect(topleft=(540, 50))

        score_message = game_font.render(f'You scored {score} points!', False, "#A93226")
        score_message_rect = score_message.get_rect(midright=(540, 310))

        tryagain_message = game_font.render("Press SPACEBAR to try again", False, "#A93226")
        tryagain_message_rect = tryagain_message.get_rect(midbottom=(540, 570))

        if score == 0:
            start_screen = pygame.image.load('chicken_graphics/Environment/start_sunrise.png').convert_alpha()
            start_scaled = pygame.transform.scale(start_screen, (1080, 620))

            player_stand = pygame.image.load('chicken_graphics/Chickmen_jump.png').convert_alpha()
            player_stand = pygame.transform.scale(player_stand, (200, 170))
            player_stand_rect = player_stand.get_rect(center=(260, 280))

            fox_stand = pygame.image.load('chicken_graphics/fox.png').convert_alpha()
            fox_stand = pygame.transform.scale(fox_stand, (200, 100))
            fox_stand_rect = fox_stand.get_rect(center=(900, 400))

            game_message = game_font.render('Press  Space  to  Start', False, '#693C98')
            game_message_rect = game_message.get_rect(center=(540, 450))

            screen.blit(start_scaled, (0, 0))
            screen.blit(game_name, game_name_rect)
            screen.blit(player_stand, player_stand_rect)
            screen.blit(fox_stand, fox_stand_rect)
            screen.blit(game_message, game_message_rect)

        else:
            end_sky = pygame.image.load('chicken_graphics/Environment/end_sunset.png').convert_alpha()
            end_sky_scaled = pygame.transform.scale(end_sky, (1080, 620))

            screen.blit(end_sky_scaled, (0, 0))
            screen.blit(score_message, score_message_rect)
            screen.blit(tryagain_message, tryagain_message_rect)
            screen.blit(over_message, over_message_rect)
            player_rect = player_scaled.get_rect(midleft=(100, 300))
            screen.blit(player_walk1, player_rect)

    pygame.display.update()
    clock.tick(60)
