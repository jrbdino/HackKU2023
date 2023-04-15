import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1080, 620))
pygame.display.set_caption("Gregory's Great Game")
clock = pygame.time.Clock()
# init font if needed here

# import image surface rectangle objects here
# scuffed imports stay here, do not move out of order
from characters import *

# Background and sky
back_sky = pygame.image.load('chicken_graphics/Environment/sky.png')
sky_scaled = pygame.transform.scale(back_sky, (1080, 620))
back_ground = pygame.image.load('chicken_graphics/Environment/ground.png')
ground_scaled = pygame.transform.scale(back_ground, (1080, 200))

# Gregory
chicken = pygame.image.load('chicken_graphics/Chickmen.png')

# main loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_scaled, (0, 0))
    screen.blit(ground_scaled, (0, 425))
    screen.blit(chicken, (30, 245))

    pygame.display.update()
    clock.tick(60)
