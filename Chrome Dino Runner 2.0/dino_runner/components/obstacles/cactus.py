import random
from dino_runner.components.obstacles.obstacle import Obstacle



class Cactus(Obstacle):     #Hereda el comportamiento de Obstacle
    def __init__(self, image):
        self.type = random.randint(0,5)                 
        super().__init__(image, self.type)             
        
        if self.type in range(3,5):
            self.rect.y = 300
        elif self.type == 5 :
            self.rect.y = 300
        else:
            self.rect.y = 325






