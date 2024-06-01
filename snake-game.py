import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Snake properties
snake_block = 10
snake_speed = 15

# Fonts
font = pygame.font.SysFont(None, 25)

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(WIN, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    WIN.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def gameLoop():
    game_over = False
    game_close = False

    # Initial position and movement of the snake
    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0

    # Initial length of the snake
    snake_list = []
    length_of_snake = 1

    # Initial position of the food
    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    # Main game loop
    while not game_over:
        while game_close:
            WIN.fill(BLACK)
            message("You lost! Press Q to Quit or C to play again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Update snake's position
        x1 += x1_change
        y1 += y1_change

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            length_of_snake += 1
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

        # Draw the snake and food
        WIN.fill(BLACK)
        pygame.draw.rect(WIN, RED, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake hits itself or the wall
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # Draw the snake and update display
        snake(snake_block, snake_list)
        pygame.display.update()

        # Adjust game speed
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
