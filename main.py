import pygame 
import sys 
from settings import *
from simulation_controller import SimulationController

class Main:        
    def setup(self):
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        self.simulation_controller = SimulationController()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
    def run(self):
        self.setup()

        while True:
            try:
                self.clock.tick(fps)
                self.event()
                self.screen.fill('white')
                self.simulation_controller.run()
                pygame.display.update()
            except KeyboardInterrupt:
                print("[-] Simulation DOWN.")
                sys.exit()

if __name__ == '__main__':
    main = Main()
    main.run()