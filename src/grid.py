

class Grid:
    def __init__(self, input_dict):
        self.map_width = input_dict['width']
        self.map_height = input_dict['height']
        self.grid_x_y = input_dict['grid_cell_size']