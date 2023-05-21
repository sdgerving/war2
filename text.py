import pygame

class TextRenderer:
    def __init__(self, font_size=24, font_color=(255, 255, 255), font_name=None, font_type=None, position=(0, 0), text=""):
        self.font_size = font_size
        self.font_color = font_color
        self.font_name = font_name
        self.font_type = font_type
        self.position = position
        self.text = text
        self.font = pygame.font.SysFont(font_type, font_size)

    def render_text(self, screen):
        text_surface = self.font.render(self.text, True, self.font_color)
        screen.blit(text_surface, self.position)