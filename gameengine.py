import pygame
import hexmap


class GameEngine:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = False
        self.player = None
        self.enemies = []

    def start(self):
        self.running = True

        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update game objects
            self.player.update()
            for enemy in self.enemies:
                enemy.update()

            # Draw game objects
            self.screen.fill((255, 255, 255)) # fill screen with white
            self.player.draw(self.screen)
            for enemy in self.enemies:
                enemy.draw(self.screen)

            # Update screen
            pygame.display.update()

            # Limit frame rate
            self.clock.tick(self.fps)

        pygame.quit()
