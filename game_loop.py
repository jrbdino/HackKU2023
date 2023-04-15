import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1080, 620))
pygame.display.set_caption("Gregory's Great Game")
clock = pygame.time.Clock()
game_running = True
# init font if needed here

# import image surface rectangle objects here
# player graphics
player_surf = pygame.image.load('chicken_graphics/Chickmen.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (150, 150))
player_rect = player_surf.get_rect(bottomleft=(30, 465))
player_gravity = 0

# Background and sky
back_sky = pygame.image.load('chicken_graphics/Environment/sky.png').convert()
sky_scaled = pygame.transform.scale(back_sky, (1080, 620))
back_ground = pygame.image.load('chicken_graphics/Environment/ground.png').convert()
ground_scaled = pygame.transform.scale(back_ground, (1080, 200))

# Obstacles
fox_surf = pygame.image.load('chicken_graphics/fox.png').convert_alpha()
fox_rect = fox_surf.get_rect(bottomleft=(750, 465))


# main loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and player_rect.bottom >= 465:
            if event.key == pygame.K_SPACE:
                player_gravity -= 20

    if game_running:
        screen.blit(sky_scaled, (0, -2))
        screen.blit(ground_scaled, (0, 425))

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 465:
            player_rect.bottom = 465
            player_gravity = 0

        screen.blit(player_surf, player_rect)
        screen.blit(fox_surf, fox_rect)

    pygame.display.update()
    clock.tick(60)
