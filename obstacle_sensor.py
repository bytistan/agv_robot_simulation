import pygame 
from settings import * 

class ObstacleSensor(pygame.sprite.Sprite):
    def __init__(self,pos,direction):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill("#845ef7")
        self.rect = self.image.get_rect(topleft=pos)
        self.laser = self.create_laser(direction)

    def create_laser(self,direction):
        laser = pygame.sprite.Group()
        center = (10-4)/2
        if direction == 0:
            laser.add(Laser((self.rect.x+center*2+1,self.rect.y-40 + center),(4,40),0))
            laser.add(Laser((self.rect.x-40+center*2+1,self.rect.y + center),(40,4),3)) 
        if direction == 1:
            laser.add(Laser((self.rect.x+center,self.rect.y-40+center),(4,40),0))
            laser.add(Laser((self.rect.x+center,self.rect.y+center),(40,4),1)) 
        if direction == 2:
            laser.add(Laser((self.rect.x+center,self.rect.y+center),(4,40),2))
            laser.add(Laser((self.rect.x+center,self.rect.y+center),(40,4),1)) 
        if direction == 3:
            laser.add(Laser((self.rect.x+center*2+1,self.rect.y+center),(4,40),2))
            laser.add(Laser((self.rect.x-40+center*2+1,self.rect.y+center),(40,4),3)) 
        return laser 
    
    def update(self):
        self.laser.draw(pygame.display.get_surface()) 
        
class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,size,name):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill("#e64980")
        self.rect = self.image.get_rect(topleft=pos)
        self.name = name 