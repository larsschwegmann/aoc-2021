#!/usr/bin/env python3

from pprint import pprint
import numpy as np
from functools import reduce

lines = list()

# Read input
with open("5/input.txt") as fd:
    for line in fd:
        [c1, c2] = line.rstrip().split(" -> ")
        c1t = tuple([int(x) for x in c1.split(",")])
        c2t = tuple([int(x) for x in c2.split(",")])
        lines.append((c1t, c2t))

# Filter horizontal/vertical
lines = [c for c in lines if c[0][0] == c[1][0] or c[0][1] == c[1][1]]

print("Line coordinates")
pprint(lines)

hits = dict()

for l in lines:
    a, b = l
    pos = np.array(a)
    heading = np.subtract(b, a)
    norm = np.linalg.norm(heading)
    if norm != 0:
        heading = heading / norm

    key = tuple(pos)
    hits[key] = hits.get(key, 0) + 1
    while not np.array_equal(pos, np.array(b)):
        pos = np.add(pos, heading).astype(int)
        key = tuple(pos)
        hits[key] = hits.get(key, 0) + 1

intersections = reduce(lambda x, y: x + 1 if y >= 2 else x, hits.values(), 0)

print("Intersections:")
print(intersections)