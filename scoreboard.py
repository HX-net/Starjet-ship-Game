import pygame
class scoreboard:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.width , self.height = 200 , 70
        self.button_color = (0,0,0)
        self.rect = pygame.Rect(1350,0,self.width,self.height)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,80)
        self.prep_score()

    def prep_score(self):
        self.score_str = str(self.stats.score)
        self.score_img = self.font.render(self.score_str,True,self.text_color,self.settings.BG_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 
        self.score_rect.top = 10

    def show_score(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.score_img,self.score_rect)


        


