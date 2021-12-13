#!/usr/bin/env python3

from pprint import pprint

# Parse input

paths = []
with open("12/input.txt", "r") as fd:
    for line in fd:
        paths.append((line.rstrip().split("-")[0], line.rstrip().split("-")[1]))

# populate adjacency lists

adjacency = dict()
for p in paths:
    if p[0] not in adjacency.keys():
        adjacency[p[0]] = [p[1]]
    else:
        adjacency[p[0]].append(p[1])

    if p[1] not in adjacency.keys():
        adjacency[p[1]] = [p[0]]
    else:
        adjacency[p[1]].append(p[0])

print("Adjacency lists:")
pprint(adjacency)

def traverse(current, visited) -> int:
    if current == "end":
        return 1

    new_visited = set(visited)
    if current.islower():
        new_visited.add(current)

    count = 0

    for n in adjacency[current]:
        if n.isupper() or n not in new_visited:
            count += traverse(n, new_visited)

    return count

print(traverse("start", set()))
