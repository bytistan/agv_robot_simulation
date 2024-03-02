import pygame
from line import Line
from settings import * 
from load import Load
from obj import Obj
from obstacles import Obstacles
from qr_code import QrCode
from robot import Robot
from square import Square

class SimulationController():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.setup()

    def setup(self):
        self.square = self.create_square()
        self.line = self.create_line()
        self.obj = self.create_obj()
        self.qr_code = self.create_qr_code()
        self.obstacles = self.create_obstacles()
        self.robot = self.create_robot()
        self.load = self.create_loads()

    def calculate_line_size(self,size,l,w):
        pos = (size-l)/2
        line_size = w - (size*2) + (pos+l)*2
        return (pos,line_size)

    def create_line(self):
        line = pygame.sprite.Group()

        for x in range(5,width,size):
            data = self.calculate_line_size(size,10,height)
            l = Line((x+data[0],data[0]+5),(10,data[1]-10))
            line.add(l)

        data = self.calculate_line_size(size,10,width)
        l = Line((5+data[0],data[0]+5),(data[1]-10,10))
        line.add(l)

        data = self.calculate_line_size(size,10,width)
        l = Line((5+data[0],6*size+data[0]+5),(data[1]-10,10))
        line.add(l)

        return line
    
    def create_loads(self):
        load = pygame.sprite.Group()
        load.add(Load(obj_cordinate['A'],"A",'./images/cargo-box.png'))
        load.add(Load(obj_cordinate['D'],"D",'./images/cargo-box.png'))
        return load 
    
    def create_obj(self):  
        obj = pygame.sprite.Group()
        obj.add(Obj((size,size*3),"A",'./images/frame.png'))
        obj.add(Obj((size*2,size*3),"B",'./images/frame.png'))
        obj.add(Obj((size*4,size*3),"C",'./images/frame.png'))
        obj.add(Obj((size*5,size*3),"D",'./images/frame.png'))
        obj.add(Obj((size*3,0),"S1",'./images/frame.png'))
        obj.add(Obj((size*3,size*6),"S2",'./images/frame.png'))
        obj.add(Obj((0,0),"3",'./images/select.png'))
        obj.add(Obj((0,size*6),"4",'./images/select.png'))
        obj.add(Obj((size*6,size*6),"1",'./images/select.png'))
        obj.add(Obj((size*6,0),"2",'./images/select.png'))
        return obj 
    
    def create_obstacles(self):
        obstacles = pygame.sprite.Group()
        obstacles.add(Obstacles((size,size),"./images/wooden-box.png")) 
        obstacles.add(Obstacles((size*3,size*5),"./images/wooden-box.png"))
        obstacles.add(Obstacles((size*5,size),"./images/wooden-box.png"))  
        return obstacles
    
    def create_qr_code(self):
        qr_code = pygame.sprite.Group()
        for x in range(5,width,size):
            for y in range(5,height,size):
                name = None 
                for key,item in obj_cordinate.items():
                    if item == (x-5,y-5):
                        name = key
                qr_code.add(QrCode((x,y),name))
        return qr_code
    
    def create_robot(self):
        robot = pygame.sprite.GroupSingle()
        robot.add(Robot((size*3+5,0+5)))
        return robot
    
    def create_square(self):
        square = pygame.sprite.Group()
        for x in range(0,width,size):
            for y in range(0,height,size):
                s = Square((x+5,y+5))
                square.add(s)
        return square

    def draw(self):
        self.square.draw(self.display_surface)
        self.obj.draw(self.display_surface)
        self.line.draw(self.display_surface)
        self.qr_code.draw(self.display_surface)
        self.obstacles.draw(self.display_surface)
        self.robot.draw(self.display_surface)
        self.load.draw(self.display_surface)

    def run(self):
        self.draw()
        self.robot.sprite.update(self.qr_code,self.line,self.load,self.obstacles)