import pygame
pygame.init()
G=pygame
#creating display
gamewindow=pygame.display.set_mode((1000,500))
pygame.display.set_caption('My first game')

#Game specific variables
exit_game=False
game_over=False

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==G.KEYDOWN:
            if event.key==G.K_RIGHT:
                print("you have down the right key")
            elif event.key==pygame.K_UP:
                print("you have down the up keY")
            elif event.key==pygame.K_DOWN:
                print("you have down the down ke")
            elif event.key==pygame.K_LEFT:
                print("you have down the left ke")
            
            


pygame.quit()
quit()
