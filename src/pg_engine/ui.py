import pygame
from user_input_data import uinp
from .globals import GRAPHICS_DIR


BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80

HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None,30)

        # bar setup
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        # Import weapon data images.
        self.weapon_graphics = [pygame.image.load(GRAPHICS_DIR / x['graphic']).convert_alpha() for x in uinp['weapon_data'].values()]
        self.magic_graphics = [pygame.image.load(GRAPHICS_DIR / x['graphic']).convert_alpha() for x in uinp['magic_data'].values()]
    
    def show_bar(self, stat, stat_max, bg_rect, color):
        # draw background and outline.
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # Ratio the current stat in pixels to create a current stat.
        ratio = stat / stat_max
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface, color, current_rect)

        # Draw a border inner for style
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def show_exp(self, exp):
        # Get the locations to draw
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20

        # Write the words and background        
        text_surf = self.font.render(f"Exp : {str(int(exp))}", False, TEXT_COLOR)
        text_rect = text_surf.get_rect(bottomright = (x,y))
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect)

        self.display_surface.blit(text_surf, text_rect)

    def selection_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        if not has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
        return bg_rect

    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(10, 625, has_switched) # Equiped weapon
        
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center=bg_rect.center)

        self.display_surface.blit(weapon_surf, weapon_rect)
    
    def magic_overlay(self, magic_index, has_switched):
        bg_rect = self.selection_box(80, 635, has_switched) # Equiped weapon
        
        weapon_surf = self.magic_graphics[magic_index]
        weapon_rect = weapon_surf.get_rect(center=bg_rect.center)

        self.display_surface.blit(weapon_surf, weapon_rect)
        

    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)
        
        self.show_exp(player.exp)
        self.weapon_overlay(player.weapon_index, player.can_switch_weapon)
        self.magic_overlay(player.magic_index, player.can_switch_magic)