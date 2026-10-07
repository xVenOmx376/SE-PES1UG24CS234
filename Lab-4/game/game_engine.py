import pygame
import random
from .player import Player
from .enemy import EnemyGrid
from .bullet import Bullet

# Game Engine

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (220, 60, 60)

class GameEngine:
    def __init__(self, width, height, difficulty="medium"):
        self.width = width
        self.height = height
        
        pygame.mixer.init()

        self.shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
        self.enemy_destroyed_sound = pygame.mixer.Sound("sounds/enemy_destroyed.wav")
        self.game_over_sound = pygame.mixer.Sound("sounds/game_over.wav")

        self.player = Player(width // 2 - 20, height - 50, 40, 20)
        self.difficulty = difficulty

        difficulty_settings = {
            "easy": {"speed": 1.0, "fire_chance": 0.005},
            "medium": {"speed": 1.5, "fire_chance": 0.01},
            "hard": {"speed": 2.5, "fire_chance": 0.02},
        }

        settings = difficulty_settings[difficulty]

        self.enemy_grid = EnemyGrid(width, speed=settings["speed"])

        self.player_bullets = []
        self.enemy_bullets = []
        self._shoot_cooldown = 0
        self.enemy_fire_chance = settings["fire_chance"]

        self.score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.game_over_font = pygame.font.SysFont("Arial", 60, bold=True)
        self.game_over_text_font = pygame.font.SysFont("Arial", 28)
        self.game_over = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.game_over:
                if event.key == pygame.K_r:
                    self.__init__(self.width, self.height, self.difficulty)
                elif event.key == pygame.K_q:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                return

            if event.key == pygame.K_SPACE:
                if self._shoot_cooldown <= 0:
                    bullet_x = self.player.center_x() - 2
                    self.player_bullets.append(
                        Bullet(bullet_x, self.player.y, direction=-1)
                    )
                    self.shoot_sound.play()
                    self._shoot_cooldown = 15

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move(-self.player.speed, self.width)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move(self.player.speed, self.width)

    def update(self):
        if self.game_over:
            return

        if self._shoot_cooldown > 0:
            self._shoot_cooldown -= 1

        self.enemy_grid.move()

        for enemy in self.enemy_grid.alive_enemies():
            if random.random() < self.enemy_fire_chance:
                bullet_x = enemy.x + enemy.width // 2
                self.enemy_bullets.append(Bullet(bullet_x, enemy.y + enemy.height, direction=1))

        for bullet in self.player_bullets:
            bullet.move()
        for bullet in self.enemy_bullets:
            bullet.move()

        self.player_bullets = [b for b in self.player_bullets if not b.off_screen(self.height)]
        self.enemy_bullets = [b for b in self.enemy_bullets if not b.off_screen(self.height)]

        # NOTE: this removes a bullet from player_bullets while iterating
        # directly over that same list. Python skips the element right
        # after a removed one, so when two enemies are hit on the same
        # frame the second collision can be missed - the bullet appears
        # to pass straight through. See Task 1 in the README.
        
        remaining_bullets = []
        for bullet in self.player_bullets:
            hit = False

            for enemy in self.enemy_grid.alive_enemies():
                if bullet.rect().colliderect(enemy.rect()):
                    enemy.alive = False
                    self.score += 1
                    self.enemy_destroyed_sound.play()
                    hit = True
                    break

            if not hit:
                remaining_bullets.append(bullet)

        self.player_bullets = remaining_bullets

        for bullet in self.enemy_bullets:
            if bullet.rect().colliderect(self.player.rect()):
                self.game_over = True
                self.game_over_sound.play()
                break

        if self.enemy_grid.reached_bottom(self.player.y):
            self.game_over = True
            self.game_over_sound.play()

    def render(self, screen):
        pygame.draw.rect(screen, GREEN, self.player.rect())

        for enemy in self.enemy_grid.alive_enemies():
            pygame.draw.rect(screen, WHITE, enemy.rect())

        for bullet in self.player_bullets:
            pygame.draw.rect(screen, WHITE, bullet.rect())
        for bullet in self.enemy_bullets:
            pygame.draw.rect(screen, RED, bullet.rect())

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        if self.game_over:
            overlay = pygame.Surface((self.width, self.height))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            game_over_text = self.game_over_font.render("GAME OVER", True, RED)
            score_text = self.game_over_text_font.render(
                f"Final Score: {self.score}", True, WHITE
            )
            restart_text = self.game_over_text_font.render(
                "Press R to Restart", True, WHITE
            )
            quit_text = self.game_over_text_font.render(
                "Press Q to Quit", True, WHITE
            )

            screen.blit(
                game_over_text,
                game_over_text.get_rect(center=(self.width // 2, self.height // 2 - 100))
            )
            screen.blit(
                score_text,
                score_text.get_rect(center=(self.width // 2, self.height // 2 - 20))
            )
            screen.blit(
                restart_text,
                restart_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
            )
            screen.blit(
                quit_text,
                quit_text.get_rect(center=(self.width // 2, self.height // 2 + 90))
            )
