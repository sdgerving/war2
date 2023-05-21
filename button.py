import pygame

class Button:
    def __init__(self, text, pos, border_color=(0, 0, 0), hover_color=(100, 100, 100)):
        self.text = text
        self.pos = pos
        self.border_color = border_color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont("Arial", 30)
        self.surface = self.font.render(self.text, True, (255, 255, 255))
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        self.rect = pygame.Rect(*self.pos, self.width+25, self.height)

    def draw(self, screen):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            button_color = self.hover_color
        else:
            button_color = (56, 13, 12)
        pygame.draw.rect(screen, button_color, self.rect, 0)
        pygame.draw.rect(screen, self.border_color, self.rect, 3)
        text_rect = self.surface.get_rect(center=self.rect.center)
        screen.blit(self.surface, text_rect)
