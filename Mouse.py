import pygame

from text import TextRenderer


class Mouse:
    def __init__(self, selected_loc, current_loc, click_value, selectedx, selectedy):
        self.mouseX =0
        self.mouseY = 0
        self.selectedLoc = selected_loc
        self.currentLoc = current_loc
        self.click_Value = click_value
        self.selectedx = selectedx
        self.selectedy = selectedy
        self.mouse_x_text = TextRenderer("mouseX", font_size=52, position=(200, 350), text="X: 0")
        self.mouse_y_text = TextRenderer("mouseY", font_size=52, position=(200, 400), text="Y: 0")

    def update(self):
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        self.mouse_x_text.text = "X: " + str(self.mouseX)
        self.mouse_y_text.text = "Y: " + str(self.mouseY)

