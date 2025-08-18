import pygame
from user_input_data import uinp
from .globals import MAP_DIR
from csv import reader

def import_csv_layout(path_arr):
    # Get filepath
    path = MAP_DIR
    for fn in path_arr:
        path = path / fn
    
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        terrain_map = [list(row) for row in layout]

    return terrain_map