import pygame

class Timer:
    def __init__(self):
        self.start_ticks = pygame.time.get_ticks()  # Get the initial ticks when the timer starts

    def get_time(self):
        seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000  # Calculate elapsed time in seconds
        return seconds

    def reset(self):
        self.start_ticks = pygame.time.get_ticks()  # Reset the timer to the current ticks