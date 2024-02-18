import pygame
import consts as cp
from character import Character
from map.tile import Tile

WINDOW_SIZE = cp.WINDOW_SIZE

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.display = pygame.Surface((1024, 576))
        self.clock = pygame.time.Clock()
        self.running = True 
        self.character = Character(0,0)
        self.tile_map: list[Tile] = self.generate_tiles()

        
    def generate_tiles(self):
        tile_map = []
        for y in range(0, 5):
            for x in range(0, 5):
                tile = Tile(x, y, 70, 70)
                tile_map.append(tile)
        return tile_map

    def handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_ESCAPE]: #For dev purposes
            self.running = False

        if keys_pressed[pygame.K_UP]:
            self.character.move('up')
        if keys_pressed[pygame.K_DOWN]:
            self.character.move('down') 
        if keys_pressed[pygame.K_LEFT]:
            self.character.move('left')
        if keys_pressed[pygame.K_RIGHT]:
            self.character.move('right')



    def draw_elements(self):
        for tile in self.tile_map:
            # self.display.blit(tile.image, tile.location)
            pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(tile.x , tile.y, tile.height, tile.width), 1)
            self.display.blit(tile.image, (tile.x * 30 - tile.y * 30 + 300, tile.x * 20 + tile.y * 20 + 100))

        self.character.animate_character(self.screen, 0)
        # self.display.blit(self.character.image, self.character.rect)
        # pygame.display.flip()
        # self.clock.tick(60)
    

    def run(self):
        while self.running:
            
            self.display.fill((0, 0, 0))
            self.handle_events()
            # draw the character
            self.draw_elements()
            self.display.blit(self.character.image, self.character.rect)
            self.screen.blit(pygame.transform.scale(self.display, WINDOW_SIZE), (0, 0))
            pygame.display.flip()
            self.clock.tick(60)
            





if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Test")
    main = Main()
    main.run()
    pygame.quit()
    quit()