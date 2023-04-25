import pygame
from sprite import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the sprite sheet
        sprite_sheet = SpriteSheet("image/testsprite.png")

        # Load the walking animation frames
        self.walk_right_sprites = sprite_sheet.load_sprites(0, 2, 0, 2)
        self.walk_left_sprites = sprite_sheet.load_sprites(0, 2, 2, 4)
        self.walk_up_sprites = sprite_sheet.load_sprites(0, 2, 4, 6)
        self.walk_down_sprites = sprite_sheet.load_sprites(0, 2, 6, 8)

        # Set the initial sprite
        self.image = self.walk_down_sprites[0]

        # Set the rect
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

        # Set the movement speed
        self.speed = 5

        # Set the animation variables
        self.animation_counter = 0
        self.animation_index = 0
        self.animation_frames = self.walk_down_sprites
        self.facing = "down"

    def update(self):
        # Handle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.facing = "right"
            self.animation_frames = self.walk_right_sprites
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.facing = "left"
            self.animation_frames = self.walk_left_sprites
        elif keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.facing = "up"
            self.animation_frames = self.walk_up_sprites
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.facing = "down"
            self.animation_frames = self.walk_down_sprites

        # Update the animation
        self.update_animation()

    def update_animation(self):
        # Determine which animation frames to use based on the direction the player is facing
        if self.facing == "right":
            start_index, end_index = 0, 1
        elif self.facing == "left":
            start_index, end_index = 0, 1
        elif self.facing == "up":
            start_index, end_index = 0, 1
        elif self.facing == "down":
            start_index, end_index = 0, 1

        # Increment the animation counter
        self.animation_counter += 1

        # Switch to the next animation frame if it's time
        if self.animation_counter == 10:
            self.animation_index += 1
            if self.animation_index > end_index:
                self.animation_index = start_index

        # Set the new sprite image
        self.image = self.animation_frames[self.animation_index]
