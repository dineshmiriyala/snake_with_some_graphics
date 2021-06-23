import pygame
import sys
import random
from pygame.math import Vector2

class FOOD:

    def __init__(self):
        self.x = random.randint(0 , pixels - 1)
        self.y =random.randint(0 , pixels - 1)
        self.position = Vector2(self.x , self.y)

    def draw_snake(self):
        food_rect = pygame.Rect(self.position.x * pixel_size , self.position.y * pixel_size , pixel_size , pixel_size)
        pygame.draw.rect(screen , (200 , 0 , 0) , food_rect)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10) , Vector2(4, 10) , Vector2(3 , 10)]

    def draw_snake(self):
        for vector in self.body:
            food_rect = pygame.Rect(vector.x * pixel_size, vector.y * pixel_size, pixel_size, pixel_size)
            pygame.draw.rect(screen, (0, 0, 200), food_rect)


pygame.init()

pygame.display.set_caption('Snake game by Dinesh')
pixel_size = 20
pixels = 30

screen = pygame.display.set_mode((pixels*pixel_size , pixels*pixel_size))
clock = pygame.time.Clock()
food = FOOD()
snake = SNAKE()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pygame.Color(0 , 126 , 0))
    food.draw_snake()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(144)
