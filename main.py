import pygame, sys, random
from pygame.locals import *

import gamelib
from elements import *

class BigHeavyPixel(gamelib.SimpleGame):
    windows_width = 1280
    windows_height = 720
    windows_size = (windows_width,windows_height)
    def __init__(self):
        super(BigHeavyPixel, self).__init__('BigHeavyPixel', (0,0,0),BigHeavyPixel.windows_size)
        self.blackcat = Rain(pos = (50,50),speed = (0,10))
        self.player = Player(pos = (50,50))

    def init(self):
        super(BigHeavyPixel, self).init()

    def update(self):
        self.blackcat.updatePos(self.surface)

    def render(self, surface):
        self.blackcat.render(self.surface)
        self.player.render(self.surface)

def main():
    game = BigHeavyPixel()
    game.run()

if __name__ == '__main__':
    main()