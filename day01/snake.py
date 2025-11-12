import pygame, random

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(size)
pygame.display.set_caption("~~SNEKE~~")

# Set FPS and clock
FPS = 20  # Frames per second
clock = pygame.time.Clock()

# Set game values
SNAKE_SIZE = 20  # Size of each snake segment
head_x = WINDOW_WIDTH // 2  # Snake's head starting X position
head_y = (WINDOW_HEIGHT // 2) + 100  # Snake's head starting Y position
snake_dx = 0  # Snake's movement in the X direction
snake_dy = 0  # Snake's movement in the Y direction
score = 0  # Initial score

# Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)

# Set fonts
font = pygame.font.SysFont('gabriola', 48)

# Set text
title_text = font.render("~~Snake~~", True, GREEN, DARKRED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

score_text = font.render(f"Score: {score}", True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAMEOVER", True, RED, DARKRED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Press any key to play again", True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

# Set sounds and music
pick_up_sound = pygame.mixer.Sound("pickup_sound.wav")

# Set images (snake and apple)
head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.Rect(head_coord)
apple_coord = (random.randint(0, WINDOW_WIDTH - SNAKE_SIZE), random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE), SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.Rect(apple_coord)

# The main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dy == 0:
                snake_dx = 0
                snake_dy = -SNAKE_SIZE
            elif event.key == pygame.K_DOWN and snake_dy == 0:
                snake_dx = 0
                snake_dy = SNAKE_SIZE
            elif event.key == pygame.K_LEFT and snake_dx == 0:
                snake_dx = -SNAKE_SIZE
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx == 0:
                snake_dx = SNAKE_SIZE
                snake_dy = 0

    # Move the snake
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
    head_rect = pygame.Rect(head_coord)

    # Check for collision with walls
    if head_x < 0 or head_x >= WINDOW_WIDTH or head_y < 0 or head_y >= WINDOW_HEIGHT:
        running = False  # Game over if snake hits the wall

    # Check for collision with apple
    if head_rect.colliderect(apple_rect):
        score += 1
        apple_coord = (random.randint(0, WINDOW_WIDTH - SNAKE_SIZE), random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE), SNAKE_SIZE, SNAKE_SIZE)
        apple_rect = pygame.Rect(apple_coord)
        pick_up_sound.play()  # Play the sound when apple is eaten

    # Fill screen with white background
    display_surface.fill(WHITE)

    # Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)

    # Blit snake and apple
    pygame.draw.rect(display_surface, GREEN, head_coord)
    pygame.draw.rect(display_surface, RED, apple_coord)

    # Update score display
    score_text = font.render(f"Score: {score}", True, GREEN, DARKRED)
    score_rect = score_text.get_rect()
    score_rect.topleft = (10, 10)

    # Check for game over
    if not running:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        # Wait for key press to restart
        waiting_for_restart = True
        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting_for_restart = False
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Restart the game by resetting variables
                    head_x = WINDOW_WIDTH // 2
                    head_y = (WINDOW_HEIGHT // 2) + 100
                    snake_dx = 0
                    snake_dy = 0
                    score = 0
                    running = True
                    waiting_for_restart = False

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# End the game
pygame.quit()
