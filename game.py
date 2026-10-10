import pygame
from snake import Snake
from food import Food
from settings import *

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = Snake()
food = Food()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            snake.change_direction(event.key)

    snake.move()

    if snake.check_collision(food):
        food.randomize_position()
        snake.grow()

    window.fill(BACKGROUND_COLOR)
    snake.draw(window)
    food.draw(window)

    pygame.display.update()

pygame.quit()
