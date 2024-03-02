from settings import * 
import pygame 

class Load(pygame.sprite.Sprite):
    def __init__(self,pos,name,img):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(topleft=(pos[0]+35,pos[1]+35))
        self.name = name