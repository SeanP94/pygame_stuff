import pygame, os
from user_input_data import uinp
from pathlib import Path

from .globals import GRAPHICS_DIR
 

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((uinp['grid_cell_size'], uinp['grid_cell_size'])), path_arr=None):
        super().__init__(groups)

        self.sprite_type = sprite_type

        # if path_arr:
        #     file_name = GRAPHICS_DIR
        #     for fn in path_arr:
        #         file_name = file_name / fn
        #     self.image = pygame.image.load(file_name).convert_alpha()
        # else:
        #     self.image = surface
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)
        # Shrink players hitbox.
        self.hitbox = self.rect.inflate(0, -10)