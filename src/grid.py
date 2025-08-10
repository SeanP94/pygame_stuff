import pygame

GRID_COLOR = 'cornflowerblue'

class Grid:
    def __init__(self, input_dict):
        self.map_width = input_dict['width']
        self.map_height = input_dict['height']
        self.grid_x_y = input_dict['grid_cell_size']

    def update(self, input_dict):
        # Call when settings change.
        self.map_width = input_dict['width']
        self.map_height = input_dict['height']
        self.grid_x_y = input_dict['grid_cell_size']


    def draw_grid(self, pygame, surface=None):
        grid_w = self.map_width // self.grid_x_y
        grid_h = self.map_height // self.grid_x_y

        x_pos = self.grid_x_y
        end_x_pos = self.map_width - self.grid_x_y

        y_pos = self.grid_x_y
        end_y_pos = self.map_height - self.grid_x_y
        print(';p')
        for row in range(grid_h):
            pygame.draw.line(
                surface,
                (255,255,255),
                (x_pos, 0),
                (x_pos, 1)
            )
        # for cell in range(grid_w):
