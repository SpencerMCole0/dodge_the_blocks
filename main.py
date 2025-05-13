import pygame
import os
import sys
from game import Game

def show_start_screen():
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (50, 150, 255)

    title_font = pygame.font.SysFont(None, 64)
    subtitle_font = pygame.font.SysFont(None, 36)
    start_font = pygame.font.SysFont(None, 28)

    difficulty = None

    # Difficulty selection screen
    screen.fill(WHITE)
    title_text = title_font.render("Dodge the Blocks", True, BLACK)
    subtitle_text = subtitle_font.render("Avoid falling blocks. Survive as long as you can!", True, BLACK)
    diff_text = start_font.render("Select Difficulty: 1 = Easy, 2 = Normal, 3 = Hard", True, BLACK)

    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 60))
    screen.blit(subtitle_text, (WIDTH // 2 - subtitle_text.get_width() // 2, 120))
    screen.blit(diff_text, (WIDTH // 2 - diff_text.get_width() // 2, 200))
    pygame.display.flip()

    while difficulty is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    difficulty = "easy"
                elif event.key in [pygame.K_2, pygame.K_KP2]:
                    difficulty = "normal"
                elif event.key in [pygame.K_3, pygame.K_KP3]:
                    difficulty = "hard"

    # Confirm with "Press SPACE to Start"
    screen.fill(WHITE)
    confirm_text = start_font.render(f"Difficulty selected: {difficulty.title()}", True, BLACK)
    start_text = start_font.render("Press SPACE to Start", True, WHITE)

    # Draw button background
    box_width, box_height = 300, 50
    box_x = WIDTH // 2 - box_width // 2
    box_y = 250
    pygame.draw.rect(screen, BLUE, (box_x, box_y, box_width, box_height), border_radius=10)

    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 60))
    screen.blit(confirm_text, (WIDTH // 2 - confirm_text.get_width() // 2, 140))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, box_y + 10))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

    return difficulty

def run_game(high_score, difficulty):
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dodge the Blocks")
    game = Game(screen, high_score, difficulty)
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
        difficulty = show_start_screen()
        final_score, high_score = run_game(high_score, difficulty)

        # Save high score
        with open(high_score_file, "w") as file:
            file.write(str(high_score))

        show_game_over_screen(final_score, high_score)
    except Exception as e:
        print("An error occurred:", e)
        pygame.quit()
        sys.exit()
