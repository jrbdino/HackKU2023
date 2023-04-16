
# game over image
end_sky = pygame.image.load('chicken_graphics/Environment/end_sunset.png').convert_alpha()
end_sky_scaled = pygame.transform.scale(end_sky, (1080, 620))

# game over screen
if game_active:
    pass
#else:  # need to play with coords, use same colors if they have enough contrast or use similar colors
screen.blit(end_sky_scaled, (0, 0))

player_rect = player_scaled.get_rect(midleft=(100, 300))
screen.blit(player_walk1, player_rect)
# player_gravity = 0 cut if not needed

over_message = test_font.render("Game Over", False, "#A93226")
over_message_rect = over_message.get_rect(top=(540, 50))
screen.blit(over_message, over_message_rect)

score_message = test_font.render(f'You scored {score} points!', False, "#A93226")
score_message_rect = score_message.get_rect(centerright=(540, 310))
screen.blit(score_message, score_message_rect)

tryagain_message = test_font.render("Press SPACEBAR to try again", False, "#A93226")
tryagain_message_rect = tryagain_message.get_rect(bottom=(540, 570))
screen.blit(tryagain_message, tryagain_message_rect)
