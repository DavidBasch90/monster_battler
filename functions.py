import pygame

def scale_sprite(player_img, SCALE_FACTOR):
    player_img = pygame.transform.scale(player_img, (player_img.get_width() * SCALE_FACTOR, player_img.get_height() * SCALE_FACTOR))
    return player_img