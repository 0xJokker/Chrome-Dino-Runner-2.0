import pygame
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_WIDTH

class Meteor(Obstacle):     #Hereda el comportamiento de Obstacle
    def __init__(self, image):
        self.type = random.randint(0,1)            
        super().__init__(image, self.type)             
        
        if self.type == 0:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = -self.rect.width
        

        
        #self.speed = random.randrange(1, 10)

           