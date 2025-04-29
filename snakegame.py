import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set display size
width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define colors using RGB values
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake and food size
block_size = 20
snake_speed = 10

# Set up the clock for controlling frame rate
clock = pygame.time.Clock()

# Set fonts for messages and score display
font_style = pygame.font.SysFont(None, 40)
score_font = pygame.font.SysFont(None, 30)

# Function to draw the snake on the screen
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, green, [x[0], x[1], snake_block, snake_block])

# Function to display the current score
def show_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    win.blit(value, [0, 0])

# Function to display a message on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

# Main game loop function
def game_loop():
    game_over = False  # Game over flag
    game_close = False  # Game close flag when player loses

    # Starting position of the snake
    x1 = width / 2
    y1 = height / 2

    # Snake movement variables
    x1_change = 0
    y1_change = 0

    # Snake body list and initial length
    snake_List = []
    Length_of_snake = 1

    # Random position for food
    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        # If player loses, give options to quit or restart
        while game_close:
            win.fill(blue)
            message("Game Over! Press C-Play Again or Q-Quit", red)
            show_score(Length_of_snake - 1)
            pygame.display.update()

            # Handle key presses in game over screen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Quit game
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Restart game
                        game_loop()

        # Handle movement and direction keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = block_size
                    x1_change = 0

        # Check for collision with boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        win.fill(black)

        # Draw the food
        pygame.draw.rect(win, red, [foodx, foody, block_size, block_size])

        # Update snake body list
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if the snake hits itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw the updated snake and score
        draw_snake(block_size, snake_List)
        show_score(Length_of_snake - 1)
        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            Length_of_snake += 1  # Increase snake size

        # Control the speed of the snake
        clock.tick(snake_speed)

    # Exit pygame when game is over
    pygame.quit()
    quit()

# Start the game
game_loop()