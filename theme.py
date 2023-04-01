import pygame
class setting:
    def __init__(self,ai_game):
        self.active = ai_game.game_active
        #BG
        self.BG_color=(0,0,0)
        self.screen_width= 1200
        self.screen_height = 700
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.BG_image = pygame.image.load('BG/2.png')
        self.Play_BG_image = pygame.image.load('BG/Play_BG.png')
        self.BG_rect = self.BG_image.get_rect()
        self.BG_rect.width = self.screen_width
        self.BG_rect.height = self.screen_height
        # Bullet setting
        self.bullet_width = 80
        self.bullet_height = 15
        self.bullet_color = (250,253,15)
        self.bullet_allowed = 8
        #alien setting
        
        self.fleet_drop_speed = 15
        #ship
        self.ship_limit = 2
        #haert
        self.haert = pygame.image.load('other/3haert.png')
        self.haert_rect = self.haert.get_rect()
        self.haert_rect.left = self.screen_rect.left
        self.haert_rect.top = self.screen_rect.top

        self.speedup_scale = 1.4

        self.iniatialize_dynamic_setting()
        
    def iniatialize_dynamic_setting(self):
        self.alien_speed = 1.0
        self.bullet_speed = 5
        self.ship_speed = 3
        self.fleet_direction = 1
        self.alien_point = 1

    def increase_speed(self):
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_point = self.alien_point * self.speedup_scale

    def blitme(self):
        if not self.active:
            self.screen.blit(self.Play_BG_image,self.BG_rect)
        else:
            self.screen.blit(self.BG_image,self.BG_rect)
            self.screen.blit(self.haert,self.haert_rect)

        