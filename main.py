import pygame
from Screen import Screen
from sys import exit

screen = Screen(640,480)
# utworzenie okna
while True:
    screen.update()
    screen.getKeyInput()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()