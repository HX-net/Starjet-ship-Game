import sys
import pygame
from theme import setting
from Ship import ship 
from bullet import Bullet
from alien import Alien
from time import sleep
from game_states import gamestats
from button import button
from scoreboard import scoreboard


num_ships = 0
class start:
    def __init__(self):
        pygame.init()
        self.haert_list=[pygame.image.load('other/3haert.png'),pygame.image.load('other/2haert.png'),pygame.image.load('other/1haert.png'),pygame.image.load('other/0haert.png')]
        self.game_active = False
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings = setting(self)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        self.stats = gamestats(self)
        self.sb = scoreboard(self)

        
        pygame.display.set_caption("Star Jet")

        self.ship = ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = gamestats(self)
        self._creat_fleet()


        self.play_buttton = button(self,"Play")

    def _creat_fleet(self):
        alien =Alien(self)
        screen_width = self.settings.screen_width
        screen_height = self.settings.screen_height
        alien_width , alien_height = alien.rect.size

        ship_height = self.ship.rect.height

        avaolable_space_x = screen_width - (alien_width)
        number_aliens_x = avaolable_space_x // (1.5*alien_width)
        avaolable_space_y = screen_height- (alien_height + ship_height)

        numbers_rows = avaolable_space_y // (1.6 * alien_height) 
        for row_number in range(int(numbers_rows)):
            for alien_number in range(int(number_aliens_x)):
                self._creat_alien(alien_number,row_number)

    def _creat_alien(self,alien_number,row_number):
            alien = Alien(self)
            alien_width , alien_height = alien.rect.size
            alien.x = alien_width + (1.5*alien_width*alien_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height +(1.25*alien.rect.height * row_number)
            self.aliens.add(alien)


        

    def run_game(self):
        while True:
            self._check_event()
            if self.game_active:
                self.ship.upadte()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _update_aliens(self):
        self.aliens.update()
        self._check_fleet_edges()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    
    def _ship_hit(self):
        if self.stats.ship_left > 0 :
            self.stats.ship_left -= 1
            self.settings.ship_limit -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._creat_fleet()
            self.ship.reset_ship()
            if  self.stats.ship_left == 1: 
                self.settings.haert = self.haert_list[1]
            if  self.stats.ship_left == 0: 
                self.settings.haert = self.haert_list[2]
            if  self.stats.ship_left == -1: 
                self.settings.haert = self.haert_list[3]
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
            self.settings.iniatialize_dynamic_setting()
        sleep(2.0)
        
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien  in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)
        self._check_bullets_aliens_collision()

    def _check_bullets_aliens_collision(self):
        collision = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collision:
            self.stats.score += self.settings.alien_point
            self.sb.prep_score()
        if not self.aliens:
            self.bullets.empty()
            self._creat_fleet()
            self.settings.increase_speed()

    def _check_event(self):
        ships_list=[pygame.image.load('Spaceships/1.png'),pygame.image.load('Spaceships/2.png'),pygame.image.load('Spaceships/3.png'),pygame.image.load('Spaceships/4.png'),pygame.image.load('Spaceships/5.png'),pygame.image.load('Spaceships/6.png'),pygame.image.load('Spaceships/7.png'),pygame.image.load('Spaceships/8.png'),pygame.image.load('Spaceships/9.png')]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event,ships_list)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self,mouse_pos):
        button_clicked = self.play_buttton.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            if self.play_buttton.rect.collidepoint(mouse_pos):
                self.stats._reset_stats()
                self.settings.active = True
                self.game_active = True
                self.settings.ship_limit = 2
                self.stats.ship_left = 2
                self.settings.haert = self.haert_list[0]
                self.aliens.empty()
                self.bullets.empty()
                self._creat_fleet()
                self.ship.reset_ship()    
                pygame.mouse.set_visible(False)        
                sleep(1.0)


                
    def _check_keydown_event(self,event,ships_list):
        global num_ships
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_F2:
            num_ships = num_ships + 1
            if num_ships > 8 :
                num_ships = 0
            self.ship.image = ships_list[num_ships]
        if event.key == pygame.K_F1:
            num_ships = num_ships - 1
            if num_ships < 0 :
                num_ships = 8
            self.ship.image = ships_list[num_ships]
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) <  self.settings.bullet_allowed:
            #playsound('fire.mp3')
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)



    def _update_screen(self):
        self.settings.blitme()
        if self.game_active:
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)
            self.sb.show_score()
        if not self.game_active:
            self.play_buttton.draw_button()
        pygame.display.flip()

        


if __name__ == "__main__":
    ai = start()
    ai.run_game()