import pygame, sys
from random import randrange
pygame.font.init()


RES = 700
SIZE = 25

x, y = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)

length = 1
snake = [(x,y)]

dx, dy = 0, 0

fps = 20

pygame.init()
screen = pygame.display.set_mode((RES,RES))
clock = pygame.time.Clock()

game_speed = 0.5
eaten_apples = 0
current_eaten = 0
score = 0

dirs = {"UP":True,"DOWN":True,"LEFT":True,"RIGHT":True}

font = pygame.font.Font(None, 36)



while True:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    screen.fill("black")

    [(pygame.draw.rect(screen,"green", (i,j,SIZE,SIZE) ) ) for i,j in snake]    
    pygame.draw.rect(screen,"red", (*apple,SIZE,SIZE))

    
    x += dx * (SIZE//2)
    y += dy * (SIZE//2)

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT] and dirs["LEFT"]:
        dx, dy = -game_speed,0
        dirs = {"UP":True,"DOWN":True,"LEFT":True,"RIGHT":False}
    if pressed[pygame.K_RIGHT] and dirs["RIGHT"]:
        dx, dy = game_speed,0
        dirs = {"UP":True,"DOWN":True,"LEFT":False,"RIGHT":True}
    if pressed[pygame.K_UP] and dirs["UP"]:
        dx, dy = 0,-game_speed
        dirs = {"UP":True,"DOWN":False,"LEFT":True,"RIGHT":True}    
    if pressed[pygame.K_DOWN] and dirs["DOWN"]:
        dx, dy = 0,game_speed
        dirs = {"UP":False,"DOWN":True,"LEFT":True,"RIGHT":True}

    if x<-SIZE:
        x = RES 
    elif x>RES:
        x=-SIZE
    if y<-SIZE:
        y = RES 
    elif y>RES:
        y=-SIZE           

    snake.append((x,y))
    snake = snake[-length:] 

    if (snake[-1][0] > apple[0]-SIZE and snake[-1][0] < apple[0]+SIZE) and (snake[-1][1] > apple[1]-SIZE and snake[-1][1] < apple[1]+SIZE):
        apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)   
        length +=1
        eaten_apples += 1
        current_eaten += 1
    if current_eaten==3:
        game_speed+=0.1
        current_eaten=0
        score+=1

    eaten_text = font.render("eaten:"+ str(eaten_apples), True, "green")
    score_text = font.render("score:"+ str(score), True, "white")
    screen.blit(eaten_text,(RES-100,5))
    screen.blit(score_text,(RES-100,35))
    pygame.display.flip()
    clock.tick(fps)    