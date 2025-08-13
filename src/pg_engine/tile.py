import pygame, os
from user_input_data import uinp
from pathlib import Path

 

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, path_arr):
        super().__init__(groups)

        file_name = Path(os.path.abspath(__file__)).parent.parent.parent / 'graphics'
        for fn in path_arr:
            file_name = file_name / fn

        self.image = pygame.image.load(file_name).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)