#!/usr/bin/env python3

# Parse input

heightmap = []
with open("9/input.txt", "r") as fd:
    for line in fd:
        heightmap.append([int(x) for x in line.rstrip()])

# Find lowpoints
risk_levels = []
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
            risk_levels.append(heightmap[i][j] + 1)

# Print output
print(sum(risk_levels))