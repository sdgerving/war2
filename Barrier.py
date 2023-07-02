import pygame


import pygame


class Barrier:
    def __init__(self, x, y, width, height, thickness, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.thickness = thickness
        self.color = color

    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.width, self.height), self.thickness)