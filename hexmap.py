import pygame
import random

class HexagonMap:
    def __init__(self, rows, cols, radius):
        self.rows = rows
        self.cols = cols
        self.radius = radius
        self.height = self.radius * 2
        self.width = self.radius * 2 * 0.866
        self.horz_spacing = self.width * 0.75
        self.vert_spacing = self.height * 0.5
        self.map = self.create_map()

    def create_map(self):
        map = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                x = c * self.horz_spacing + (r % 2) * self.horz_spacing / 2 + self.radius
                y = r * self.vert_spacing + self.height
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                row.append((x, y, color))
            map.append(row)
        return map

    def draw(self, screen):
        for r in range(self.rows):
            for c in range(self.cols):
                self.draw_hexagon(screen, self.map[r][c][0], self.map[r][c][1], self.map[r][c][2])

    def draw_hexagon(self, screen, x, y, color):
        points = [
            (x - self.radius, y),
            (x - self.radius / 2, y - self.height / 2),
            (x + self.radius / 2, y - self.height / 2),
            (x + self.radius, y),
            (x + self.radius / 2, y + self.height / 2),
            (x - self.radius / 2, y + self.height / 2)
        ]
        pygame.draw.polygon(screen, color, points, 0)
        pygame.draw.polygon(screen, (0, 0, 0), points, 1)