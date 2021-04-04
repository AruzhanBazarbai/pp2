import pygame
import random
pygame.init()
#RGB(255, 255, 255)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 255)
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame example")
clock = pygame.time.Clock() #FPS
colors = [WHITE, GREEN, RED, BLUE]

done = False
x = 100
y = 100
color = WHITE
dx = 1
dy = 0
speed = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            dy = 1 * speed
            dx = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            dy = -1 * speed
            dx = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            dy = 0
            dx = 1 * speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            dy = 0
            dx = -1 * speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed += 1

    screen.fill(BLACK)

    #animation
    x += dx
    y += dy
    if x > 700:
        x = 0
    if x < 0:
        x = 700
    if y > 500:
        y = 0
    if y < 0:
        y = 500
    pygame.draw.ellipse(screen, color, [x, y, 20, 20])

    clock.tick(60)

    pygame.display.flip()

pygame.quit()