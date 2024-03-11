import pygame

pygame.init()

screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
done = False

def next_song(lst, index):
    if index<len(lst)-1:
        return index+1
    elif index==len(lst)-1:
        return 0
def previous_song(lst, index):
    if index>0:
        return index-1
    elif index==0:
        return len(lst)-1   

songs = ['Imagine Dragons - Believer.mp3', 'MGMT - Little Dark Age.mp3', 'Unknown Brain - War Zone (ft. M.I.M.E).mp3']
current = 0
playing  = False

sound = pygame.mixer.music

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not playing:
                sound.load(songs[current])
                sound.play(0)
                playing = True
            elif event.key == pygame.K_SPACE and playing:
                sound.pause()
                playing = False

            if event.key == pygame.K_RIGHT:
                current = next_song(songs,current)
                print(current)
            elif event.key == pygame.K_LEFT:
                current = previous_song(songs,current)  
                print(current)   

                     
        
    screen.fill((255,255,255))
    
    
    pygame.display.flip()
    clock.tick(60)