import pygame, random

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(size)
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock
# TODO: make a variable (constant) called FPS and initialize to 20
FPS = 20
clock = pygame.time.Clock()

# Set game values
# TODO: make a variable (constant) named SNAKE_SIZE and initialize to 20
SNAKE_SIZE = 20

# TODO: make a variable named head_x and assign half of the WINDOW_WIDTH to it.  use integer division //
head_x = WINDOW_WIDTH // 2
# TODO: make a variable named head_y and assign half of the WINDOW_HEIGHT + 100 to it.  use integer division //
head_y = (WINDOW_HEIGHT // 2) + 100

# TODO: make a variable named snake_dx and assign 0 to it.
snake_dx = 0
# TODO: repeat for a variable named snake_dy
snake_dy = 0

# TODO: make a variable named score and assign 0 to it.
score = 0

# Set colors
GREEN = (0, 255, 0)
# TODO: make a DARKGREEN color with rgb(10, 50, 10)
DARKGREEN = (10, 50, 10)
# TODO: make a RED
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
# TODO: make a WHITE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set fonts
font = pygame.font.SysFont('gabriola', 48)

# Set text
title_text = font.render("~~Snake~~", True, GREEN, DARKRED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# TODO: make a score_text object...
score_text = font.render("Score: 0", True, GREEN, DARKRED)
# TODO: make a score_rect object
score_rect = score_text.get_rect()
# TODO: place the topleft
score_rect.topleft = (10, 10)

# TODO: game_over_text
game_over_text = font.render("GAMEOVER", True, RED, DARKRED)
# TODO: game_over_rect
game_over_rect = game_over_text.get_rect()
# TODO: center placement
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# TODO: continue_text
continue_text = font.render("Press any key to play again", True, RED, DARKGREEN)
# TODO: continue_rect
continue_rect = continue_text.get_rect()
# TODO: placement
continue_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 64)

# Set sounds and music
pick_up_sound = pygame.mixer.Sound("pick_up_sound.wav")

# Set images
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

# TODO: head_coord
head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
# TODO: head_rect
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

body_coords = []

running = True
is_paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake
        # TODO: check KEYDOWN
        if event.type == pygame.KEYDOWN:
            # TODO: K_LEFT
            if event.key == pygame.K_LEFT:
                snake_dx = -SNAKE_SIZE
                snake_dy = 0
            # TODO: K_RIGHT
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            # TODO: K_UP
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -SNAKE_SIZE
            # TODO: K_DOWN
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    # TODO: insert body
    body_coords.insert(0, head_coord)
    # TODO: pop
    body_coords.pop()

    # TODO: add dx/dy
    head_x += snake_dx
    head_y += snake_dy
    # TODO: update head_coord
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    head_rect = pygame.Rect(head_coord)

    if head_x < 0 or head_x + SNAKE_SIZE > WINDOW_WIDTH or head_y < 0 or head_y + SNAKE_SIZE > WINDOW_HEIGHT or head_coord in body_coords:
        # TODO: blit
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        # TODO: update
        pygame.display.update()
        # TODO: pause
        is_paused = True

    while is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_paused = False
                running = False
            # TODO: KEYDOWN reset
            if event.type == pygame.KEYDOWN:
                score = 0
                head_x = WINDOW_WIDTH // 2
                head_y = (WINDOW_HEIGHT // 2) + 100
                head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
                body_coords = []
                snake_dx = 0
                snake_dy = 0
                is_paused = False

    if head_rect.colliderect(apple_rect):
        # TODO: score + 1
        score += 1
        # TODO: play
        pick_up_sound.play()

        # TODO: random apple coords
        apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)

        # TODO: append body
        body_coords.append(head_coord)

    # TODO: update score_text
    score_text = font.render(f"Score: {score}", True, GREEN, DARKRED)

    # TODO: fill WHITE
    display_surface.fill(BLACK)

    # TODO: blit title + score
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)

    # TODO: draw bodies, head, apple
    for body in body_coords:
        pygame.draw.rect(display_surface, DARKGREEN, body)
    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

    # TODO: update + tick
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
