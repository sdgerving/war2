import pygame


def resize_image(image, new_width, new_height):
    return pygame.transform.scale(image, (new_width, new_height))


class Sprite:
    def __init__(self, sprite_sheet, width, height, resizeWidth, resizeHeight, num_rows, num_cols, num_frames, gb_posX, gb_posY, game_width, game_height):
        self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()
        self.resizewidth = resizeWidth
        self.resizeheight = resizeHeight
        self.width = width
        self.height = height
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_frames = num_frames
        self.game_width = game_width
        self.game_height = game_height
        self.frame_index = 0
        self.frame_count = 0
        self.frame_delay = 10
        self.animation_finished = False
        self.x = gb_posX
        self.y = gb_posY
        self.velocity = 5
        self.direction = "idle"
        self.gb_posX = gb_posX
        self.gb_posY = gb_posY

    def update_position(self, keys, collision_rects):
        prev_x = self.x
        prev_y = self.y

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.velocity
            self.direction = "left"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.velocity
            self.direction = "right"
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.velocity
            self.direction = "up"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.velocity
            self.direction = "down"
        else:
            self.direction = "idle"



        # Check for collisions with collision rectangles
        sprite_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        for rect in collision_rects:
            if rect.check_collision(sprite_rect):

                self.x = prev_x
                self.y = prev_y

        if prev_x != self.x or prev_y != self.y:
            self.frame_count += 1
            if self.frame_count >= self.frame_delay:
                self.frame_index += 1
                if self.frame_index >= self.num_frames:
                    self.frame_index = 0
                self.frame_count = 0

    def draw(self, screen):
        row = self.frame_index // self.num_cols
        col = self.frame_index % self.num_cols
        if self.direction == "idle":
            col = 0
        elif self.direction == "left":
            row = 1
        elif self.direction == "right":
            row = 2
        elif self.direction == "up":
            row = 3
        elif self.direction == "down":
            row = 0
        else:
            col = (self.frame_index % self.num_cols) + 1

        sprite_x = col * self.width
        sprite_y = row * self.height

        sprite_image = self.sprite_sheet.subsurface(pygame.Rect(sprite_x, sprite_y, self.width, self.height))
        resized_image = resize_image(sprite_image, self.resizewidth, self.resizeheight)

        screen.blit(resized_image, (self.x, self.y))