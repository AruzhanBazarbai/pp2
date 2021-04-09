#working with wav files
import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))
sound=pygame.mixer.Sound('path_to_wavfile')
sound.play()
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    screen.fill((255,255,255))
    pygame.display.flip()
pygame.quit()