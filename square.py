import pygame 
from settings import * 

class Square(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((size-10,size-10))
        self.image.fill("#e9ecef")
        self.rect = self.image.get_rect(topleft=(pos[0]+5,pos[1]+5))