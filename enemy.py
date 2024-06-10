import pygame
import random


class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = 0
        self.image = pygame.image.load("enemy.png")
        self.image_size = self.image.get_size()
        scale_size = (50, 60)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def set_location(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def direction_x(self):
        increment_x = random.uniform(-.1, .1)
        return increment_x

    def direction_y(self):
        increment_y = random.uniform(.1, .5)
        return increment_y

    def obstacle_move(self, increment_x, increment_y):
        self.x = self.x + increment_x
        self.y = self.y + increment_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])