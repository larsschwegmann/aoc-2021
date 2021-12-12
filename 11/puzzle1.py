#!/usr/bin/env python3

from pprint import pprint

# Parse input

with open("11/input.txt", "r") as fd:
    grid = [[int(x) for x in line.rstrip()] for line in fd]

pprint(grid)

# Simulate

def get_adjacent_coordinates(c, grid_size):
    adjacent = list()
    # Top
    if c[0] > 0:
        # Top Left
        if c[1] > 0:
            adjacent.append((c[0] - 1, c[1] - 1))
        
        # Top
        adjacent.append((c[0] - 1, c[1]))

        # Top Right
        if c[1] < grid_size - 1:
            adjacent.append((c[0] - 1, c[1] + 1))

    # Left
    if c[1] > 0:
        adjacent.append((c[0], c[1] - 1))

    # Right
    if c[1] < grid_size - 1:
        adjacent.append((c[0], c[1] + 1))

    # Bottom
    if c[0] < grid_size - 1:
        # Bottom Left
        if c[1] > 0:
            adjacent.append((c[0] + 1, c[1] - 1))
        
        # Bottom
        adjacent.append((c[0] + 1, c[1]))

        if c[1] < grid_size - 1:
            adjacent.append((c[0] + 1, c[1] + 1))

    return adjacent

flash_count = 0

for i in range(100):
    # Increase all energy levels by one
    will_flash = set()
    for y in range(len(grid)):
        for x in range(len(grid)):
            grid[y][x] += 1
            if grid[y][x] > 9:
                will_flash.add((y, x))

    # Simulate flash chain reaction
    has_flashed = set()
    while len(will_flash) > 0:
        o = will_flash.pop()

        # o only flashes if o hasnt flashed in this iteration and energy is > 9
        if o in has_flashed:
            continue

        if grid[o[0]][o[1]] <= 9:
            continue

        # Make o flash and set as flashed
        has_flashed.add(o)
        grid[o[0]][o[1]] = 0
        flash_count += 1

        # Increase surrounding octopus energy levels
        for c in get_adjacent_coordinates(o, len(grid)):
            if c not in has_flashed:
                grid[c[0]][c[1]] += 1
            
                if grid[c[0]][c[1]] > 9:
                    will_flash.add(c)

print(flash_count)