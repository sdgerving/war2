import pygame
import os
from sprite import Sprite
from button import Button
from text import TextRenderer

class Game:
    def __init__(self):
        pygame.init()
        screen_info = pygame.display.Info()
        self.window_width = screen_info.current_w
        self.window_height = screen_info.current_h
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))

        pygame.display.set_caption("fuck yea!")
        sprite_sheet_image = os.path.join("image", "testsprite.png")
        dungeonImage =os.path.join("image", "dungeon1.png")
        self.sprite = Sprite(sprite_sheet_image, 32, 32, 3, 4, 2, self.window_width, self.window_height)
        self.sprite = Sprite(sprite_sheet_image, 32, 32, 3, 4, 2, self.window_width, self.window_height)
        self.buttons = [
            Button("Button 1", (10, 10), (255, 0, 0), (255, 100, 100)),
            Button("Button 2", (150, 10), (255, 0, 0), (255, 100, 100)),
            Button("Exit", (300, 10), (255, 0, 0), (255, 100, 100))
        ]

        # Create an array of texts
        self.texts = [
            TextRenderer(font_size=45,font_color=[223,123,123], position=(100, 200), text="Hello, World!"),
            TextRenderer(font_size=24, position=(200, 300), text="Welcome to the game!")
        ]

        self.clock = pygame.time.Clock()
        self.running = True

    def handle_exit_button_click(self):
        pygame.quit()

    def run(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button in self.buttons:
                            if button.rect.collidepoint(event.pos):
                                if button.text == "Exit":
                                    self.handle_exit_button_click()
            keys = pygame.key.get_pressed()
            self.sprite.update_position(keys)
            self.screen.fill((0, 0, 0))
            self.sprite.draw(self.screen)

            # Render and display the texts on the screen
            for text in self.texts:
                text.render_text(self.screen)

            for button in self.buttons:
                button.draw(self.screen)
            pygame.display.flip()
        pygame.quit()
