#WORKING WITH IMAGE
import pygame
import os
pygame.init()

screen=pygame.display.set_mode((1200,700))
pygame.display.set_caption("example with image")
done=False
clock=pygame.time.Clock()
_image_library={}

#ТАК МЫ МОЖЕМ ЗАГРУЗИТЬ КАРТИНКУ ТОЛЬКО ОДИН РАЗ И В УАЙЛЕ НЕ БУДЕТ БЕСКОНЕЧНО ЗАГРУЖАТЬСЯ
def get_image(path):
    global _image_library
    image=_image_library.get(path)
    if image is None:
        _path=path.replace('/',os.sep).replace('\\',os.sep)
        image=pygame.image.load(_path)
        _image_library[path]=image
    return image



while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
     
    screen.fill((255,255,255))
    screen.blit(get_image('sk8.bmp'),(0,0))
    # screen.blit(get_image('bf.png'),(0,0))

    pygame.display.flip()
pygame.quit()