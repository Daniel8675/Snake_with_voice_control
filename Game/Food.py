import pygame
from pygame.math import Vector2
import random


class FOOD:
    def __init__(self, cell_size, cell_number, screen):
        self.x, self.y, self.position = None, None, None
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.food = pygame.image.load("./Graphics/food.png").convert_alpha()
        self.screen = screen
        self.randomize()

    def draw_food(self):
        food_rect = pygame.Rect(self.position.x * self.cell_size, self.position.y * self.cell_size, self.cell_size,
                                self.cell_size)
        self.screen.blit(self.food, food_rect)

    def randomize(self):
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.position = Vector2(self.x, self.y)
