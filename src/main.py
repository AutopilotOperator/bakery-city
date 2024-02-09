import pygame
import consts as cp

WINDOW_SIZE = cp.WINDOW_SIZE

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True 


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Test")
    main = Main()
    main.run()
    pygame.quit()
    quit()