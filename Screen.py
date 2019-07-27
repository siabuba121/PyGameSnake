import pygame
from Scene import Scene

class Screen:
    window = None
    lastFrame = 0
    clock = None
    scene = None
    framesCount = 0

    def __init__(self, sizeX, sizeY):
        pygame.init()
        self.window = pygame.display.set_mode((sizeX, sizeY))
        self.clock = pygame.time.Clock()
        self.scene = Scene()

    def update(self):
        self.lastFrame += self.clock.tick()
        if self.lastFrame >= 15:
            self.framesCount+=1
            self.scene.draw(self.window, self.framesCount)
            self.scene.serveFood()
            if self.framesCount == 5:
                self.framesCount = 0
            self.lastFrame = 0
            pygame.display.update(); 
    
    def getKeyInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.scene.snake.moveDirection != "RIGHT":
                self.scene.snake.moveDirection = "LEFT"
        elif keys[pygame.K_RIGHT]:
            if self.scene.snake.moveDirection != "LEFT":
                self.scene.snake.moveDirection = "RIGHT"
        elif keys[pygame.K_UP]:
            if self.scene.snake.moveDirection != "DOWN":
                self.scene.snake.moveDirection = "UP"
        elif keys[pygame.K_DOWN]:
            if self.scene.snake.moveDirection != "UP":
                self.scene.snake.moveDirection = "DOWN"

