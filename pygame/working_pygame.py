import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))  # width, height
pygame.display.set_caption("Runner")  # title of window
clock = pygame.time.Clock()  # used for frame rates
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 50)  # font type, font size / None is default font

sky_surface = pygame.image.load('graphics/sky.png').convert()  # check image dimensions or figure out duplication
ground_surface = pygame.image.load('graphics/ground.jpg').convert()  # convert helps run more smoothly

score_surf = test_font.render("My Game", False, "Black")  # text, anti-aliasing, color
score_rect = score_surf.get_rect(center=(400, 50))

jellyfish_surf = pygame.image.load('graphics/enemies/All/jellyfish.png').convert_alpha()  # alpha for non-transparent
# jellyfish_x_pos = 600 -- replaced with rect below
jellyfish_rect = jellyfish_surf.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load('graphics/player/kenney_platformerCharacters/PNG/Female/Poses/female_stand.png') \
    .convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))  # get_rect draws rectangle around surface 300 - ground starts

# test_surface = pygame.Surface((100,200))  # width, height
# test_surface.fill("Red")  # fill color

while True:  # display all our elements and update everything
    for event in pygame.event.get():  # iterates over all events in event list
        if event.type == pygame.QUIT:  # keeps it from running indefinitely
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:  # can do mousebuttomdown and -up to see if clicked or released
        # print(event.pos)  # prints the x,y position
            if player_rect.collidepoint(event.pos):
                print("collision")

    screen.blit(sky_surface, (0, 0))  # block image transfer aka display surface atop another ; origin is top left
    screen.blit(ground_surface, (0, 300))  # draw sky first (lay ground on top of sky)
    screen.blit(score_surf, score_rect)
    # jellyfish_x_pos -= 4  # speed -- replaced with rect
    # if jellyfish_x_pos < -100:
    # jellyfish_x_pos = 800
    screen.blit(jellyfish_surf, jellyfish_rect)
    jellyfish_rect.right -= 4  # moving jelly to the left
    if jellyfish_rect.right <= 0:
        jellyfish_rect.right = 800  # reset to right of screen
    # player_rect.left += 1  # moving her to the right
    # print(player_rect.left) to get location
    screen.blit(player_surf, player_rect)  # taking surface and placing in position of rectangle

    # if player_rect.colliderect(jellyfish_rect):  # boolean False-no collision, True-yes
        # print("collision")  # ensure collision once then invincibility frames if health system (more than 1 hit)
    mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint(mouse_pos):  # for mouse / pygame.mouse < lots of info or event loop
        # print(pygame.mouse.get_pressed())  # Boolean for left click, middle click, and right click, true-pressed
        # print("collision")
    pygame.display.update()
    clock.tick(60)  # max 60fps
