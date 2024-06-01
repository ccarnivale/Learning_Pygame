import pygame, sys
from player import Player
from settings import *
from level import Level 

#initiates pygame for playing the sounds produce images
#pygame.init()

#create a screen for the game 
#screen =  pygame.display.set_mode((1910,1080))
#pygame.display.set_caption("From Mummer to Legend")
#creates a time object for use
#clock = pygame.time.Clock()

#Incorporating all of the vars above into a game class and then use a "run" method for game class to include the running game loop.
#Sourcing the settings into additional helper files.

class Game:
    def __init__(self):
        pygame.init() #from line 6...initializes the pygame module for everything the pygame "engine" does.
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.name = pygame.display.set_caption("From Mummer to Legend")
        self.level = Level()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
                    
            dt = self.clock.tick()/1000
            self.level.run(dt)
            pygame.display.update()
    
    #draw all elements
    #update everything as it happens
    #pygame.display.update()
    #clock.tick(60)
    
if __name__ == '__main__':
    game = Game()
    game.run()    