#!/usr/bin/env python
import pygame
from pygame.locals import *
from pygame.sprite import Sprite
"""
A block is a solid (static) piece of the world, such as a wall, floor, spike, or goal.
"""
class Block(Sprite):
        def __init__(self, (x,y), color = (255,0,0), (w,h) = (20,20)):
            Sprite.__init__(self)
            self.x, self.y = (x, y)
            
            self.image = pygame.Surface((w,h))
            self.rect = self.image.get_rect()
            self.rect.topleft = x,y
            
            self.image.fill(color)
