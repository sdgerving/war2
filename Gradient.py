import pygame

class GradientBorder:
    def __init__(self, screen, x, y, width, height, border_thickness, num_colors):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_thickness = border_thickness
        self.num_colors = num_colors
        self.colors = self.create_gradient_colors(self.num_colors)

    def create_gradient_colors(self,num_colors):
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
        # Return the gradient colors
        return colors

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Draw the gradient border from outside to inside
        for color in self.colors[:self.num_colors]:
            pygame.draw.rect(self.screen, color, rect, self.border_thickness)
            rect.inflate_ip(-2 * self.border_thickness, -2 * self.border_thickness)

