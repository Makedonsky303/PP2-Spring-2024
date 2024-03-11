import pygame
# from pygame import Vector2
import datetime

pygame.init()

time = datetime.datetime.now()

width = 1400
height = 1050

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

done = False

original = pygame.image.load("mainclock.png").convert_alpha()
minutes = pygame.image.load("right_hand.png").convert_alpha()
seconds = pygame.image.load("left_hand.png").convert_alpha()

real_min = time.minute
real_sec = time.second

move_min = -real_min*6 - 50
move_sec = -real_sec*6 - 3


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255,255,255)) 

    screen.blit(original,(0,0))

    sec = seconds.get_rect(center=(width//2, height//2))
    min = minutes.get_rect(center=(width//2, height//2))

    # Повернуть изображение объекта на текущий угол
    rotated_sec = pygame.transform.rotate(seconds, move_sec)
    rotated_min = pygame.transform.rotate(minutes, move_min)

    # Получить прямоугольник ограничивающий повернутое изображение объекта
    rotated_rect1 = rotated_sec.get_rect(center=sec.center)
    rotated_rect2 = rotated_min.get_rect(center=min.center)

    # Отобразить повернутое изображение объекта на экране
    screen.blit(rotated_sec, rotated_rect1)
    screen.blit(rotated_min, rotated_rect2)

    move_sec-=6
    if move_sec==-360:
        move_min-=6
        move_sec=0

    

    pygame.display.flip()
    clock.tick(60) 
    pygame.time.wait(1000)      