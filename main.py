import pygame
import os

# Initialize Pygame
pygame.init()

# Set the size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Sprite Sheet Animation")

# Load the sprite sheet
sprite_sheet_image = pygame.image.load(os.path.join("image/testsprite.png")).convert_alpha()

# Define the dimensions of each sprite
SPRITE_WIDTH = 32
SPRITE_HEIGHT = 32

# Define the number of sprites in each row and column
SPRITES_PER_ROW = 3
SPRITES_PER_COL = 4

# Define a function to slice the sprite sheet into individual sprites
def slice_spritesheet(sprite_sheet_image, sprite_width, sprite_height, sprites_per_row, sprites_per_col):
    sprites = []
    for row in range(sprites_per_col):
        for col in range(sprites_per_row):
            x = col * sprite_width
            y = row * sprite_height
            sprite_image = sprite_sheet_image.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
            sprites.append(sprite_image)
    return sprites

# Slice the sprite sheet into individual sprites
sprites = slice_spritesheet(sprite_sheet_image, SPRITE_WIDTH, SPRITE_HEIGHT, SPRITES_PER_ROW, SPRITES_PER_COL)

# Define a function to color key the sprites
def colorkey_sprites(sprites):
    colorkey = sprites[0].get_at((0, 0))
    for sprite in sprites:
        sprite.set_colorkey(colorkey, pygame.RLEACCEL)

# Color key the sprites
colorkey_sprites(sprites)

# Define the position and speed of the sprite
sprite_x = SCREEN_WIDTH // 2
sprite_y = SCREEN_HEIGHT // 2
sprite_speed = 5

# Define the animation frames for moving the sprite
move_frames=[]
move_frames_down = [0, 1, 2, 1]
move_frames_up = [9, 10, 11, 9]
move_frames_left = [3, 4, 5, 3]
move_frames_right = [6, 7, 8 ,6]
# Define a function to draw the sprite on the screen
def draw_sprite(screen, sprite, x, y):
    screen.blit(sprite, (x - sprite.get_width() // 2, y - sprite.get_height() // 2))

# Define the clock to control the frame rate of the animation
clock = pygame.time.Clock()

# Define the main game loop
running = True
frame_index = 0
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the sprite based on input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite_x -= sprite_speed
        frame_index = (frame_index + 1) % len(move_frames_left)
        move_frames = move_frames_left
    elif keys[pygame.K_RIGHT]:
        sprite_x += sprite_speed
        frame_index = (frame_index + 1) % len(move_frames_right)
        move_frames = move_frames_right
    elif keys[pygame.K_UP]:
        sprite_y -= sprite_speed
        frame_index = (frame_index + 1) % len(move_frames_up)
        move_frames = move_frames_up
    elif keys[pygame.K_DOWN]:
        sprite_y += sprite_speed
        frame_index = (frame_index + 1) % len(move_frames_down)
        move_frames = move_frames_down

    # Draw the background
    screen.fill((255, 255, 255))

    # Draw the sprite
    frame = move_frames[frame_index]
    sprite = sprites[frame]
    draw_sprite(screen, sprite, sprite_x, sprite_y)

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()

