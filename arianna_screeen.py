def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f"Score: {current_time}", False, "#2E4053")
    score_rect = score_surf.get_rect(center=(540, 100))
    screen.blit(score_surf, score_rect)
    return current_time

...

if game_active:
    pass
else:

    screen.blit(sky_scaled, (0, 0))
    screen.blit(player_stand, player_stand_rect)
    player_rect.midbottom = (100,300)
    player_gravity = 0

    over_message = test_font.render("Game Over", False, "#2E4053")
    over_message_rect = over_message.get_rect()

    score_message = test_font.render(f'You scored {score} points!', False, "#2E4053")
    score_message_rect = score_message.get_rect(center=(540, 310))
    screen.blit(game_name, game_name_rect)
