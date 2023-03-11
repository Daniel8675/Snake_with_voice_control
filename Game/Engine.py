import pygame
import sys
from Game.Food import FOOD
from Game.Snake import SNAKE


class ENGINE:
    def __init__(self, cell_size, cell_number, screen):
        self.snake = SNAKE(cell_size, screen)
        self.food = FOOD(cell_size, cell_number, screen)
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = screen

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.food.draw_food()
        self.snake.draw_snake()

    def check_collision(self):
        if self.food.position == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.food.position:
                self.food.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.cell_number:
            self.snake.body[0].x = self.snake.body[0].x % self.cell_number
            # self.game_over()
        if not 0 <= self.snake.body[0].y < self.cell_number:
            self.snake.body[0].y = self.snake.body[0].y % self.cell_number
            # self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    @staticmethod
    def game_over():
        pygame.quit()
        sys.exit()

    def draw_grass(self):
        green_color = (0, 105, 60, 0)  # pygame.Color(0, 105, 60, 10)
        black_color = (30, 30, 30, 0)
        red_color = (167, 25, 48, 0)

        for row in range(self.cell_number):
            if row % 3 == 0:
                for column in range(self.cell_number):
                    if column % 3 == 0:
                        grass_rect = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size,
                                                 self.cell_size)
                        pygame.draw.rect(self.screen, green_color, grass_rect)
                    if column % 3 == 1:
                        grass_rect = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size,
                                                 self.cell_size)
                        pygame.draw.rect(self.screen, black_color, grass_rect)
                    if column % 3 == 2:
                        grass_rect = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size,
                                                 self.cell_size)
                        pygame.draw.rect(self.screen, red_color, grass_rect)
            elif row % 3 == 1:
                for column in range(self.cell_number):
                    if column % 3 == 0:
                        grass_rect = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size,
                                                 self.cell_size)
                        pygame.draw.rect(self.screen, black_color, grass_rect)
                    if column % 3 == 1:
                        grass_rect = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size,
                                                 self.cell_size)
                        pygame.draw.rect(self.screen, red_color, grass_rect)
                    if column % 3 == 2:
                        grass_rect = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size,
                                                 self.cell_size)
                        pygame.draw.rect(self.screen, green_color, grass_rect)
            else:
                for column in range(self.cell_number):
                    if column % 3 == 0:
                        grass_rect = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size,
                                                 self.cell_size)
                        pygame.draw.rect(self.screen, red_color, grass_rect)
                    if column % 3 == 1:
                        grass_rect = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size,
                                                 self.cell_size)
                        pygame.draw.rect(self.screen, green_color, grass_rect)
                    if column % 3 == 2:
                        grass_rect = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size,
                                                 self.cell_size)
                        pygame.draw.rect(self.screen, black_color, grass_rect)
