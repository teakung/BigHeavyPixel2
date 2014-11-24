import pygame
from pygame.locals import *

class Rain(object):

    def __init__(self,pos,speed=(0,10)):
        self.x, self.y = pos
        self.vx, self.vy = speed
        self.rect = Rect(self.x, self.y , 50, 100)

    def updatePos(self,surface):
        self.x += self.vx
        self.y += self.vy
        self.rect = Rect(self.x, self.y , 50, 100)
        horiBorder = surface.get_width()
        verBorder = surface.get_height()
        self.checkBorder(horiBorder,verBorder)
        
    def checkBorder(self, horiBorder,verBorder):
        if self.y >= verBorder:
            self.y = 0
        # if self.x >= horiBorder:
        #     self.x = 0
        # elif self.x <= horiBorder:
        #     self.x = horiBorder

    def render(self,surface):
        pos = (int(self.x),int(self.y))
        pygame.draw.rect(surface,(100,100,100),self.rect)



