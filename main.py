import pygame
import sys
import sounddevice as sd
import threading
import numpy as np
import time

from queue import Queue
from pygame.math import Vector2
from Game.Engine import ENGINE
from Game.Prediction import predict_mic

q = Queue()  # Simple multithreading communication
exit_flag = False


def predict_mice_with_volume_activation(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > 10:
        print(int(volume_norm))
        q.put("pause")
        command = predict_mic()
        q.put(command)
        if command != "stop":
            q.put("start")


def predictions():
    while not exit_flag:
        with sd.Stream(callback=predict_mice_with_volume_activation):
            sd.sleep(10000)


if __name__ == "__main__":

    t1 = threading.Thread(target=predictions, args=())
    t1.start()
    time.sleep(1)

    pygame.init()
    cell_size = 40
    cell_number = 20
    screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))

    clock = pygame.time.Clock()
    SCREEN_UPDATE = pygame.USEREVENT

    pygame.time.set_timer(SCREEN_UPDATE, 150)

    game = ENGINE(cell_size, cell_number, screen)

    paused = True
    instruction = None

    while True:

        if not q.empty():
            instruction = q.get()

        match instruction:
            case "pause":
                paused = True
            case "start":
                paused = False
            case "yes":
                paused = False
            case "up":
                if game.snake.direction != Vector2(0, 1):
                    game.snake.direction = Vector2(0, -1)
            case "down":
                if game.snake.direction != Vector2(0, -1):
                    game.snake.direction = Vector2(0, 1)
            case "left":
                if game.snake.direction != Vector2(1, 0):
                    game.snake.direction = Vector2(-1, 0)
            case "right":
                if game.snake.direction != Vector2(-1, 0):
                    game.snake.direction = Vector2(1, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = True
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if game.snake.direction != Vector2(0, 1):
                        game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if game.snake.direction != Vector2(0, -1):
                        game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if game.snake.direction != Vector2(1, 0):
                        game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if game.snake.direction != Vector2(-1, 0):
                        game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_SPACE:
                    paused = not paused

            if paused:
                continue
            elif event.type == SCREEN_UPDATE:
                game.update()

        instruction = None

        game.draw_elements()
        pygame.display.update()
        clock.tick(60)
