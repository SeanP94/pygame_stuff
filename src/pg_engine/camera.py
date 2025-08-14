import pygame
from user_input_data import uinp

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.display_surface = pygame.display.get_surface()

        self.half_width = uinp['width'] // 2
        self.half_height = uinp['height'] // 2
        self.offset = pygame.math.Vector2()


    
    def custom_draw(self, player):

        # Get the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)