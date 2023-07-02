import pygame


class ImageDisplay:
    def __init__(self, max_width,  max_height,  background_image, x, y):
        self.x = x
        self.y = y
        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h

        self.width = max_width
        self.height =max_height

        # Resize game board based on monitor size
        self.width = int(self.width * screen_width / 1920)
        self.height = int(self.height * screen_height / 1080)
        self.surface = pygame.Surface((self.width, self.height))
        self.background_image = background_image
        self.position = (self.x, self.y)

        if self.background_image:
            self.background = pygame.image.load(self.background_image).convert()
            self.background = pygame.transform.scale(self.background, (self.width, self.height))
            self.surface.blit(self.background, (0, 0))
        else:
            self.surface.fill((0, 0, 0))

    def draw(self, screen):
        screen.blit(self.surface, self.position)

