# start screen
import pygame
from sys import exit

test_font = pygame.font.Font('pygame/fonts/Pixeltype.ttf', 50)

#start screen
start_sky = pygame.image.load('chicken_graphics/Environment/start_sunrise.png').convert()
game_name = test_font.render('Gregorys Great Game', False, 'Red')
game_name_rect = game_name.get_rect(center = (540,150))

game_message = test_font.render('Press Space to Start',False,'Red')
game_message_rect = game_message.get_rect(center = (540,450))
