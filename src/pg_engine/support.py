import pygame
from user_input_data import uinp
from .globals import MAP_DIR, GRAPHICS_DIR
from csv import reader
from os import walk

def import_csv_layout(path_arr):
    # Get filepath
    path = MAP_DIR
    for fn in path_arr:
        path = path / fn
    
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        terrain_map = [list(row) for row in layout]

    return terrain_map

def import_folder(path):
    surface_list = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path / image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
