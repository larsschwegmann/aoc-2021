#!/usr/bin/env python3

import sys

crabs = []
with open("7/input.txt", "r") as fd:
    crabs = [int(x) for x in fd.readline().rstrip().split(",")]


def cost(crab_positions, designated_position):
    costs = 0
    for pos in crab_positions:
        costs += abs(pos - designated_position)

    return costs

min_cost = sys.maxsize
min_i = -1
for i in range(max(crabs)):
    c = cost(crabs, i)
    if c < min_cost:
        min_cost = c
        min_i = i

print(f"Position: {min_i}")
print("Total Fuel:")
print(min_cost)
