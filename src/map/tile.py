import pygame
import consts
IMAGE_PATH = '.\\assets\\images\\tiles'

class Tile():
    def __init__(self, x, y, type='floor'):
        self.x = x
        self.y = y
        self.type = type
        # self.image = pygame.transform.scale(pygame.image.load(f'{IMAGE_PATH}\\test.png'), (width, height)).convert_alpha()
        self.set_dimensions()
        self.set_image()

    def set_dimensions(self):
        if self.type == 'floor':
            self.width = 70
            self.height = 70
        elif self.type == 'wall':
            self.width = 70
            self.height = 130
        else:
            self.width = 10
            self.height = 10
        
        return
        

    def set_image(self):
        if (self.type == 'floor'):
            self.image = pygame.transform.scale(pygame.image.load(f'{IMAGE_PATH}\\test.png'), (self.width, self.height)).convert_alpha()
        if (self.type == 'wall'):
            self.image = pygame.transform.scale(pygame.image.load(f'{IMAGE_PATH}\\wall_test.png'), (self.width, self.height)).convert_alpha()


    def draw_tile(self, display):
        # display.blit(self.image, (self.x, self.y))
        if self.type == 'floor':
            display.blit(self.image, (self.x * 30 - self.y * 30 + 500, self.x * 20 + self.y * 20 - 100))
            return
        elif self.type == 'wall':
            display.blit(self.image, (self.x * 30 - self.y * 30 + 500, self.x * 20 + self.y * 20 - 160))
            return
        return
        

    @property
    def location(self):
        return (self.x, self.y)
    
    
