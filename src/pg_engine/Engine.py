import pygame, sys
from user_input_data import uinp



class Engine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((uinp['width'], uinp['height']))
        self.clock = pygame.time.Clock()

    def run(self):
        while 1:
            for event in pygame.event.get():
                # X box
                if event.type == pygame.QUIT:
                    print('GOTCHA')
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(uinp['fps_target'])
