import pygame, sys, random
from pygame.locals import *

import gamelib
from elements import *


Rains = []

class BigHeavyPixel(gamelib.SimpleGame):
    windows_width = 1280
    windows_height = 720
    windows_size = (windows_width,windows_height)
    def __init__(self):
        super(BigHeavyPixel, self).__init__('BigHeavyPixel', (0,0,0),BigHeavyPixel.windows_size)
        self.player = Player(pos = (BigHeavyPixel.windows_width/2,BigHeavyPixel.windows_height/2))

    def init(self):
        super(BigHeavyPixel, self).init()

    def update(self):
        if len(Rains) < 20:
            Rains.append(Rain((random.randint(0, BigHeavyPixel.windows_width),(random.randint(0, BigHeavyPixel.windows_height)))))
        for rain in Rains:
            rain.updatePos()
            rain.setVy(10)
            rain.setVx(0)
            if rain.isCollide(self.player):
                print 'collide' 

        if self.is_key_pressed(K_UP):
            self.player.move_up()
        if self.is_key_pressed(K_DOWN):
            self.player.move_down()
        if self.is_key_pressed(K_LEFT):
            self.player.move_left()
        if self.is_key_pressed(K_RIGHT):
            self.player.move_right()

        if self.is_key_pressed(K_w):
            for rain in Rains:
                rain.setVy(5)
        if self.is_key_pressed(K_s):
            for rain in Rains:
                rain.setVy(15)
        if self.is_key_pressed(K_a):
            for rain in Rains:
                rain.setVx(2)
        if self.is_key_pressed(K_d):
            for rain in Rains:
                rain.setVx(-2)

    def render(self, surface):
        for i in Rains:
            i.render(self.surface)
        self.player.render(self.surface)

def main():
    game = BigHeavyPixel()
    game.run()

if __name__ == '__main__':
    main()