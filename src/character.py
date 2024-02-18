import pygame
import random

FRAME_COUNT = 30

ORIANTATIONS = {
    # 'down': 0,
    # 'up': 1,
    # 'left': 2,
    'right': 3,
}

class Character (pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect((x, y), (50, 50))
        # self.rect.x = x
        # self.rect.y = y
        # self.rect.width = 50
        # self.rect.height = 50
        self.speed = 5
        self.max_frame_id = 1
        self.frame_id = random.randint(0, self.max_frame_id)
        self.oriantion = "right"
        self.frame_count = 20
        self.load_character_frames()

    def move(self, direction):
        if direction == "right":
            self.rect.x += self.speed
        if direction == "left":
            self.rect.x -= self.speed
        if direction == "up":
            self.rect.y -= self.speed
        if direction == "down":
            self.rect.y += self.speed            

    def load_character_frames(self):
        self.frames = {};
        for oriantion in ORIANTATIONS:
            self.frames[oriantion] = []
            for frame_id in range(self.max_frame_id + 1):
                image = pygame.image.load(f"./assets/images/character/main_{oriantion}_{frame_id}.png")
                image = pygame.transform.scale(image, (50, 50))
                self.rect = image.get_rect()
                self.frames[oriantion].append(image)


    def animate_character(self, display, scroll):
        self.scroll = scroll
        self.frame_count -= 1
        if self.frame_count <= 0:
            self.frame_id += 1
            self.frame_count = FRAME_COUNT
            if self.frame_id > self.max_frame_id:
                self.frame_id = 0
        self.image = self.frames[self.oriantion][self.frame_id]

        display.blit(self.image, (self.rect.x - self.scroll, self.rect.y))

