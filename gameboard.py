import pygame
import random

class GameBoard:

    def __init__(self, max_width, min_width, max_height, min_height, background_image, x, y,borderthickness):
        self.x = x
        self.y = y
        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h

        self.max_width = max_width
        self.min_width = min_width
        self.max_height = max_height
        self.min_height = min_height

        self.width55 = random.randint(self.min_width, self.max_width)
        self.height55 = random.randint(self.min_height, self.max_height)
        self.borderthickness=borderthickness

        self.surface = pygame.Surface((self.width55, self.height55))
        self.background_image = background_image
        self.position = ((screen_width - self.width55) // 2, (screen_height - self.height55) // 2)


        # Create gradient colors from gold to black
        self.colors = self.create_gradient_colors(10)  # Specify the desired number of color values

        if self.background_image:
            self.background = pygame.image.load(self.background_image).convert()
            self.background = pygame.transform.scale(self.background, (self.width55, self.height55))
            self.surface.blit(self.background, (0, 0))
        else:
            self.surface.fill((0, 0, 0))

        # Draw gradient border
        #self.draw_gradient_border(-20)

    def draw(self, screen):
        screen.blit(self.surface, self.position)

    def create_gradient_colors(self, num_colors):
        color1 = (191, 6, 13)
        color2 = (117, 11, 18)
        color3 = (83, 14, 18)
        color4 = (49, 13, 14)
        color5 = (17, 2, 2)
        colors = []

        for i in range(num_colors):
            r = int(color1[0] + (color2[0] - color1[0]) * i / (num_colors - 1))
            g = int(color1[1] + (color2[1] - color1[1]) * i / (num_colors - 1))
            b = int(color1[2] + (color2[2] - color1[2]) * i / (num_colors - 1))
            colors.append((r, g, b))

        for i in range(num_colors):
            r = int(color2[0] + (color3[0] - color2[0]) * i / (num_colors - 1))
            g = int(color2[1] + (color3[1] - color2[1]) * i / (num_colors - 1))
            b = int(color2[2] + (color3[2] - color2[2]) * i / (num_colors - 1))
            colors.append((r, g, b))

        for i in range(num_colors):
            r = int(color3[0] + (color4[0] - color3[0]) * i / (num_colors - 1))
            g = int(color3[1] + (color4[1] - color3[1]) * i / (num_colors - 1))
            b = int(color3[2] + (color4[2] - color3[2]) * i / (num_colors - 1))
            colors.append((r, g, b))

        for i in range(num_colors):
            r = int(color4[0] + (color5[0] - color4[0]) * i / (num_colors - 1))
            g = int(color4[1] + (color5[1] - color4[1]) * i / (num_colors - 1))
            b = int(color4[2] + (color5[2] - color4[2]) * i / (num_colors - 1))
            colors.append((r, g, b))



        return colors

    def draw_gradient_border(self, border_increase):
        rect = pygame.Rect(0, 0, self.width55, self.height55)

        # Draw the gradient border from outside to inside
        for color in self.colors:
            pygame.draw.rect(self.surface, color, rect, self.borderthickness)

            rect.inflate_ip(-border_increase * self.borderthickness, -border_increase * self.borderthickness)


    def update_size(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.surface = pygame.Surface((self.width, self.height))

        if self.background_image:
            self.background = pygame.image.load(self.background_image).convert()
            self.background = pygame.transform.scale(self.background, (self.width, self.height))
            self.surface.blit(self.background, (0, 0))
        else:
            self.surface.fill((0, 0, 0))

        # Create gradient colors from gold to black


        # Draw gradient border
        self.draw_gradient_border()