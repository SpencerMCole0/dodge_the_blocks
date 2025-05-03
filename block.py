import pygame
import random

class Block:
    def __init__(self, x, y, size, speed, color):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color

    def move(self):
        self.y += self.speed

    def reset(self, screen_width):
        self.y = -self.size
        self.x = random.randint(0, screen_width - self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)
