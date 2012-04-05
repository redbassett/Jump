#!/usr/bin/env python

"""
A block is a solid (static) piece of the world, such as a wall, floor, spike, or goal.
"""
class Block(Point):
    def __init__(self, loc):
        self.loc = loc
    
    @overload
    def __init__(self, x, y):
        self.loc = (x, y)
    
    
