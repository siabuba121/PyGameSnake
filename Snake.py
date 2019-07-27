from BodyPart import BodyPart
import pygame
from pygame import Color
from pprint import pprint

class Snake:
    bodyParts = []
    moveDirection = ''
    snakeColor = None
    partSize = 20

    def __init__(self):
        self.moveDirection = "UP"
        self.bodyParts.append(BodyPart(320,240))
        self.snakeColor = (255,255,255)

    def move(self,food):
        newBodyParts = []
        for id,part in enumerate(self.bodyParts):
            if id == 0:
                newPart = BodyPart(part.x, part.y)
                if self.moveDirection == "UP":
                    if newPart.y == 0:
                        newPart.y = 480-self.partSize
                    else:
                        newPart.y -= self.partSize
                elif self.moveDirection == "DOWN":
                    if newPart.y == 460:
                        newPart.y = 0
                    else:
                        newPart.y += self.partSize
                elif self.moveDirection == "LEFT":
                    if newPart.x == 0:
                        newPart.x = 640 - self.partSize
                    else:
                        newPart.x -= self.partSize
                elif self.moveDirection == "RIGHT":
                    if newPart.x == 620:
                        newPart.x = 0
                    else:
                        newPart.x += self.partSize
                newBodyParts.append(newPart)
            else:
                newPart = BodyPart(self.bodyParts[id-1].x,self.bodyParts[id-1].y)
                newBodyParts.append(newPart)
        eaten = False
        if newBodyParts[0].x == food.x and newBodyParts[0].y == food.y:
            eaten = True
            newPart = BodyPart(self.bodyParts[-1].x, self.bodyParts[-1].y)
            if len(self.bodyParts) == 1:
                print("only one")
                if self.moveDirection == "UP":
                    newPart.y -= self.partSize
                elif self.moveDirection == "DOWN":
                    newPart.y += self.partSize
                elif self.moveDirection == "LEFT":
                    newPart.x -= self.partSize
                elif self.moveDirection == "RIGHT":
                    newPart.x += self.partSize                
            newBodyParts.append(newPart)
        self.bodyParts = newBodyParts
        self.checkForCollision()
        return eaten

    def draw(self, screen):
        for part in self.bodyParts:
            pygame.draw.rect(screen, self.snakeColor, (part.x,part.y,20,20))
    
    def checkForCollision(self):
        if len(self.bodyParts) == 2:
            return
        for id,part in enumerate(self.bodyParts):
            for idToCheck, partTocheck in enumerate(self.bodyParts):
                if id != idToCheck and part.x == partTocheck.x and part.y == partTocheck.y:
                    self.reset()

    def reset(self):
        self.bodyParts = []
        self.__init__()


