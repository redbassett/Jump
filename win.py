#!/usr/bin/env python

from Block import Block
"""
Winner
"""

class Win(Block):
    def __init__(self, (x,y), color = (218, 112, 214), (w, h) = (20, 20)):
        Block.__init__(self, (x,y), color, (w, h))
