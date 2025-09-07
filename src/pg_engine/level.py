import pygame
from user_input_data import uinp
from .tile import Tile
from .player import Player
from .camera import YSortCameraGroup
from .support import import_csv_layout, import_folder
from .globals import GRAPHICS_DIR
from .weapon import Weapon
from random import choice
from .debug import debug
from .ui import UI

class Level:
    def __init__(self):
        # Get the display surface.
        self.display_surface = pygame.display.get_surface()

        # Camera group to draw.
        self.visible_sprites = YSortCameraGroup()
        # Map obstacles
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

        # Attack logic
        self.current_attack = None

        # User Interface
        self.ui = UI()

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])
    
    def create_magic(self, style, strength, cost):
        print(style, strength, cost)

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def create_map(self):
        
        layouts = {
            # Store the bounder of the map
            'boundary' : import_csv_layout(['map_FloorBlocks.csv']),
            'grass' : import_csv_layout(['map_Grass.csv']),
            'object' : import_csv_layout(['map_Objects.csv'])
        }
        graphics = {
            'grass' : import_folder(GRAPHICS_DIR / 'Grass'),
            'objects' : import_folder(GRAPHICS_DIR / 'Objects')
        }

        for style, layout in layouts.items():
            for ridx, row in enumerate(layout):
                for cidx, col in enumerate(row):
                    if col != '-1':
                        # Pos on mapgrid
                        x = cidx * uinp['grid_cell_size']
                        y = ridx * uinp['grid_cell_size']
                        
                        if style == 'boundary':
                            Tile((x,y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            random_grass_img = choice(graphics['grass'])
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'grass', random_grass_img)
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
        self.player = Player((2000, 1400), [self.visible_sprites], self.obstacle_sprites, self.create_attack, self.destroy_attack, self.create_magic)



    def run(self):
        # self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)
        # debug(self.player.status)