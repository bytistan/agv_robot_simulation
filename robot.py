import pygame 
from settings import * 
from obstacle_sensor import ObstacleSensor

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

        self.speed = 5
        self.mission = ["S2","A","S1","C"]
        
        self.flag = True
        self.laser_info = []
        
        self.mode = {
            "line_center":None,
            "obstacle_avoider":None
        } 

        self.step = 0
        
        self.data = {
            "line_status":None,
            "distance_sensor":None,
            "qr_code":None,
            "load":None
        }
        
        self.stop = False 

        self.destination_x = False
        self.destination_y = False

        self.tolerance = 10

    def qr_code_reader(self,qr_code):
        for sprite in qr_code.sprites():
            if sprite.rect.colliderect(self.rect):
                return sprite
        
        return False 
    
    def line_reader(self,lines):
        c = 0
        for sprite in lines.sprites():
            if sprite.rect.colliderect(self.rect):
                c += 1    
        return c

    def guidance(self,l):
        cor = obj_cordinate.get(self.mission[0])

        cor_x = cor[0] + (size // 2) + 5 
        cor_y = cor[1] + (size // 2) + 5 
        
        rob_x = self.rect.x + (size // 4)
        rob_y = self.rect.y + (size // 4)
       
        target_vertical = 1 if cor_y > rob_y else -1 
        target_horizontal = 1 if cor_x > rob_x > 0 else -1 
        
        robot_horizontall_axis = (0 < rob_y < (size // 2)) or (height-(size//2) < rob_y < height)
        
        self.destination_x = False
        self.destination_y = False

        if rob_x  < cor_x < rob_x + self.tolerance:
            self.destination_x = True 
        
        if rob_y < cor_y < rob_y + self.tolerance:
            self.destination_y = True 
        
        pygame.draw.circle(pygame.display.get_surface(), (0,255,0), (cor_x, cor_y), 10) 

        if l > 1: 
            if self.destination_x:
                self.direction.y = target_vertical
                self.direction.x = 0

            elif robot_horizontall_axis:
                self.direction.x = target_horizontal
                self.direction.y = 0

            elif not self.destination_y:
                self.direction.y = 1 if rob_y > height // 2 else -1  
                self.direction.x = 0

    def find_protocol(self):
        for m,protocols in self.mode.items():
            if protocols:
                for index,protocol in enumerate(protocols): 
                    if protocol and not protocol.get("completed"):
                        return protocol,m,index 
                self.mode[m] = None 
        return None
    
    def do_procotol(self,protocol,m,index,l):
        if not protocol.get("process"):
            move = protocol.get("move")

            x,y = move.get("x") ,move.get("y")
            
            if x and self.direction.x != x: self.direction.x = x
            if y and self.direction.y != y: self.direction.y = y
            
            self.mode[m][index]["process"] = True 

        to = protocol.get("to")
        cor = to.get("cor")
        line = to.get("line")

        cor_x = cor.get("x")
        cor_y = cor.get("y")

        rob_x = self.rect.x
        rob_y = self.rect.y

        if cor_x and self.direction.x != 0:
            if rob_x - (size // 4) > cor_x > rob_x - ((size // 2) + (size // 4)):
                self.mode[m][index]["completed"] = True 
                self.mode[m][index]["process"] = False 
                self.mission.pop(0)   
                self.guidance_flag = True

        if cor_y and self.direction.y != 0:
            if rob_y - (size // 4) > cor_y > rob_y - ((size // 2) + (size // 4)):
                self.mode[m][index]["completed"] = True 
                self.mode[m][index]["process"] = False 
                self.mission.pop(0)   
                self.guidance_flag = True

        if line and l > line:
            self.mode[m][index]["completed"] = True 
            self.mode[m][index]["process"] = False 

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
        self.laser_info.clear()

        for sprite in self.obstacles_sensor.sprites():
            f = False

            sprite.rect.x += self.direction.x * self.speed
            sprite.rect.y += self.direction.y * self.speed 

            for s in sprite.laser.sprites():
                
                s.rect.x += self.direction.x * self.speed
                s.rect.y += self.direction.y * self.speed 

                for obs in obstacles.sprites():

                    if obs.rect.colliderect(s.rect):
                        if ((s.name == 0 and self.direction.y == -1) or (s.name == 2 and self.direction.y == 1)):
                           f = True 
                        self.laser_info.append(s.name)
        return f

    def update(self,qr_code,line,load,obstacles):
        self.obstacles_sensor.draw(pygame.display.get_surface())
        self.obstacles_sensor.update()

        if not self.stop:
            obs = self.update_tools(obstacles)
            qr = self.qr_code_reader(qr_code) 
            l = self.line_reader(line)

            if qr and qr.name == self.mission[0] and self.destination_x and self.destination_y:
                self.mission.pop(0)

            if len(self.mission) > 0:
                self.guidance(l)

        if len(self.mission) == 0 and not self.stop:
            self.stop = True 
        
        if self.stop:
            self.direction.x = 0
            self.direction.y = 0

        self.appy_speed()
