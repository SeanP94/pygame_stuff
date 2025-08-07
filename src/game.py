import pygame
from user_input_data import UserInput

# Variables
game_settings = UserInput().get_uinp()


# Setup Pygame
pygame.init()
pygame.display.set_caption(game_settings['game_name'])

screen = pygame.display.set_mode((game_settings['width'], game_settings['height']))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # X button
            exit()


    pygame.display.update()



# if __name__ == '__main__':


