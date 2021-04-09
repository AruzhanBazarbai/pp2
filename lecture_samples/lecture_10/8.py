#Working with music
import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.mixer.music.load('path_to_file')
pygame.mixer.music.play()
# pygame.mixer.music.play(-1) - музыка будет бесконечно играть
# pygame.mixer.play.stop() -останавливает музыку, например с помощью условии нажатием клавиш

SONG_END=pygame.USEREVENT+1
pygame.mixer.music.set_endevent(SONG_END)
#когда музыка останавливается то функция set_endevent отправляет этот сигнал
# в очередь событии 
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==SONG_END:
            print("the song ended!") #отлавливаем ивент когда музыка заканчивается
     
    screen.fill((255,255,255))

    pygame.display.flip()
pygame.quit()