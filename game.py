import pygame
import sys
import random
from player import Player
from block import Block

class Game:
    def __init__(self, screen, high_score):
        self.WIDTH, self.HEIGHT = screen.get_size()
        self.screen = screen
        self.high_score = high_score
        self.score = 0
        self.lives = 3
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)

        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.BLUE = (50, 150, 255)

        self.player = Player(
            x=self.WIDTH // 2 - 25,
            y=self.HEIGHT - 60,
            size=50,
            speed=5,
            color=self.BLUE
        )

        self.block_size = 50
        self.base_speed = 5
        self.num_blocks = 3
        self.blocks = []
        for _ in range(self.num_blocks):
            x = random.randint(0, self.WIDTH - self.block_size)
            y = random.randint(-300, -self.block_size)
            block = Block(x, y, self.block_size, self.base_speed, self.RED)
            self.blocks.append(block)

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            self.screen.fill(self.WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update()
            self.draw()

            if self.lives <= 0:
                return self.score, max(self.score, self.high_score)

            pygame.display.flip()

    def update(self):
        block_speed = self.base_speed + (self.score // 10)
        keys = pygame.key.get_pressed()
        self.player.move(keys, self.WIDTH)

        player_rect = self.player.get_rect()
        for block in self.blocks:
            block.speed = block_speed
            block.move()

            if block.y > self.HEIGHT:
                block.reset(self.WIDTH)
                self.score += 1

            if player_rect.colliderect(block.get_rect()):
                self.lives -= 1
                block.reset(self.WIDTH)

    def draw(self):
        self.player.draw(self.screen)
        for block in self.blocks:
            block.draw(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        lives_text = self.font.render(f"Lives: {self.lives}", True, (0, 0, 0))
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 40))
        self.screen.blit(high_score_text, (10, 70))
