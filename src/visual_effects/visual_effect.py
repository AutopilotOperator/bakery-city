from pygame.locals import *
import pygame
import abc
from utils.font import GameFont


class VisualEffect:
    def __init__(self) -> None:
        self.particle_list = []
        self.is_active = False
        # self.font = pygame.font.Font(cp.FONT_PATH, 35)
        self.font = GameFont(35)

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass
