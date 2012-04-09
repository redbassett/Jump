#!/usr/bin/env python

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")

name = 'slicelevel'

path = os.path.join(DATA_DIR, name) + '.lvl'
with open(path, 'r') as f:
    data = f.read().strip().split('\n')

#data = [[self._map.get(c) for c in row] for row in data]

blocks = []
lethals = []

rowNum = 0
for row in data:
    cNum = 0
    for  c in row:
        if c == '.':
            blocks.append((cNum,rowNum))
        elif c == '!':
            lethals.append((cNum,rowNum))
        cNum += 20
    rowNum += 20

print blocks
print lethals
