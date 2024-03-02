import pygame 

class Line(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill('#343a40')
        self.rect = self.image.get_rect(topleft=pos)