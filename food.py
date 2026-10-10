import pygame
import random
from settings import *

class Food:
    def __init__(self):
        self.randomize_position()

    def randomize_position(self):
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        self.position = (x, y)

    def draw(self, window):
        pygame.draw.rect(window, FOOD_COLOR, (*self.position, CELL_SIZE, CELL_SIZE))
