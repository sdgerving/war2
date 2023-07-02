import pygame
import bullet
class enemysprite:
    def __init__(self, game_width, game_height):
        self.x = game_width // 2
        self.y = game_height // 2
        self.velocity = 5
        self.bullet = None

    def move(self):
        # Add your code for autonomous movement of the enemy sprite here
        pass

    def fire(self):
        if not self.bullet:
            self.bullet = bullet.Bullet(self.x, self.y, 10, 10, (255, 0, 0), self.velocity + 2)
            return self.bullet
        else:
            return None

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 10)
