import pygame
class Bullet:
    def __init__(self, x, y, width, height, color, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity = velocity

    def move(self):
        self.y += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
