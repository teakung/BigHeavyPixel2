import pygame,random
from pygame.locals import *

import pyganim

rain_width = 50
rain_height = 100

class Rain(object):

    def __init__(self,pos,speed=(0,10)):
        self.x, self.y = pos
        self.vx, self.vy = speed
        self.rect = Rect(self.x, self.y , rain_width, rain_height)

    def updatePos(self):
        self.x += self.vx
        self.y += self.vy
        self.rect = Rect(self.x, self.y , rain_width, rain_height)
        horiBorder = 1280
        verBorder = 720
        self.checkBorder(horiBorder,verBorder)
        
    def checkBorder(self, horiBorder,verBorder):
        if self.y >= verBorder:
            self.y = 0
            self.randomX()
        if self.x >= horiBorder:
            self.x = 0
        elif self.x <= 0:
            self.x = horiBorder

    def randomX(self):
        self.x = random.randint(0,1280)

    def render(self,surface):
        pygame.draw.rect(surface,(100,100,100),self.rect)

    def setVy(self,newVy):
        self.vx = newVy

    def setVx(self,newVx):
        self.vx = newVx

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
        self.y -= self.vy

    def move_down(self):
        self.y += self.vy

    def move_left(self):
        self.x -= self.vx

    def move_right(self):
        self.x += self.vx 

    def render(self,surface):
        pos = (int(self.x),int(self.y))
        self.ani.blit(surface, pos)