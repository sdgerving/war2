import pygame


class TextRenderer:
    all_texts = {}  # Dictionary to store texts with their IDs
    screen = None  # Class variable to store the screen object

    @classmethod
    def set_screen(cls, screen):
        cls.screen = screen
    def __init__(self, id_name, font_size=24, font_color=(255, 255, 255), font_name=None, font_type=None,
                 position=(0, 0), text=""):
        self.id_name = id_name
        self.font_size = font_size
        self.font_color = font_color
        self.font_name = font_name
        self.font_type = font_type
        self.position = position
        self.text = text
        self.font = pygame.font.SysFont(font_type, font_size)

        # Add the text to the dictionary
        TextRenderer.all_texts[id_name] = self

    def render_text(self):
        text_surface = self.font.render(self.text, True, self.font_color)
        self.screen.blit(text_surface, self.position)

    @classmethod
    def render_all_texts(cls):
        for text in cls.all_texts.values():
            text.render_text()
