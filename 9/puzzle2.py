#!/usr/bin/env python3

import math

# Parse input

heightmap = []
with open("9/input.txt", "r") as fd:
    for line in fd:
        heightmap.append([int(x) for x in line.rstrip()])

# Find lowpoints
lowpoints = []
for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        lowpoint = True
        if i > 0:
            # Check above
            if heightmap[i][j] >= heightmap[i - 1][j]:
                lowpoint = False
        
        if i < len(heightmap) - 1:
            # Check below
            if heightmap[i][j] >= heightmap[i + 1][j]:
                lowpoint = False

        if j > 0:
            # Check left
            if heightmap[i][j] >= heightmap[i][j - 1]:
                lowpoint = False

        if j < len(heightmap[i]) - 1:
            # Check right
            if heightmap[i][j] >= heightmap[i][j + 1]:
                lowpoint = False

        if lowpoint:
            print(f"Found lowpoint {(i, j)} with height {heightmap[i][j]}")
            lowpoints.append((i, j))

# Find basins

basins = []
for point in lowpoints:
    queue = list([point])
    basin = set()
    
    while len(queue) > 0:
        c = queue.pop(0)
        basin.add(c)

        # Check neighbours
        if c[0] > 0:
            # Check above
            if  heightmap[c[0] - 1][c[1]] < 9 and (c[0] - 1, c[1]) not in basin:
                queue.append((c[0] - 1, c[1]))
        
        if c[0] < len(heightmap) - 1:
            # Check below
            if heightmap[c[0] + 1][c[1]] < 9 and (c[0] + 1, c[1]) not in basin:
                queue.append((c[0] + 1, c[1]))

        if c[1] > 0:
            # Check left
            if heightmap[c[0]][c[1] - 1] < 9 and (c[0], c[1] - 1) not in basin:
                queue.append((c[0], c[1] - 1))

        if c[1] < len(heightmap[c[0]]) - 1:
            # Check right
            if heightmap[c[0]][c[1] + 1] < 9 and (c[0], c[1] + 1) not in basin:
                queue.append((c[0], c[1] + 1))

    basins.append(basin)

# Sort basins by size and multiply
basin_sizes_sorted = sorted([len(x) for x in basins], reverse=True)

# Print output
print(math.prod(basin_sizes_sorted[0:3]))