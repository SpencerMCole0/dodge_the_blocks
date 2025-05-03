import pygame
import os
import sys
from game import Game

def run_game(high_score):
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dodge the Blocks")
    game = Game(screen, high_score)
    return game.run()

def show_game_over_screen(score, high_score):
    font = pygame.font.SysFont(None, 36)
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    WHITE = (255, 255, 255)

    screen.fill(WHITE)
    game_over_text = font.render("Game Over!", True, (200, 0, 0))
    score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
    high_score_text = font.render(f"High Score: {high_score}", True, (0, 0, 0))
    restart_text = font.render("Press R to Restart or Q to Quit", True, (0, 0, 0))

    screen.blit(game_over_text, (200, 100))
    screen.blit(score_text, (200, 150))
    screen.blit(high_score_text, (200, 190))
    screen.blit(restart_text, (120, 250))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Start the game
pygame.init()

# Load high score
high_score_file = "high_score.txt"
if os.path.exists(high_score_file):
    with open(high_score_file, "r") as file:
        content = file.read().strip()
        high_score = int(content) if content.isdigit() else 0
else:
    high_score = 0

while True:
    try:
        final_score, high_score = run_game(high_score)

        # Save high score
        with open(high_score_file, "w") as file:
            file.write(str(high_score))

        show_game_over_screen(final_score, high_score)
    except Exception as e:
        print("An error occurred:", e)
        pygame.quit()
        sys.exit()
