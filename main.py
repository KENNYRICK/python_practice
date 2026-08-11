import pygame
import sys

# Start Pygame
pygame.init()

# Window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Frogger Game")

# Game clock
clock = pygame.time.Clock()

# Colors
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (200, 0, 0)

# Frog
frog = pygame.Rect(380, 540, 40, 40)

# Car
car = pygame.Rect(100, 400, 80, 40)
car_speed = 5

# Main game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Move frog
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                frog.y -= 40
            elif event.key == pygame.K_DOWN:
                frog.y += 40
            elif event.key == pygame.K_LEFT:
                frog.x -= 40
            elif event.key == pygame.K_RIGHT:
                frog.x += 40

    # Move car
    car.x += car_speed

    # If car leaves screen, put it back
    if car.x > WIDTH:
        car.x = -80

    # Check collision
    if frog.colliderect(car):
        print("GAME OVER!")
        frog.x = 380
        frog.y = 540

    # Draw background
    screen.fill(GRAY)

    # Draw frog
    pygame.draw.rect(screen, GREEN, frog)

    # Draw car
    pygame.draw.rect(screen, RED, car)

    # Update screen
    pygame.display.flip()

    # 60 frames per second
    clock.tick(60)
