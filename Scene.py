from Snake import Snake
from Food import Food
import random
import pygame

class Scene:
    snake = None
    food = None

    def __init__(self):
        self.snake = Snake()

    def drawPoints(self, screen):
        font = pygame.font.Font('freesansbold.ttf',25)
        text = font.render("Score: "+str(len(self.snake.bodyParts)-1), True, (0, 171, 89))
        screen.blit(text, (10,10))


    def draw(self, screen, frames):
        screen.fill((0,0,0))
        self.drawPoints(screen)
        self.snake.draw(screen)
        if self.food != None:
            self.food.draw(screen)
        if frames == 5:
            eaten = self.snake.move(self.food)
            if eaten == True:
                self.food = None
    
    def serveFood(self):
        if self.food == None:
            foodCollision = True
            while foodCollision:
                x = random.randrange((640-self.snake.partSize)/self.snake.partSize)
                y = random.randrange((480-self.snake.partSize)/self.snake.partSize)
                x *= self.snake.partSize
                y *= self.snake.partSize

                for part in self.snake.bodyParts:
                    if part.x == x and part.y == y:
                        continue
                foodCollision = False
            self.food = Food(x,y)

