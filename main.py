import pygame
import sys
import random
from pygame.math import Vector2

class FOOD:

    def __init__(self):
        self.random()


    def draw_food(self):
        food_rect = pygame.Rect(self.position.x * pixel_size , self.position.y * pixel_size , pixel_size , pixel_size)
        pygame.draw.rect(screen , (200 , 0 , 0) , food_rect)

    def random(self):
        self.x = random.randint(0, pixels - 1)
        self.y = random.randint(0, pixels - 1)
        self.position = Vector2(self.x, self.y)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10) , Vector2(4, 10) , Vector2(3 , 10)]
        self.direction = Vector2( 1 , 0)
        self.ate = False

    def draw_snake(self):
        for vector in self.body:
            x_pos = vector.x * pixel_size
            y_pos = vector.y * pixel_size
            snake_rect = pygame.Rect(x_pos, y_pos, pixel_size, pixel_size)
            pygame.draw.rect(screen, (0, 0, 200), snake_rect)

    def move_snake(self):
        if not self.ate:
            body_copy = self.body[: - 1]
            body_copy.insert(0 , body_copy[0] + self.direction)
            self.body = body_copy
        else:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.ate = False


    def addlength(self):
        self.ate = True



class MAIN:
    def __init__(self):
        self.food = FOOD()
        self.snake = SNAKE()

    def update(self):
        self.snake.move_snake()
        self.snake_eat()
        self.error()

    def draw_elments(self):
        game_init.food.draw_food()
        game_init.snake.draw_snake()

    def snake_eat(self):
        if self.food.position == self.snake.body[0]:
            self.food.random()
            self.snake.addlength()

    def error(self):
        if (not 0 <= self.snake.body[0].x < pixels) or (not 0 <= self.snake.body[0].y < pixels):
            self.gameover()
        for block in self.snake.body[1 : ]:
            if block == self.snake.body[0]:
                self.gameover()

    def gameover(self):
        pygame.quit()
        sys.exit()





pygame.init()

pygame.display.set_caption('Snake game by Dinesh')
pixel_size = 20
pixels = 30

screen = pygame.display.set_mode((pixels*pixel_size , pixels*pixel_size))
clock = pygame.time.Clock()


game_init = MAIN()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE , 150)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_init.gameover()
        if event.type == SCREEN_UPDATE:
            game_init.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game_init.snake.direction.y != 1:
                    game_init.snake.direction = Vector2(0 , -1)
            if event.key == pygame.K_DOWN:
                if game_init.snake.direction.y != -1:
                    game_init.snake.direction = Vector2(0 , 1)
            if event.key == pygame.K_RIGHT:
                if game_init.snake.direction.x != -1:
                    game_init.snake.direction = Vector2(1 , 0)
            if event.key == pygame.K_LEFT:
                if game_init.snake.direction.x != 1:
                    game_init.snake.direction = Vector2(-1 , 0)
    screen.fill(pygame.Color(0 , 126 , 0))
    game_init.draw_elments()
    pygame.display.update()
    clock.tick(144)
