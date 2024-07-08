from settings import * 
import pygame 

class Obstacles(pygame.sprite.Sprite):
    def __init__(self,pos,img):
        super().__init__()
        
        self.image = pygame.Surface((size-60,size-60))
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (size-50, size-50))

        self.rect = self.image.get_rect(topleft=(pos[0]+30,pos[1]+30))
