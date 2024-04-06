# Imports
import pygame, sys, time
from pygame.locals import *
import random


# Pygane initializing
pygame.init()

# Screen
WIDTH = 633
HEIGHT = 800
BACKGROUND_COLOR = "white"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Race")

# Game speed
GAME_SPEED = 7

# Score
SCORE = 0


# Setting up FPS 
FPS = 60
clock = pygame.time.Clock()


# Text
pygame.font.init()

f1 = pygame.font.Font(None, 48)
game_over = f1.render("Game Over", True, "black")


background = pygame.image.load("AnimatedStreet.png")
sound = pygame.mixer.music


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(self.rect.width//2-100, WIDTH-self.rect.width//2-100),random.randint(-300,0)) 
        
    def move(self):
        self.rect.move_ip(0,GAME_SPEED)
        if (self.rect.bottom > HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width, WIDTH-self.rect.width-100), random.randint(-300,0))
        
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

class Coin(Enemy):
    def __init__(self):
        super().__init__()  
        self.image = pygame.image.load("coin.png")
    def move(self, touch):
        self.rect.move_ip(0,GAME_SPEED)
        if (self.rect.bottom > HEIGHT or touch):
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width, WIDTH-self.rect.width-100), random.randint(-300,0))
    def draw(self):
        super().draw()
    def get_pos(self):
            
        return (self.rect.x + 10 , self.rect.y + 5)
    def side_move(self):
        self.rect.center = (random.randint(self.rect.width, WIDTH-self.rect.width-100),0)
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2, (HEIGHT*2)//3)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-GAME_SPEED, 0)
        if self.rect.right < WIDTH:        
              if pressed_keys[K_RIGHT] and self.rect.right<WIDTH-100:
                  self.rect.move_ip(GAME_SPEED, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     

# Setting up Sprites   
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
all_coins = pygame.sprite.Group()
all_coins.add(C1)
coin_weigth = 1
coin_weigth_text = f1.render(str(coin_weigth), True, "black")

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

# INC_SPEED = 5

# Game Loop
while True:
    pressed_keys = pygame.key.get_pressed()
    # Cycles through all events occuring
    for event in pygame.event.get():
        if event.type == QUIT or pressed_keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()
        # if event.type == INC_SPEED:
        #     GAME_SPEED += 0.1

    screen.fill(BACKGROUND_COLOR)
    text1 = f1.render(str(SCORE), True, (180, 0, 0))
    
    coin_weigth_text = f1.render(str(coin_weigth), True, "black")

    speed = f1.render(str(GAME_SPEED), True, "black")
    screen.blit(speed, (WIDTH-70,40))
    
    screen.blit(background, (0,0))
    screen.blit(text1,(WIDTH-50,10))
    
    
    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    for coin in all_coins:
        screen.blit(coin.image, coin.rect)
        coin.move(False)
 
    screen.blit(coin_weigth_text,C1.get_pos())


    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        sound.load("Omae_wa_mou_shindeiru.mp3")
        sound.play(0)
        time.sleep(5)
        screen.fill("red")
        screen.blit(game_over, (WIDTH//2 - 100 ,HEIGHT//2-100))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        for coin in all_coins:
            coin.kill()     
        time.sleep(3)
        pygame.quit()
        sys.exit() 
    elif pygame.sprite.spritecollideany(P1, all_coins):
        sound.load("coin_receive.mp3")
        sound.play(0)
        SCORE+=coin_weigth
        GAME_SPEED+=0.1
   
        C1.move(True)
        coin_weigth = random.randrange(1,6)

    elif pygame.sprite.spritecollideany(C1, enemies):    
        C1.side_move()

    pygame.display.update()
    clock.tick(FPS)