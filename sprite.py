import pygame

class Sprite:
    def __init__(self, sprite_sheet_image, sprite_width, sprite_height, sprites_per_row, sprites_per_col, sprite_speed, window_width, window_height):
        self.sprite_sheet_image = pygame.image.load(sprite_sheet_image).convert_alpha()
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.sprites_per_row = sprites_per_row
        self.sprites_per_col = sprites_per_col
        self.sprite_speed = sprite_speed
        self.sprites = self.slice_spritesheet()
        self.colorkey_sprites()
        self.sprite_x = window_width // 2
        self.sprite_y = window_height // 2
        self.move_frames = [0, 0, 0, 0]
        self.move_frames_down = [0, 1, 2, 1]
        self.move_frames_up = [9, 10, 11, 9]
        self.move_frames_left = [3, 4, 5, 3]
        self.move_frames_right = [6, 7, 8, 6]
        self.frame_index = 0

    def slice_spritesheet(self):
        sprites = []
        for row in range(self.sprites_per_col):
            for col in range(self.sprites_per_row):
                x = col * self.sprite_width
                y = row * self.sprite_height
                sprite_image = self.sprite_sheet_image.subsurface(pygame.Rect(x, y, self.sprite_width, self.sprite_height))
                sprites.append(sprite_image)
        return sprites

    def colorkey_sprites(self):
        colorkey = self.sprites[0].get_at((0, 0))
        for sprite in self.sprites:
            sprite.set_colorkey(colorkey, pygame.RLEACCEL)

    def update_position(self, keys):
        if keys[pygame.K_LEFT]:
            self.sprite_x -= self.sprite_speed
            self.frame_index = (self.frame_index + 1) % len(self.move_frames_left)
            self.move_frames = self.move_frames_left
        elif keys[pygame.K_RIGHT]:
            self.sprite_x += self.sprite_speed
            self.frame_index = (self.frame_index + 1) % len(self.move_frames_right)
            self.move_frames = self.move_frames_right
        elif keys[pygame.K_UP]:
            self.sprite_y -= self.sprite_speed
            self.frame_index = (self.frame_index + 1) % len(self.move_frames_up)
            self.move_frames = self.move_frames_up
        elif keys[pygame.K_DOWN]:
            self.sprite_y += self.sprite_speed
            self.frame_index = (self.frame_index + 1) % len(self.move_frames_down)
            self.move_frames = self.move_frames_down

    def draw(self, screen):
        frame = self.move_frames[self.frame_index]
        sprite = self.sprites[frame]
        screen.blit(sprite, (self.sprite_x - sprite.get_width() // 2, self.sprite_y - sprite.get_height() // 2))
