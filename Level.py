#!/usr/bin/env python

from pygame import Rect, Surface
from pygame.sprite import Sprite, Group
from Block import *
from Lethal import Lethal

LEVEL_SIZE = (800,600)

#Thanks Alec!
class Level(object):
    def __init__(self):
        self.bounds = Rect((0,0,), LEVEL_SIZE)
        
        self.blocks = Group(
            Block((0,0)),
            Block((0,20)),
            Block((0,40)),
            Block((0,60)),
            Block((0,80)),
            Block((0,100)),
            Block((0,120)),
            Block((0,140)),
            Block((0,160)),
            Block((0,180)),
            Block((0,200)),
            Block((0,220)),
            Block((0,240)),
            Block((0,260)),
            Block((0,300)),
            Block((0,600)),
            Lethal((20,600)),
            Block((40,600)),
            Block((60,600)),
            Block((80,600)),
            Block((100,600)),
            Block((20,300))
        )
        
        self.spawnPoint = (20,20)
        
        self.render_background()
    
    def render_background(self):
        self.background = Surface(self.bounds.size)
        self.background.fill((0,0,0))
        self.blocks.draw(self.background)
