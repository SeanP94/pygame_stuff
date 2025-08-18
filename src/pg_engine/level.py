import pygame
from user_input_data import uinp
from .tile import Tile
from .player import Player
from .camera import YSortCameraGroup
from .support import import_csv_layout


class Level:
    def __init__(self):
        # Get the display surface.
        self.display_surface = pygame.display.get_surface()

        # Camera group to draw.
        self.visible_sprites = YSortCameraGroup()
        # Map obstacles
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        
        layouts = {
            # Store the bounder of the map
            'boundary' : import_csv_layout(['map_FloorBlocks.csv'])
        }

        for style, layout in layouts.items():
            for ridx, row in enumerate(layout):
                for cidx, col in enumerate(row):
                    # 
                    if col != '-1':
                        # Pos on mapgrid
                        x = cidx * uinp['grid_cell_size']
                        y = ridx * uinp['grid_cell_size']
                        
                        if style == 'boundary':
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'invisible')
                    
        # for y_index, row in enumerate(uinp['world_map']):
        #     for x_index, cell in enumerate(row):
        #         x = x_index * uinp['grid_cell_size']
        #         y = y_index * uinp['grid_cell_size']
        #         if cell == 'x':
        #             Tile((x,y), [self.visible_sprites, self.obstacle_sprites], ['test', 'rock.png'])
        #         elif cell == 'p':
        #             self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites)
        self.player = Player((1000, 430), [self.visible_sprites], self.obstacle_sprites)




    def run(self):
        # self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()