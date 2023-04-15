import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('pygame/fonts/Pixeltype.ttf', 50)


sky_surface = pygame.image.load('pygame/graphics/sky.png').convert_alpha()
ground_surface = pygame.image.load('pygame/graphics/ground.jpg').convert_alpha()
text_surface = test_font.render('My Game', False, 'Black')

snail_surf = pygame.image.load('pygame/graphics/enemies/snail/32bit-gastropod-scaly-foot.gif').convert_alpha()
snail_surf = pygame.transform.scale(snail_surf, (50, 50))
snail_rect = snail_surf.get_rect(bottomright=(600,300))

player_surf = pygame.image.load('pygame/graphics/player/kenney_platformerCharacters/PNG/Adventurer/Poses/adventurer_stand.png')
player_rect = player_surf.get_rect(midbottom=(80,300))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface, (300,50))

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    print(player_rect.left)
    screen.blit(player_surf,player_rect)

    if player_rect.colliderect((snail_rect)):
        print('collision')

    pygame.display.update()
    clock.tick(60)

# stopped for the night on mouse collisions