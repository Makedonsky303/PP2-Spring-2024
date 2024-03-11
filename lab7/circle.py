import pygame

pygame.init()

width = 1000
height = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

done = False

color = (0,0,155)

radius = 30
x = 400
y = 300

jumping = False
jump_count = 15
gravity = 0.5  

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True

    screen.fill((255,255,255))
           
    if jumping:
        if y>radius:
            y -= jump_count
        jump_count -= gravity
        if jump_count == 0:  
            jumping = False
            jump_count = 15
    if not jumping and y<height-radius:
        y+=7


    pressed = pygame.key.get_pressed()    


    if pressed[pygame.K_UP] and y>radius: y-=10 
    if pressed[pygame.K_DOWN] and y<height-radius: y+=10
    if pressed[pygame.K_LEFT] and x>radius: x-=10
    if pressed[pygame.K_RIGHT] and x<width-radius: x+=10

    pygame.draw.circle(screen,color,(x,y),radius) 

    clock.tick(60)
    pygame.display.flip() 
    