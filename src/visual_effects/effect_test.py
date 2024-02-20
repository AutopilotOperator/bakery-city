from visual_effects.visual_effect import VisualEffect
import pygame
from typing import TypedDict
import random
import consts

class Particle(TypedDict):
    x: int
    y: int
    y_speed: int
    x_speed: int
    size: int
    ticks_left: int


class EffectTest(VisualEffect):
    def __init__(self):
        super().__init__()
        self.color = consts.LIGHT_BLUE


    def start(self, base_coordinates: tuple[int, int]):
        if self.is_active is False:
            self.is_active = True
            self.particle_list: list[Particle] = []
            for i in range(10):
                # random y and x speeds
                particle: Particle = {'x': base_coordinates[0], 'y': base_coordinates[1], 'y_speed': random.randint(-5, -1), 'x_speed': random.randint(-2, 2), 'size': random.randint(1,4), 'ticks_left': 20}
                self.particle_list.append(particle)            
        

    def update(self):
        if self.is_active:
            for particle in self.particle_list:
                particle['x'] += particle['x_speed']
                particle['y'] += particle['y_speed']
                particle['y_speed'] += 1
                particle['ticks_left'] -= 1
                # particle['size'] += 0.1
                if particle['ticks_left'] <= 0:
                    self.particle_list.remove(particle)

            if len(self.particle_list) == 0:
                self.is_active = False
                self.particle_list = []


    def draw(self, surface: pygame.surface.Surface ):
        if self.is_active:
            self.update()
            for particle in self.particle_list:
                pygame.draw.circle(surface, self.color, (particle['x'], particle['y']), particle['size'])