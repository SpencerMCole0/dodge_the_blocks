import pygame

class Player:
    def __init__(self, x, y, size, speed, color):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color

    def move(self, keys, screen_width):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < screen_width - self.size:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)
