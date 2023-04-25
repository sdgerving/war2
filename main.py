import sys
import pygame.font
import pygame
import os
import pygame.time
# Initialize Pygame
pygame.init()
font32 = pygame.font.Font(None, 32)
font24 = pygame.font.Font(None, 24)
screen_info = pygame.display.Info()

# Set the size of the game window to be the same as the screen
window_width = screen_info.current_w
window_height = screen_info.current_h
screen = pygame.display.set_mode((window_width, window_height))
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

button_font = pygame.font.SysFont("Arial", 20)

# Create the button surface
button_text = "Exit Game"
button_surface = button_font.render(button_text, True, (26, 15, 56))
button_width = button_surface.get_width()
button_height = button_surface.get_height()
button_rect = pygame.Rect(window_width - button_width - 10, window_height - button_height - 10, button_width, button_height)

def draw_button(text, pos):
    # Render the text
    text_surface = font32.render(text, True, (153, 16, 6))

    # Create a rectangle for the button
    button_rect = pygame.Rect(*pos, 80, 40)

    # Draw the button rectangle
    pygame.draw.rect(screen, (0, 0, 0), button_rect)

    # Draw the text in the center of the button
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

def handle_exit_button_click():
    pygame.quit()
    sys.exit()
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
sprite_x = window_width  // 2
sprite_y = window_height // 2
sprite_speed = 5

# Define the animation frames for moving the sprite
move_frames=[0,0,0,0]
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
exit_button_rect = pygame.Rect(190, 10, 80, 40)
while running:
    clock.tick(60)
    # Handle events
    mouse_pos_text = font24.render(f"Mouse position: {pygame.mouse.get_pos()}", True, (255,255,255))
    fps_text = font24.render(f"FPS: {int(clock.get_fps())}", True, (255,255,255))

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
    elif keys[pygame.K_ESCAPE]:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            # Check if the exit button was clicked
            if exit_button_rect.collidepoint(event.pos):
                handle_exit_button_click()
    # Draw the background
    screen.fill((0, 0, 0))

    # Draw the sprite
    frame = move_frames[frame_index]
    sprite = sprites[frame]
    draw_sprite(screen, sprite, sprite_x, sprite_y)

    # Update the screen
    screen.blit(mouse_pos_text, (450, 10))
    screen.blit(fps_text, (400, 30))
    draw_button("Button 1", (10, 10))
    draw_button("Button 2", (100, 10))
    draw_button("Exit", (190, 10))
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()

