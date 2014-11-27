import pygame
from pygame.locals import *

import pyganim

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
        if self.x >= horiBorder:
            self.x = 0
        elif self.x <= 0:
            self.x = horiBorder

    def randomX(self):
        temp = random.randint(0,9)
        pass

    def render(self,surface):
        # pos = (int(self.x),int(self.y))
        pygame.draw.rect(surface,(100,100,100),self.rect)


class Player(object):

    def __init__(self,pos,speed=(10,10)):
        self.x, self.y = pos
        self.vx, self.vy = speed
        self.ani = pyganim.PygAnimation([('blackcatSprite/1.png', 0.1),
                                 ('blackcatSprite/2.png', 0.1),
                                 ('blackcatSprite/3.png', 0.1),
                                 ('blackcatSprite/4.png', 0.1),
                                 ('blackcatSprite/5.png', 0.1),
                                ])
        self.ani.play()
        # self.rect = self.image.get_rect()
        
    def move_up(self):
        self.y += vy

    def move_down(self):
        self.y -= vy

    def move_left(self):
        self.x -= vx

    def move_right(self):
        self.x += vx 

    def render(self,surface):
        pos = (int(self.x),int(self.y))
        self.ani.blit(surface, pos)