import pygame
from settings import *
from player import Player

class Level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        
        #Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.setup()
        
    def setup(self):
        self.player = Player((100,100), self.all_sprites)

#dt is delta time and important for any updating steps so they are all updated on the same timescale        
    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)