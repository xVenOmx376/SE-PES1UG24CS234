import pygame
from game.game_engine import GameEngine

pygame.init()

WIDTH, HEIGHT = 600, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders - Pygame Version")

BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60


def select_difficulty():
    font = pygame.font.SysFont("Arial", 40)
    small_font = pygame.font.SysFont("Arial", 28)

    while True:
        SCREEN.fill(BLACK)

        title = font.render("SPACE INVADERS", True, (255, 255, 255))
        prompt = small_font.render("Select Difficulty", True, (255, 255, 255))
        easy = small_font.render("1 - Easy", True, (255, 255, 255))
        medium = small_font.render("2 - Medium", True, (255, 255, 255))
        hard = small_font.render("3 - Hard", True, (255, 255, 255))

        SCREEN.blit(title, title.get_rect(center=(WIDTH // 2, 180)))
        SCREEN.blit(prompt, prompt.get_rect(center=(WIDTH // 2, 280)))
        SCREEN.blit(easy, easy.get_rect(center=(WIDTH // 2, 350)))
        SCREEN.blit(medium, medium.get_rect(center=(WIDTH // 2, 400)))
        SCREEN.blit(hard, hard.get_rect(center=(WIDTH // 2, 450)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "easy"
                elif event.key == pygame.K_2:
                    return "medium"
                elif event.key == pygame.K_3:
                    return "hard"


def main():
    difficulty = select_difficulty()

    if difficulty is None:
        pygame.quit()
        return

    engine = GameEngine(WIDTH, HEIGHT, difficulty)

    running = True
    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            engine.handle_event(event)

        engine.handle_input()
        engine.update()
        engine.render(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()