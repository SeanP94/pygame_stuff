import pygame
from user_input_data import uinp
from .globals import GRAPHICS_DIR
from .support import import_folder

class Player(pygame.sprite.Sprite):

    def __init__(self, pos,  groups : pygame.sprite.Group, obstacle_sprites : pygame.sprite.Group, create_attack, destroy_attack):
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
        self.hitbox = self.rect.inflate(0, -26)

        # Sprite Obstacle list
        self.obstacle_sprites = obstacle_sprites

        # User Input
        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.attacking = False
        self.attack_cooldown = 400 # MS
        self.attack_time = None

        # Animation Logic 
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15
        

        # Graphics setup.
        self.import_player_assets()


        # Weapon 
        self.create_attack = create_attack # This is the create_attack function from weapon, passed to us by the level.
        self.destroy_attack = destroy_attack
        self.weapon_index = 0 # Weapon type in game default : sword
        self.update_weapon()
        

    def import_player_assets(self):
        '''
        Imports all of the players assets into self.animations
        '''
        character_path = GRAPHICS_DIR / 'player'
        self.animations = {
            'up' : [], 'down' : [], 'left' : [], 'right' : [],
            'up_idle' : [], 'down_idle' : [], 'right_idle' : [], 'left_idle' : [],
            'up_attack' : [], 'down_attack' : [], 'right_attack' : [], 'left_attack' : []
        } 

        for animation in self.animations.keys():
            img_list = import_folder(character_path / animation)
            self.animations[animation] = img_list
    
    
    def input(self):
        keys = pygame.key.get_pressed()

        if not self.attacking:
            if keys[pygame.K_UP]:
                self.status = 'up'
                self.direction.y = -1
            elif keys[pygame.K_DOWN]:
                self.status = 'down'
                self.direction.y = 1
            else:
                self.direction.y = 0

            if keys[pygame.K_LEFT]:
                self.status = 'left'
                self.direction.x = -1
            elif keys[pygame.K_RIGHT]:
                self.status = 'right'
                self.direction.x = 1
            else:
                self.direction.x = 0

            # New attack
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
                print('Attack!')

            if keys[pygame.K_z]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                print("Spell!")
            
            if keys[pygame.K_q] and self.can_switch_weapon:
                self.weapon_index = (self.weapon_index + 1) % len(uinp['weapon_data'])
                self.update_weapon()
                self.weapon_switch_time = pygame.time.get_ticks()
                self.can_switch_weapon = False

    def update_weapon(self):
        self.weapon = list(uinp['weapon_data'].keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = uinp['weapon_data'][self.weapon]['cooldown']


    def get_status(self):

        # Idle
        idle = (self.direction.x == 0 and self.direction.y == 0)

        # Get users dir
        status_dir = self.status.split('_')[0]

        if self.attacking :
            self.direction.x = 0
            self.direction.y = 0
            if 'attack' not in self.status:
                self.status = status_dir + '_attack'
        # elif not self.attacking:
        #     self.status = status_dir
        elif idle and not self.attacking and 'idle' not in self.status:
            self.status = status_dir + '_idle'
            


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

    def cooldowns(self):
        '''
        Cooldowns for user actions.
        '''
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if (current_time - self.attack_time) >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()
        
        if not self.can_switch_weapon:
            if (current_time - self.weapon_switch_time) >= self.switch_duration_cooldown:
                self.can_switch_weapon = True
                self.weapon_switch_time = None

    def animate(self):
        animations = self.animations[self.status]

        self.frame_index = (self.frame_index + self.animation_speed) % len(animations)
        
        self.image = animations[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move()

