import pygame
from .globals import GRAPHICS_DIR

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)

        self.direction = player.status.split('_')[0] # Get players direction.
        
        self.image = pygame.image.load(GRAPHICS_DIR / 'weapons' / player.weapon / f'{self.direction}.png')
        self.weapon_dir(player)

    def weapon_dir(self, player):
        if self.direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16))
        elif self.direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16))
        elif self.direction == 'down':
            self.rect = self.image.get_rect(topleft = player.rect.bottomleft)# + pygame.math.Vector2(0,16))
        elif self.direction == 'up':
            self.rect = self.image.get_rect(bottomleft = player.rect.topleft + pygame.math.Vector2(8, 0))# + pygame.math.Vector2(0,16))
        else:
            self.rect = self.image.get_rect(center = player.rect.center) # Err

    