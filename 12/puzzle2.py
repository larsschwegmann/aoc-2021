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


# Recursive DFS
def traverse(current, visited, current_path, visited_twice=None) -> int:
    if current == "end":
        return 1

    count = 0
    for n in adjacency[current]:
        if n == "start":
            continue  

        if n.isupper() or n not in visited or (n in visited and visited_twice is None):
            new_path = list(current_path)
            new_path.append(n)  

            new_visited = set(visited)

            if current.islower():
                new_visited.add(current)
            if n in visited:
                count += traverse(n, new_visited, new_path, visited_twice=n)
            else:
                count += traverse(n, new_visited, new_path, visited_twice=visited_twice)

    return count

print(traverse("start", set(), ["start"]))
