import pygame
from pygame.sprite import Sprite
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import HAMMER

class Shoot (Sprite):
    def __init__(self):
        self.dinosaur = Dinosaur()
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rectcenter = (self.dinosaur.dino_rect.x + 100, self.dinosaur.dino_rect.y + 20)
        self.speed_hammer = 100
        self.hammer = False
        self.tiro = False

    def update(self, user_Input):
        if user_Input[pygame.K_z] and not self.tiro:
            self.tiro = True
            self.hammer = True
            self.rect.x += self.speed_hammer
             
    
        





