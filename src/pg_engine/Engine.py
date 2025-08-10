import pygame
from user_input_data import UserInput
from grid import Grid

# Variables
game_settings = UserInput().get_uinp()

grid_obj = Grid(game_settings)


# Setup Pygame
pygame.init()
pygame.display.set_caption(game_settings['game_name'])

screen = pygame.display.set_mode((game_settings['width'], game_settings['height']))
clock = pygame.time.Clock()
gamefont = pygame.font.Font(None, 50)



# Temp surfaces to remove later.
# bg_surface = pygame.image.load('graphics/Sky.png')
# ground_surface = pygame.image.load('graphics/ground.png')

text_surface = gamefont.render('Score : 0', False, 'Black')
# This is going to be the one I use for the grid To learn. 
'''
TODO: 
    - I want to set the size of the surface and stretch it to the screen.
    - 
'''
game_surface = pygame.Surface((game_settings['width'], game_settings['height']))



# Pygame Functions

def event_loop():
    # Control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # X button
            exit()

def draw():
    # Draw BG
    # screen.blit(bg_surface, (0,0))
    # screen.blit(ground_surface, (
    #      0,
    #      bg_surface.get_height() # Place at bottom of bg_surface
    # ))

    # Draw text.
    # grid_obj.draw_grid(pygame, screen)
    # screen.blit(text_surface, (300, 50))

def game_loop():
    while True:
        event_loop()
        draw()
        pygame.display.update()
        clock.tick(game_settings['fps_target'])

