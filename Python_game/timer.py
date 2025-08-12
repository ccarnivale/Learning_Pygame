import pygame

class Timer:
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func
        self.active = False
        self.start_ticks = 0
        
        
    def activate(self):
        self.active = True
        self.start_ticks = pygame.time.get_ticks()
        seconds = (pygame.time.get_ticks() - self.start_ticks) # Calculate elapsed time in seconds
        return seconds

    def deactivate(self):
        self.active = False  # Reset the timer to turn off