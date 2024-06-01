import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        
        #has to be first b/c when you make image (next step) you need the animations dictionary to pull from.
        self.import_assets()
        #create status states to determine which animation to use
        self.status = 'down'
        #create a starting index to use for animation loop
        self.frame_index = 0
        
        # general setup
        self.image = self.animations[self.status][self.frame_index]
        #self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)
        # Movement attributes instead of functional to be framerate indpendent and use delta time
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center) #this is needed b/c we are using delta time, which returns floats commonly...rects store as int() and not compatible with the dt approach
        self.speed = 150


    #only doing a few movement animations in the dictionary for now to make sure I cut the sprite file correctly
    def import_assets(self):
        self.animations = {'up': [], 'down':[], 'left': [], 'right': []} #will make larger with more sprites
        
        #my file path is weird as there is an extra sub folder with the same name that VScode omits in the file folder viewer.
        for animation in self.animations.keys():
            full_path = "C:\\Users\\Chris Carnivale\\OneDrive\\Desktop\\Python_fun_project\\Python_game\\Assets\\Sprout Lands - Sprites - Basic pack\\Sprout Lands - Sprites - Basic pack\\Characters\\" + animation 
            self.animations[animation] = import_folder(full_path)   
    
    def animate(self, dt):
        self.frame_index += 4*dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
            
        self.image = self.animations[self.status][int(self.frame_index)]
                
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            self.status = 'up'
        else:
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0
    
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
        else:
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x = 0
    
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
        self.move(dt)
        self.animate(dt)