import pygame
from user_input_data import UserInput

# Variables
game_settings = UserInput().get_uinp()


# Setup Pygame
pygame.init()
pygame.display.set_caption(game_settings['game_name'])

screen = pygame.display.set_mode((game_settings['width'], game_settings['height']))
clock = pygame.time.Clock()
gamefont = pygame.font.Font(None, 50)


bg_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = gamefont.render('Score : 0', False, 'Black')

def event_loop():
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # X button
                    exit()

def draw():
    # Draw BG
    screen.blit(bg_surface, (0,0))
    screen.blit(ground_surface, (
         0,
         bg_surface.get_height() # Place at bottom of bg_surface
    ))

    # Draw text.
    screen.blit(text_surface, (300, 50))


def game_loop():
    while True:
        event_loop()
        draw()
        pygame.display.update()
        clock.tick(game_settings['fps_target'])



# if __name__ == '__main__':
#     game_loop()


