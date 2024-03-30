import pygame 
from settings import * 
from time import sleep 
from obstacle_sensor import ObstacleSensor
from datetime import datetime 

class Robot(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((size/2,size/2))
        self.image.fill("#66d9e8")
        self.rect = self.image.get_rect(
            topleft=(pos[0]+(size-size/2)/2,pos[1]+(size-size/2)/2)
        )

        self.direction = pygame.math.Vector2()
        self.obstacles_sensor = self.create_obstacles_sensor()

        self.mission = []
        
    def line_control(self,line):
        count = 0 

        for sprite in line.sprites():
            if sprite.rect.colliderect(self.rect):
                count += 1 
        
        return count 

    def qr_code_reader(self,qr_code):
        
        for sprite in qr_code.sprites():
            if sprite.rect.colliderect(self.rect):
                return sprite 
        
        return False 
        
    def go_target(self,target):
        target = [target[0] + (size-size/2)/2, target[1] + (size-size/2)/2]
        if self.rect.x > target[0] and self.direction.x != 1:
            self.direction.y = 0
            self.direction.x = -1 
        elif self.rect.x < target[0] and self.direction.x != -1:
            self.direction.y = 0
            self.direction.x = 1
        elif self.rect.y > target[1] and self.direction.y != 1:
            self.direction.y = -1
            self.direction.x = 0 
        elif self.rect.y < target[1] and self.direction.y != -1:
            self.direction.y = 1
            self.direction.x = 0

    def on(self,qr_code,line,load):
        total = self.line_control(line) 

    def create_obstacles_sensor(self):
        obstacles_sensor = pygame.sprite.Group()
        obstacles_sensor.add(ObstacleSensor((self.rect.x-5,self.rect.y-5),0))
        obstacles_sensor.add(ObstacleSensor((self.rect.x+size/2-5,self.rect.y-5),1))
        obstacles_sensor.add(ObstacleSensor((self.rect.x+size/2-5,self.rect.y+size/2-5),2))
        obstacles_sensor.add(ObstacleSensor((self.rect.x-5,self.rect.y+size/2-5),3))
        return obstacles_sensor
    
    def appy_speed(self):

        self.rect.x += self.direction.x * self.speed 
        self.rect.y += self.direction.y * self.speed 

    def update_tools(self,obstacles):
        pass 
                            
    def update(self,qr_code,line,load,obstacles):
        if self.load:
           self.load.rect.x = self.rect.x + 10 
           self.load.rect.y = self.rect.y + 10  

        self.obstacles_sensor.draw(pygame.display.get_surface())
        self.obstacles_sensor.update()
        self.update_tools(obstacles)

        if self.mission:
            self.on(qr_code,line,load)
            self.appy_speed()
        else:
            self.direction.x = 0
            self.direction.y = 0