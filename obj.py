from settings import * 
import pygame 

class Obj(pygame.sprite.Sprite):
    def __init__(self,pos,name,img):
        super().__init__()
        self.image = pygame.Surface((size-30,size-30))
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (size-20, size-20))
        self.rect = self.image.get_rect(topleft=(pos[0]+15,pos[1]+15))
        self.name = name 