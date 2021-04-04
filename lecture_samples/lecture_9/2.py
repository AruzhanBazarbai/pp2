import pygame
pygame.init()
# RGB(255, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame examples")

done = False
PI = 3.14

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    #line
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    for y in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y], [100, 110 + y], 2)

    #rectangle
    pygame.draw.rect(screen, BLACK, [100, 20, 200, 100], 3)

    #ellipse
    pygame.draw.ellipse(screen, GREEN, [100, 20, 200, 100], 3)

    #arc
    pygame.draw.arc(screen, RED, [100, 200, 200, 100], 0, PI/2, 3)
    pygame.draw.arc(screen, GREEN, [100, 200, 200, 100], PI/2, PI, 3)
    pygame.draw.arc(screen, BLACK, [100, 200, 200, 100], PI, 3*PI/2, 3)
    pygame.draw.arc(screen, BLUE, [100, 200, 200, 100], 3*PI/2, 2*PI, 3)

    #text
    font = pygame.font.Font(None, 50)  #1-p)любой шрифт
    text = font.render("My text", True, RED)  #2-р)сглаживание
    screen.blit(text, (200, 200))

    #text rotating
    font = pygame.font.SysFont("Calibri", 50, True, False)
    text = font.render("Best version", True, BLACK)
    text = pygame.transform.rotate(text, 45)
    screen.blit(text, (0, 0))

    #polygon
    pygame.draw.polygon(screen, RED, [[100, 100], [200, 100], [100, 200], [200, 200], [150, 150]])
    

    pygame.display.flip()

pygame.quit()