import pygame, sys, random
from pygame.locals import *

import gamelib
from elements import Rain

class BigHeavyPixel(gamelib.SimpleGame):

    def __init__(self):
        super(BigHeavyPixel, self).__init__('BigHeavyPixel', (0,0,0))
        self.blackcat = Rain(pos = (50,50))

    def init(self):
        super(BigHeavyPixel, self).init()

    def update(self):
        self.blackcat.updatePos()

    def render(self, surface):
        self.blackcat.render(surface)

def main():
    game = BigHeavyPixel()
    game.run()

if __name__ == '__main__':
    main()