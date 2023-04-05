import random
import pygame

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus

from dino_runner.utils.constants import CACTUS, BIRD, SHIELD_TYPE


class ObstacleManager:
    

    def __init__(self) :
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus = Cactus(CACTUS)
            bird = Bird(BIRD)


            if random.randint(0,1) == 1:
                self.obstacles.append(cactus)
            
            else:
                self.obstacles.append(bird)

        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type != SHIELD_TYPE:
                    pygame.time.delay(1000)
                    game.death_count.update()
                    game.playing = False
                    break
                else:
                    self.obstacles.remove(obstacle)
                
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen) 

    def reset_obstacles(self):
        self.obstacles = []  