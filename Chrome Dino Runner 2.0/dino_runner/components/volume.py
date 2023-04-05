import pygame

from dino_runner.utils.constants import  VOL_MUTE, VOL_MAX, VOL_MIN, VOL_UP

class Volume:
    def __init__(self):
        self.x_pos_volume = 500
        self.y_pos_volume = 10


    def config_vol(self, keys, screen):       #CONFIGURACION VOLUMEN DEL JUEGO
        
        if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
            screen.blit(VOL_MIN, (self.x_pos_volume, self.y_pos_volume))

        elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
            screen.blit(VOL_MUTE, (self.x_pos_volume, self.y_pos_volume))
        
        if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
                 pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
                 screen.blit(VOL_UP, (self.x_pos_volume, self.y_pos_volume))

        elif keys [pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
                screen.blit(VOL_MAX, (self.x_pos_volume, self.y_pos_volume))

        elif keys[pygame.K_m]:
                pygame.mixer.music.set_volume(0.0)
                screen.blit(VOL_MUTE, (self.x_pos_volume, self.y_pos_volume))

        elif keys[pygame.K_COMMA]:
                pygame.mixer.music.set_volume(1.0)
                screen.blit(VOL_MAX, (self.x_pos_volume, self.y_pos_volume))

        pygame.display.update()
