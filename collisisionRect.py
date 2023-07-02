import pygame

class CollisionRect:
    collision_rects = []

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.visible = True # Flag to control visibility of the collision rectangle

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def check_collision(self, other_rect):
        return self.rect.colliderect(other_rect)