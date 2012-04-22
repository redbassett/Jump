#!/usr/bin/env python

from pygame import Rect, Surface
from pygame.sprite import Sprite, Group
from Block import *
from Lethal import Lethal
from win import *
import os

LEVEL_SIZE = (10000,10000)

#Thanks Alec!
class Level(object):
    def __init__(self, name):
        self.bounds = Rect((0,0,), LEVEL_SIZE)
        
        self.blocks = Group()
        self.lethal = Group()
        self.win = Group()

        self.loadData(name)

        self.spawnPoint = (20,20)
        
        self.render_background()
    
    def render_background(self):
        self.background = Surface(self.bounds.size)
        self.background.fill((0,0,0))
        self.blocks.draw(self.background)
        self.lethal.draw(self.background)
        self.win.draw(self.background)
        
    def loadData(self, name):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        DATA_DIR = os.path.join(ROOT_DIR, 'data')

        path = os.path.join(DATA_DIR, name) + '.lvl'
        with open(path, 'r') as f:
            data = f.read().strip().split('\n')

        width = 20
        height = 20
        for y, row in enumerate(data):
            for x,c in enumerate(row):
                loc = (x*width, y*height)
                
                if c == '.':
                    self.blocks.add(Block(loc))
                elif c == '!':
                    self.lethal.add(Lethal(loc))
                elif c == "^":
                    self.win.add(Win(loc))
