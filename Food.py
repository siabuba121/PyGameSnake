import pygame

class Food:
    x = None
    y = None
    foodColor = (204,0,51)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.foodColor, (self.x,self.y,20,20))