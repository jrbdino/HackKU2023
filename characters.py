import pygame


# Chicken Graphics

player_surf = pygame.image.load('chicken_graphics/Chickmen.png').convert_alpha()
player_scaled = pygame.transform.scale(player_surf, (150, 150))
player_rect = player_surf.get_rect(topleft=(150, 150))
