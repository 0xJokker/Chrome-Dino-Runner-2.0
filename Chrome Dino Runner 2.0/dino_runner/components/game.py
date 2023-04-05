import pygame
import random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, GAME_OVER
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.volume import Volume
from dino_runner.components.clouds import Cloud
from dino_runner.components.counter import Counter
from dino_runner.components.power_ups.power_up_manager import PowerUpManager



class Game:
    GAME_SPEED = 20

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.menu = Menu(self.screen)
        self.running = False
        self.music = False
        self.color_screen = True



        self.volume = Volume()
        self.cloud = Cloud()

        self.score = Counter()
        self.death_count = Counter()
        self.highest_score = Counter()
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.reset_game()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            pygame.mixer.music.unpause()
            self.sound_game()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        
        self.volume_config()


    def sound_game(self):
        if not self.music:
            pygame.mixer.music.load('sound1.mp3')
            pygame.mixer.music.play(-1)
            self.music = True

    def volume_config(self):
        keys = pygame.key.get_pressed()
        self.volume.config_vol(keys, self.screen)


    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.score.update()
        self.update_game_speed()
        self.cloud.update(self)

    def draw(self):
        self.clock.tick(FPS)
        #self.screen.fill((255, 255, 255))
        self.paint_draw()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.score.draw(self.screen, self.color_screen)
        self.cloud.draw(self.screen)
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def show_menu(self):
        pygame.mixer.music.pause()
        self.color_screen = True
        self.menu.reset_screen_color(self.screen)

        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        if self.death_count.count == 0:
            self.menu.draw(self.screen, 'Press any key to start ...')
            self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))
        else:
            self.update_highest_score()
            self.menu.draw(self.screen, 'Press any key to restart')
            self.menu.draw(self.screen, f'Your Score: {self.score.count}', half_screen_width, 350, )
            self.menu.draw(self.screen, f'Highest Score: {self.highest_score.count}', half_screen_width, 400, )
            self.menu.draw(self.screen, f'Total Deaths: {self.death_count.count}', half_screen_width, 450, )
            
            self.screen.blit(GAME_OVER, (half_screen_width - 180, half_screen_height - 200))
            self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))
        
        self.menu.update(self)
        

    def update_game_speed(self):
        if self.score.count % 100 == 0 and self.game_speed < 500:
            self.game_speed += 3
        
        if self.score.count == 1000:
            self.color_screen = False
        
    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)
            

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.score.reset()
        self.game_speed = self.GAME_SPEED
        self.player.reset_dino()
        self.power_up_manager.reset_power_ups()
    
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)
            
            if time_to_show >= 0:
                self.menu.draw(self.screen, f'{self.player.type.capitalize()} enable for {time_to_show} seconds', 500, 50)
            else:
                self.has_power_up = False
                self.player.type = DEFAULT_TYPE
    
    #Cambia color de la pantalla dependiendo al SCORE
    def paint_draw(self):
        if self.color_screen == True:
            self.screen.fill((255, 255, 255))
 
        elif self.color_screen == False:
            self.screen.fill((0, 0, 0))   
            