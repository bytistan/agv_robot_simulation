import pygame 
from settings import * 

class QrCode(pygame.sprite.Sprite):
    def __init__(self,pos,name):
        super().__init__()

        self.image = pygame.Surface((10,10))
        self.image.fill("#f03e3e")

        center = (size-10) / 2
        
        self.rect = self.image.get_rect(topleft=(pos[0]+center,pos[1]+center))
        self.name = name
