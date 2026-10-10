import pygame
from settings import *

class Snake:
    def __init__(self):
        self.body = [(WIDTH//2, HEIGHT//2)]
        self.direction = (CELL_SIZE, 0)

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != (0, CELL_SIZE):
            self.direction = (0, -CELL_SIZE)
        elif key == pygame.K_DOWN and self.direction != (0, -CELL_SIZE):
            self.direction = (0, CELL_SIZE)
        elif key == pygame.K_LEFT and self.direction != (CELL_SIZE, 0):
            self.direction = (-CELL_SIZE, 0)
        elif key == pygame.K_RIGHT and self.direction != (-CELL_SIZE, 0):
            self.direction = (CELL_SIZE, 0)

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self, food):
        return self.body[0] == food.position

    def draw(self, window):
        for segment in self.body:
            pygame.draw.rect(window, SNAKE_COLOR, (*segment, CELL_SIZE, CELL_SIZE))
