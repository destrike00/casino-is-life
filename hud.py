import random
from user import *
import pygame
from settings import *

class Hud:
    def __init__(self, user):
        self.user = user
        self.display_surface = pygame.display.get_surface()
        try:
            self.font, self.bet_font = pygame.font.Font(FONT_STYLE, FONT_SIZE), pygame.font.Font(FONT_STYLE, FONT_SIZE)
            self.win_font = pygame.font.Font(FONT_STYLE, BIG_FONT_SIZE)
        except:
            print("Couldn't load font!")
            quit()
        self.win_text_angle = random.randint(-4, 4)

    def get_userdata(self):
        user_data=self.user.get_data()
        balance_surf = self.font.render("Balance:" + user_data['balance']+" HUF", True, "white", None)
        bet_surf=self.font.render("Bet:" + user_data['balance']+" HUF", True, "white", None)

        x, y = 20, self.display_surface.get_size()[1] - 30
        balance_rect = balance_surf.get_rect(bottomleft=(x, y))

        x = self.display_surface.get_size()[0] - 20
        bet_rect = bet_surf.get_rect(bottomright=(x, y))
        pygame.draw.rect(self.display_surface, False, balance_rect)
        pygame.draw.rect(self.display_surface, False, bet_rect)
        self.display_surface.blit(balance_surf, balance_rect)
        self.display_surface.blit(bet_surf, bet_rect)

    def update(self):
        pygame.draw.rect(self.display_surface, 'Black', pygame.Rect(0, 900, 1600, 100))
        self.display_info()