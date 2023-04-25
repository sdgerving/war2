import pygame

class SpriteSheet:
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    def load_sprites(self, row_start, row_end, col_start, col_end):
        sprites = []

        for row in range(row_start, row_end):
            for col in range(col_start, col_end):
                rect = pygame.Rect(col * 64, row * 64, 64, 64)
                image = pygame.Surface(rect.size, pygame.SRCALPHA)
                image.blit(self.sprite_sheet, (0, 0), rect)
                sprites.append(image)

        return sprites