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



# main loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
