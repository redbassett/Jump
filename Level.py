#!/usr/bin/env python

from pygame import Rect, Surface
from pygame.sprite import Sprite, Group
from Block import *
from Lethal import Lethal
import os

LEVEL_SIZE = (10000,10000)

#Thanks Alec!
class Level(object):
    def __init__(self, name):
        self.bounds = Rect((0,0,), LEVEL_SIZE)
        
        self.blocks = Group()
        self.loadData(name)

        self.spawnPoint = (20,20)
        
        self.render_background()
    
    def render_background(self):
        self.background = Surface(self.bounds.size)
        self.background.fill((0,0,0))
        self.blocks.draw(self.background)
        
    def loadData(self, name):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        DATA_DIR = os.path.join(ROOT_DIR, 'data')

        path = os.path.join(DATA_DIR, name) + '.lvl'
        with open(path, 'r') as f:
            data = f.read().strip().split('\n')

        width = 20
        height = 20
        rowNum = 0
        for row in data:
            cNum = 0
            for c in row:
                loc = (cNum*width,rowNum*height)
                if c == '.':
                    self.blocks.add(Block(loc))
                elif c == '!':
                    self.blocks.add(Lethal(loc))
                cNum += 1
            rowNum += 1
