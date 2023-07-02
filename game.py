import pygame
import random

import Gradient
from collisisionRect import CollisionRect
from Gradient import GradientBorder
from gimages import ImageDisplay
from herosprite import Sprite
from button import Button

from gameboard import GameBoard
from enemysprite import enemysprite
from Mouse import Mouse
from text import TextRenderer


class Game:
    def __init__(self):
        pygame.init()
        screen_info = pygame.display.Info()
        self.window_width = screen_info.current_w
        self.window_height = screen_info.current_h
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.gameboard = GameBoard(1000,500,1000, 500, "image/dungeon1.png",(self.window_width//2), (self.window_height//2),1)
        pygame.display.set_caption("fuck yea!")

        self.mouse1 = Mouse( 0, 0, 0, 0, 0)
        self.sprite = Sprite("image/testsprite.png", 32, 32, 32, 32, 3, 4, 3, self.gameboard.position[0],self.gameboard.position[1], self.gameboard.width55, self.gameboard.height55)
        self.statsboard = ImageDisplay(625, 1100, "image/Parchment2.png", 0,0)
        self.firstGradient = GradientBorder(self.screen,self.gameboard.position[0]-25,self.gameboard.position[1]-25, self.gameboard.width55+51, self.gameboard.height55+51, 1, 25)


        self.enemy = enemysprite(self.window_width, self.window_height)
        self.bullet = None

        self.buttons = [
            Button("Button 1", (10, 10), (255, 0, 0), (255, 100, 100)),
            Button("map", (150, 10), (255, 0, 0), (255, 100, 100)),
            Button("Exit", (300, 10), (255, 0, 0), (255, 100, 100))
        ]
        self.colRect = [
            CollisionRect(self.gameboard.position[0], self.gameboard.position[1]-25 , self.gameboard.width55,25),
            CollisionRect(self.gameboard.position[0], self.gameboard.position[1] + self.gameboard.height55,self.gameboard.width55, 25),
            CollisionRect(self.gameboard.position[0] - 25, self.gameboard.position[1] , 25, self.gameboard.height55+25),
            CollisionRect(self.gameboard.position[0] +self.gameboard.width55, self.gameboard.position[1], 25,self.gameboard.height55 + 25),

            CollisionRect(1200, 600, 100, 100),

        ]


            # Add more collision rectangles here...


        self.clock = pygame.time.Clock()
        self.running = True
        TextRenderer.set_screen(self.screen)

        TextRenderer("test", font_size=45, font_color=[223, 123, 123], position=(10, 10), text="Hello, World!"),
        TextRenderer("welcome",font_size=24, position=(200, 300), text="Welcome to the game!"),

        TextRenderer("maxwidth",font_size=32, position=(200, 500),text=("Min Width: " + str(self.gameboard.min_width)) + "  Max Width " + str(self.gameboard.max_width)),
        TextRenderer("maxheight",font_size=32, position=(200, 525),text=("Min Height: " + str(self.gameboard.min_height)) + "  Max Height " + str(self.gameboard.max_height)),
        TextRenderer("gameboard",font_size=32, position=(200, 550),text=("gameboard x:: " + str(self.gameboard.x)) + "  gameboard y " + str(self.gameboard.y)),
        TextRenderer("spriteloc",font_size=32, position=(200, 575),text=("sprite x:: " + str(self.sprite.x)) + "  sprite y " + str(self.sprite.y)),
        TextRenderer("gbheightwidht",font_size=32, position=(200, 600),text=("width 55: " + str(self.gameboard.width55)) + "  height 55 " + str(self.gameboard.height55)),
        TextRenderer("spritepos",font_size=32, position=(200, 625),text=("sprite x:: " + str(self.sprite.x)) + "  sprite y " + str(self.sprite.y)),
        TextRenderer("resize",font_size=32, position=(200, 650),text=("resize width: " + str(self.sprite.resizewidth)) + "  resize height " + str(self.sprite.resizeheight))

    def handle_exit_button_click(self):
        pygame.quit()

    import random

    def createNewMap(self):
        self.gameboard = GameBoard(1000, 500, 1000, 500, "image/dungeon1.png", (self.window_width // 2),
                                   (self.window_height // 2), 1)
        self.sprite = Sprite("image/testsprite.png", 32, 32, 32, 32, 3, 4, 3, self.gameboard.position[0],
                             self.gameboard.position[1], self.gameboard.width55, self.gameboard.height55)
        self.firstGradient = GradientBorder(self.screen, self.gameboard.position[0] - 25,
                                            self.gameboard.position[1] - 25, self.gameboard.width55 + 51,
                                            self.gameboard.height55 + 51, 1, 25)

        self.colRect = [
            CollisionRect(self.gameboard.position[0], self.gameboard.position[1] - 25, self.gameboard.width55, 25),
            CollisionRect(self.gameboard.position[0], self.gameboard.position[1] + self.gameboard.height55,
                          self.gameboard.width55, 25),
            CollisionRect(self.gameboard.position[0] - 25, self.gameboard.position[1], 25,
                          self.gameboard.height55 + 25),
            CollisionRect(self.gameboard.position[0] + self.gameboard.width55, self.gameboard.position[1], 25,
                          self.gameboard.height55 + 25),
            *[CollisionRect(random.randint(self.gameboard.position[0] + 25,
                                           self.gameboard.position[0] + self.gameboard.width55 - 25),
                            random.randint(self.gameboard.position[1] + 25,
                                           self.gameboard.position[1] + self.gameboard.height55 - 25),
                            random.randint(5, 50),
                            random.randint(5, 50)) for _ in range(5)]
        ]

    def update(self):
        self.enemy.move()
        self.mouse1.update()
        self.mouse1.mouse_x_text.render_text()
        self.mouse1.mouse_y_text.render_text()

        if not self.bullet:
            self.bullet = self.enemy.fire()

        if self.bullet:
            self.bullet.move()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.statsboard.draw(self.screen)
        self.gameboard.draw(self.screen)
        self.sprite.draw(self.screen)
        self.enemy.draw(self.screen)
        self.firstGradient.draw()
        self.mouse1.update()

        if self.bullet:
            self.bullet.draw(self.screen)

        # Render and display the texts on the screen
        self.mouse1.mouse_x_text.render_text()
        self.mouse1.mouse_y_text.render_text()
        TextRenderer.render_all_texts()
        for coll in self.colRect:
            if coll.visible:
                coll.draw(self.screen)
        for button in self.buttons:
            button.draw(self.screen)

        pygame.display.flip()

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
                                if button.text == "map":
                                    self.createNewMap()

            keys = pygame.key.get_pressed()


                # Check for collisions among the rectangles
            for i in range(len(self.colRect)):
                for j in range(i + 1, len(self.colRect)):
                    if self.colRect[i].check_collision(self.colRect[j].rect):
                        TextRenderer("collision", font_size=45, font_color=[223, 123, 123], position=(1000, 130),
                                     text="Collision detected between rect " + str(i) + " and rect " + str(j))
                        print("Collision detected between rect", i, "and rect", j)

            self.sprite.update_position(keys, self.colRect)

            self.update()
            self.draw()

        pygame.quit()

