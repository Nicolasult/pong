from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.displayer.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.running = True
    
    def run(self):
        while self.running == True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update

            # draw
            pygame.display.update()
        pygame.quit()
