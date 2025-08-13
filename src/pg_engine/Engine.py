import pygame, sys
from .level import Level
from user_input_data import uinp
from .debug import debug

class Engine:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(uinp['game_name'])
        self.screen = pygame.display.set_mode((uinp['width'], uinp['height']))
        self.clock = pygame.time.Clock()
        self.level = Level()
        
    def run(self):
        while 1:
            self.screen.fill('black')
            for event in pygame.event.get():
                # X box
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            self.level.run()
            pygame.display.update()
            self.clock.tick(uinp['fps_target'])
