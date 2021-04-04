import pygame
pygame.init()
#RGB(255, 255, 255)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 255)
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame example")

done = False
PI = 3.14
text_rotate_degrees = 0
clock = pygame.time.Clock()  #FPS chastota peremeshenii

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)

    # text rotating animation
    font = pygame.font.SysFont("Calibri", 50, True, False)
    text = font.render("Best version", True, GREEN)
    text = pygame.transform.rotate(text, text_rotate_degrees)
    screen.blit(text, (130, 130))
    text_rotate_degrees += 1
    clock.tick(100)

    pygame.display.flip()

pygame.quit()