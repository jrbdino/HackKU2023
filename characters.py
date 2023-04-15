import pygame

# Chicken Graphics
chick_surf = pygame.image.load('chicken_graphics/Chickmen.png').convert_alpha()
chick_scaled = pygame.transform.scale(chick_surf, (150, 150))
chick_rect = chick_surf.get_rect(topleft=(150, 150))
