import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f' {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (540,75))
    screen.blit(score_surf,score_rect)

pygame.init()
screen = pygame.display.set_mode((1080,620))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('pygame/fonts/Pixeltype.ttf', 50)
title_font = pygame.font.Font('pygame/fonts/Pixeltype.ttf', 75)
game_active = False
start_time = 0

sky_surface = pygame.image.load('chicken_graphics/Environment/sky.png').convert()
ground_surface = pygame.image.load('chicken_graphics/Environment/ground.png').convert()
text_surface = test_font.render('My game', False, 'Green')

enemy_surf = pygame.image.load('pygame/graphics/enemies/All/jellyfish.png').convert_alpha()
enemy_rect = enemy_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('chicken_graphics/Chickmen.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

#start screen
start_sky = pygame.image.load('chicken_graphics/Environment/start_sunrise.png').convert()
start_sky_scaled = pygame.transform.scale(start_sky, (1080, 620))
game_name = title_font.render("Gregory's  Great  Game", False, '#693C98')
game_name_rect = game_name.get_rect(center = (540,160))

game_message = test_font.render('Press  Space  to  Start',False,'#693C98')
game_message_rect = game_message.get_rect(center = (540,450))
# player_stand = pygame.image.load('chicken_graphics/Chickmen.png').convert_alpha()
# player_stand = pygame.transform.scale(player_stand,(200, 400))
# player_stand_rect = player_stand.get_rect(center = (400,200))
screen.blit(game_name,game_name_rect)
screen.blit(game_message,game_message_rect)

while True:
    for event in pygame.event.get():

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.botton >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy_rect = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface, (0,300))
    # screen.blit(text_surface,(300,50))

    # screen.blit(enemy_surf,(enemy_x_pos,250))

        display_score()

        enemy_rect.x -= 4
        if enemy_rect.right <= 0: enemy_rect.left = 800
        screen.blit(enemy_surf, enemy_rect)

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300

        #collision
        if enemy_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.blit(start_sky_scaled,(0,0))
        screen.blit(game_name,game_name_rect)
        screen.blit(game_message,game_message_rect)


    pygame.display.update()
    clock.tick(60)