import pygame
class ship():
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        #speed
        self.ship_speed = 3

        #load ships
        self.image = pygame.image.load('Spaceships/1.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.lokx = float(self.rect.x)
        self.loky = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def upadte(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.lokx += self.ship_speed 
        if self.moving_left  and self.rect.left > 0:
            self.lokx -= self.ship_speed 
        if self.moving_up  and self.rect.top > 0:
            self.loky -= self.ship_speed 
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.loky += self.ship_speed 
        


        self.rect.y = self.loky
        self.rect.x = self.lokx    

    def reset_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.lokx = float(self.rect.x)
        self.loky = float(self.rect.y)