import pygame
from pygame.locals import *

import gamelib

class Rain(object):

	def __init__(self,pos,speed=(0,10)):
		self.x, self.y = pos
		self.vx, self.vy = speed
		self.rect = Rect(self.x, self.y , 50, 100)

	def updatePos(self):
		self.x += self.vx
		self.y += self.vy
		self.rect = Rect(self.x, self.y , 50, 100)
		self.checkBorder()
		
	def checkBorder(self):
		pass

	def render(self,surface):
		pos = (int(self.x),int(self.y))
		pygame.draw.rect(surface,(100,100,100),self.rect)



