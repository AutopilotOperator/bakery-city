import pygame
import consts as cp
from character import Character
from map.tile import Tile
from utils.font import GameFont
from visual_effects.effect_test import EffectTest

WINDOW_SIZE = cp.WINDOW_SIZE

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.display = pygame.Surface((1024, 576))
        self.clock = pygame.time.Clock()
        self.running = True 
        self.character = Character(400, 400)
        self.tile_map: list[Tile] = self.generate_tiles()
        self.game_text = GameFont()
        # self.init_character_loaction()
        self.test_effect  = EffectTest()

    def init_character_loaction(self):
        # find the first element which is floor type
        index = [element.type == 'floor' for element in self.tile_map].index(True)
        first_floor_tile = self.tile_map[index]
        self.character.rect.x = first_floor_tile.x * 30 - first_floor_tile.y * 30 + 500
        self.character.rect.y = first_floor_tile.x * 20 + first_floor_tile.y * 20 - 100
        # return self.character.rect.x, self.character.rect.y

    def generate_tiles(self):
        # read config txt file
        map_config = open("./map/map_config.txt", "r")
        map_config_lines = map_config.readlines()
        tile_map = []
        for (i, line) in enumerate(map_config_lines):
            map_config_columns = line.strip()
            for (j, column) in enumerate(map_config_columns):
                if column == "1":
                    tile = Tile(j, i)
                    tile_map.append(tile)
                if column == "2":
                    tile = Tile(j, i, 'wall')
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

        if keys_pressed[pygame.K_p]:
            self.test_effect.start((self.character.rect.x, self.character.rect.y))



    def draw_vfx(self):

        pass


    def draw_elements(self):
        for tile in self.tile_map:
            # self.display.blit(tile.image, tile.location)
            pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(tile.x * 20 , tile.y * 20, 20, 20), 1)
            tile.draw_tile(self.display)

        # get mouse pos
        mouse_pos = pygame.mouse.get_pos()
        y = (3 * mouse_pos[1] - 2 * mouse_pos[0] + 1300) / 120
        x = (3 * mouse_pos[1] + 2 * mouse_pos[0] - 700) / 120

        

        self.character.animate_character(self.screen, 0)
        # self.display.blit(self.game_text.get_text_paragraph([f'X: {round(x, 2)}   Y: {round(y, 2)}']), (self.character.rect)) 
        # self.display.blit(self.game_text.get_text_paragraph([f'X: {self.character.rect.x}   Y: {self.character.rect.y}']), ((300, 300))) 
        # self.display.blit(self.game_text.get_text_paragraph([f'X: {self.character.tile_coordinates[0]}   Y: {self.character.tile_coordinates[1]}']), ((300, 400))) 
        self.test_effect.draw(self.display)
        

    

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