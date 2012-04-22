#!/usr/bin/env python

from Block import Block

"""
An abstract sort of block, kill splayer on contact.
"""
class Lethal(Block):
    def __init__(self, (x,y), color = (0,255,0), (w,h) = (20,20)):
        Block.__init__(self, (x,y), color, (w,h))
