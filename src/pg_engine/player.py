import pygame
from user_input_data import uinp
from .globals import GRAPHICS_DIR

class Player(pygame.sprite.Sprite):

    def __init__(self, pos,  groups : pygame.sprite.Group, obstacle_sprites : pygame.sprite.Group):
        '''
            Parameters:
            pos: position of Player
            groups: the pygame.sprite.Group it belongs too
            obstacle_sprites: the pygame.sprite.Group of the collidable map objects.
        '''
        super().__init__(groups)

        self.image = pygame.image.load(GRAPHICS_DIR / 'test' / 'player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        # Shrink players hitbox.
        self.hitbox = self.rect.inflate(0, -12)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    

    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
    
    def move(self):
        # Solve the problem of going diagnoal
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * self.speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * self.speed
        self.collision('vertical')
        
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        '''
        Collision will correct the rectangles. So the wall of the object's coordinates
        will be set to the Players coresponding wall.
        '''
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # Right
                        self.hitbox.right = sprite.hitbox.left 
                    elif self.direction.x < 0: # Left
                        self.hitbox.left = sprite.hitbox.right
        if direction == 'vertical':  
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y < 0: # Up
                        self.hitbox.top = sprite.hitbox.bottom 
                    elif self.direction.y > 0: #Down
                        self.hitbox.bottom = sprite.hitbox.top

    def update(self):
        self.input()
        self.move()

