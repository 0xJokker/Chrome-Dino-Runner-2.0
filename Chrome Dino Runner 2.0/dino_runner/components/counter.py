import pygame

from dino_runner.utils.constants import FONT_STYLE


class Counter:
  def __init__(self):
    self.count = 0
    

  def update(self):
    self.count += 1
    
  def draw(self, screen, color):
    if color == True:
      font = pygame.font.Font(FONT_STYLE, 30)
      text = font.render(f'Score: {self.count}', True, (0, 0, 0))
      text_rect = text.get_rect()
      text_rect.center = (1000, 50)
      screen.blit(text, text_rect)
      
    elif color == False:
      font = pygame.font.Font(FONT_STYLE, 30)
      text = font.render(f'Score: {self.count}', True, (255, 255, 255))
      text_rect = text.get_rect()
      text_rect.center = (1000, 50)
      screen.blit(text, text_rect)

  def reset(self):
    self.count = 0
    
  def set_count(self, value):
    self.count = value
