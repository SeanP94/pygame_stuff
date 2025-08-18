import pygame
from user_input_data import uinp
from .globals import GRAPHICS_DIR

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.display_surface = pygame.display.get_surface()

        self.half_width = uinp['width'] // 2
        self.half_height = uinp['height'] // 2
        self.offset = pygame.math.Vector2()

        # Get `skybox background`
        self.floor_surface = pygame.image.load(GRAPHICS_DIR / 'tilemap' / 'ground.png')
        self.floor_rect = self.floor_surface.get_rect(topleft=(0,0))

    
    def custom_draw(self, player):

        # Get the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Draw the floor, (get the offset compared to the user.)
        floor_offset_pos = self.floor_rect.topleft - self.offset

        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

