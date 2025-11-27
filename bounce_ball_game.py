import pygame
import sys
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")  

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (50, 150, 255)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()

# ============================
# SPEED SELECT MENU (FIXED)
# ============================
def speed_menu():
    while True:
        screen.fill(BLUE)

        title = font.render("Select Speed:", True, WHITE)
        s1 = font.render("1 - Slow", True, YELLOW)
        s2 = font.render("2 - Normal", True, YELLOW)
        s3 = font.render("3 - Fast", True, YELLOW)
        exit_msg = font.render("Press ESC to Exit", True, WHITE)

        screen.blit(title, (230, 120))
        screen.blit(s1, (245, 160))
        screen.blit(s2, (245, 190))
        screen.blit(s3, (245, 220))
        screen.blit(exit_msg, (210, 260))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # ✅ Proper key detection
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 2  # Slow
                if event.key == pygame.K_2:
                    return 3  # Normal
                if event.key == pygame.K_3:
                    return 5  # Fast
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        clock.tick(30)

# ✅ Get selected speed
base_speed = speed_menu()

# Paddle
paddle_width, paddle_height = 100, 10
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 30
paddle_speed = 6

# Ball setup using selected speed
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_radius = 10
ball_dx = random.choice([-base_speed, base_speed])
ball_dy = -base_speed

# Score & Level
score = 0
level = 1

# ============================
# MAIN GAME LOOP
# ============================
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Paddle movement
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Wall bounce
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1

    # Paddle collision
    if paddle_y - ball_radius <= ball_y <= paddle_y and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_dy *= -1
        score += 1

        # Level up
        if score % 5 == 0:
            level += 1
            ball_dx *= 1.2
            ball_dy *= 1.2

    # Ball falls below
    if ball_y > HEIGHT:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = random.choice([-base_speed, base_speed])
        ball_dy = -base_speed
        score = 0
        level = 1

    # Draw graphics
    screen.fill(BLUE)
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Display Score + Level
    score_text = font.render(f"Score: {score}", True, YELLOW)
    level_text = font.render(f"Level: {level}", True, YELLOW)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 35))

    pygame.display.update()
    clock.tick(60)
