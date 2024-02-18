import pygame
import consts
IMAGE_PATH = '.\\assets\\images\\tiles'

class Tile():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load(f'{IMAGE_PATH}\\test.png'), (width, height)).convert_alpha()

    @property
    def location(self):
        return (self.x, self.y)
    
    
