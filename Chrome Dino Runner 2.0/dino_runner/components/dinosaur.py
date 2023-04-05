import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, RUNNING_SHIELD, DUCKING_SHIELD, JUMPING_SHIELD, DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, DUCKING_HAMMER, JUMPING_HAMMER, RUNNING_HAMMER


RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
JUM_IMG = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}


class Dinosaur (Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340        #POSICION EN DUCK
    JUMP_SPEED = 8.5        #CUANTO VA A TARDAR EN CAER

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.jump_speed = self.JUMP_SPEED  

        self.has_power_up = False
        self.power_time_up = 0

        self.sound_jump = pygame.mixer.Sound('jump.wav')    #Sonido Jumping

        self.dino_run = True
        self.dino_jump = False  
        self.dino_duck = False
    
    def update(self, user_Input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if (user_Input[pygame.K_UP] or user_Input[pygame.K_SPACE]) and not self.dino_jump:
            self.sound_jump.play()
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False

        elif user_Input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
                
        elif not (self.dino_jump or user_Input[pygame.K_DOWN]):
            self.dino_jump = False
            self.dino_run = True 
            self.dino_duck = False

        if self.step_index >= 10:
            self.step_index = 0


    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump (self):
        self.image = JUM_IMG[self.type]
        self.dino_rect.y -= self.jump_speed *4
        self.jump_speed -= 0.8

        if self.jump_speed  < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED
        
    def duck (self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1
    
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


    def reset_dino(self):
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_speed = self.JUMP_SPEED


 
        
        





