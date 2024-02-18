import pygame
import consts
import os

FONT_PATH = os.path.abspath(consts.FONT_PATH)
class GameFont:
    def __init__(self, size=25):
        self.size = size
        self.font = pygame.font.Font(FONT_PATH, size)

        
    def render(self, string, antialias, color=consts.BLACK):
        return self.font.render(string, antialias, color)
        

    def get_height(self):
        return self.font.get_height()


    def get_text_paragraph(self, text_list):
        #Render all lines
        rendered_text_list = []
        for text_line in text_list:
            rendered_text_list.append(self.font.render(text_line, 1, consts.BLACK))

        #Get needed width for the surface
        max_width = rendered_text_list[0].get_width()
        for rendered_line in rendered_text_list:
            width = rendered_line.get_width()
            if  width > max_width:
                max_width = width
 
        #Blit all lines to a surface and return it
        surface = pygame.Surface((max_width + 10, self.font.get_height() + 20), pygame.SRCALPHA)
        for index, label_line in enumerate(rendered_text_list):
            surface.blit(label_line,(5,5 + index * (self.font.get_height() + 10)))

        return surface