import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1080, 620))

pygame.display.set_caption("Chicken Game")
clock = pygame.time.Clock()

# initialize
# backgrounds here



# main loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()