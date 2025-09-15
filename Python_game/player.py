import pygame
from settings import *
from support import *
import os
from os.path import join
from itertools import product
from timer import Timer

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        
        #has to be first b/c when you make image (next step) you need the animations dictionary to pull from.
        #create a dictionary to hold all of the player animations
        self.animations = {'up': [], 'down':[], 'left': [], 'right': []} 
        self.tool_animations = {'hoe': [], 'axe': [], 'water': []}
        # Create new list comprehension to generate animation names
        # this is to create a list of all the tool animation names for use in the sprite sheet import function. This is what is used in import_tool_assets()
        self.animation_names = [f'{animation}_{tool}'for tool, animation in product(self.tool_animations.keys(), self.animations.keys())]
        
        #Import the tool assets for the player
        self.import_assets()
        
        self.import_tool_assets('Basic Charakter Actions')
        #create status states to determine which animation to use
        self.status = 'down'
        #Setting the tool status to false so that the player is not using a tool at the start of the game.
        self.tool_status = False
        #create a starting index to use for animation loop
        self.frame_index = 0
        
        #Logic help to determine if the player is idle or not
        #if the player is idle, we want to use only the first two frames of the animation
        self.idle = True
        
        #load the first image to use for the player sprite
        # general setup
        #Conditional images based on if there is a tool being used or not
        #Will add seed use later
        self.image = self.animations[self.status][self.frame_index] #if not self.tool_status else self.tool_animations[self.status][self.frame_index]
        #self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)
        # Movement attributes instead of functional to be framerate indpendent and use delta time
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center) #this is needed b/c we are using delta time, which returns floats commonly...rects store as int() and not compatible with the dt approach
        self.speed = 100
        
        #tools section for player
        #default tool is hoe...will add ability to change tools later
        self.tool_index = 0
        self.tool = ['hoe', 'axe', 'water'][self.tool_index]   

        
        #Timers for all player actions
        self.timers = {'tool use': Timer(duration=350, func=self.use_tool)}
        
        
    #only doing a few movement animations in the dictionary for now to make sure I cut the sprite file correctly
    def import_assets(self):
        #Fixed the file path issues. Directs to correct folder and uses the import_folder function to get all images in the folder.
        #Adjusted to use os.path.join for cross platform compatibility
        for animation in self.animations.keys():
            full_path = join('Assets','Sprout Lands Sprites','Sprout Lands - Sprites - Basic pack','Characters', animation)
            self.animations[animation] = import_folder(full_path)
    
    def import_tool_assets(self, filename: str, format: str = '.png'): 
        full_path = join('Assets','Sprout Lands Sprites','Sprout Lands - Sprites - Basic pack','Characters', f'{filename}{format}')
        self.tool_animations = import_sprite_sheet(full_path,cols= 2,rows=12, names= self.animation_names, alpha=True)  
        print(self.tool_animations)
    
    def animate(self, dt):
        if self.idle == False:
            self.frame_index += 4*dt
            if self.frame_index >= len(self.animations[self.status]):
                self.frame_index = 0
        else:
            self.frame_index += 2*dt
            if self.frame_index >= 2:
                self.frame_index = 0
            
        self.image = self.animations[self.status][int(self.frame_index)]
                
    def input(self):
        keys = pygame.key.get_pressed()
        
        #direction to determine which way the player is moving
        if not self.tool_status:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
                self.idle = False
            else:
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.direction.y = 1
                    self.status = 'down'
                    self.idle = False
                else:
                    self.direction.y = 0
                    
        
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'
                self.idle = False
            else:
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.direction.x = 1
                    self.status = 'right'
                    self.idle = False
                else:
                    self.direction.x = 0
            if self.direction.magnitude() == 0:
                self.idle = True
        
        #tool use
        if keys[pygame.K_e]:
            self.timers['tool use'].activate()
            self.direction = pygame.math.Vector2() #stops movement when using tool
            print("Tool timer activated")
            
    
    def get_status(self):
        if self.timers['tool use'].active:
            self.tool_status = True
        else:
            self.tool_status = False
            #print("Tool being used")
        #tool use
        #if something:
        #    self.status = self.status.split('_')[0] + '_axe'
    
    def timers_update(self):
        for timer in self.timers.values():
            timer.update()
    
    def use_tool(self):
        print("Tool used")
        print(f'{self.status}_{self.tool}')    
    
    def move(self, dt):
        
        #normalizing movement speed
        if self.direction.magnitude() >0:
            self.direction = self.direction.normalize() #can't normalize 0....need an if statment to check if we are moving
        
        # Howinzontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        
        # Vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
        #this works but for collisions it needs to be separated into the x and y movement
        #self.pos += self.direction * self.speed * dt
        #self.rect.center = self.pos
            
            
#this functional method works but it's not a efficient or framerate independent...creating a separate location attribute var that we manipulate intead
# the diagonal speed using this method due to pythagorean theorm. scaled movement in the other method via normalization
#    def input(self):
#        keys = pygame.key.get_pressed()
#        if keys[pygame.K_UP] or keys[pygame.K_w]:
#            self.rect.y -= 1
#        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
#            self.rect.y += 1
#        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
#            self.rect.x -= 1
#        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
#            self.rect.x += 1

#dt is delta time and important for any updating steps so they are all updated on the same timescale       
    def update(self, dt):
        self.input()
        self.get_status()
        self.timers_update()
        self.move(dt)
        self.animate(dt)
        
        