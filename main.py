import pygame
from sys import exit

pygame.init()


class App():
    def __init__(self) -> None:
        #important variables
        self.clock = pygame.time.Clock()

        self.fps = 60
        self.width = 1200
        self.height = 800
        self.wn = pygame.display.set_mode((self.width, self.height))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.clock.tick(self.fps)
            pygame.display.update()


if __name__ == "__main__":
    app = App()
    app.run()


