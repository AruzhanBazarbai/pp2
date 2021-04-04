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
rect_x = 50
rect_y = 50
a = 2
b = 2
color = WHITE

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            color = colors[random.randint(0, 3)]

    screen.fill(BLACK)

    # animation
    rect_y += b
    rect_x += a

    font = pygame.font.Font(None, 50)
    text = font.render("HELLO WORLD!!!", True, GREEN)


    if rect_x > 650 or rect_x < 0:
        a *= -1
        screen.blit(text, (200, 250))
    if rect_y > 450 or rect_y < 0:
        b *= -1
        screen.blit(text, (200, 250))

    pygame.draw.rect(screen, color, (rect_x, rect_y, 50, 50))
    pygame.draw.rect(screen, RED, (rect_x + 10, rect_y + 10, 30, 30))

    clock.tick(60)

    pygame.display.flip()

pygame.quit()