#!/usr/bin/env python3

from queue import PriorityQueue
import sys
import heapq as pq

# Parse input

with open("15/input.txt", "r") as fd:
    map = dict()
    orig_mapsize  = 0
    for y, line in enumerate(fd):
        orig_mapsize += 1
        for x, c in enumerate(line.rstrip()):
            map[(x, y)] = int(c)

mapsize = orig_mapsize * 5

# Generate full map
for x in range(0, mapsize):
    for y in range(0, mapsize):
        if x < orig_mapsize and y < orig_mapsize:
            continue
        tile = (int(x / orig_mapsize), int(y / orig_mapsize))
        orig_coord = (x % orig_mapsize, y % orig_mapsize)
        map[(x, y)] = map[orig_coord] + tile[0] + tile[1]
        if map[(x, y)] > 9:
            map[(x, y)] -= 9


# Pathfinding with djikstra (ugly code ahead, quick and dirtys)

queue = []
dist = dict()
dist[(0, 0)] = 0
prev = dict()
goal = (mapsize - 1, mapsize - 1)

for x in range(mapsize):
    for y in range(mapsize):
        pq.heappush(queue, (dist.get((x, y), sys.maxsize), (x, y)))

while len(queue) > 0:
    v = pq.heappop(queue)[1]
    # Check top
    if v[0] > 0:
        w = (v[0] - 1, v[1])
        if dist.get(v, sys.maxsize) + map[w] < dist.get(w, sys.maxsize):
            dist[w] = dist.get(v, sys.maxsize) + map[w]
            pq.heappush(queue, (dist[w], w))
            prev[w] = v
    # Check Left
    if v[1] > 0:
        w = (v[0], v[1] - 1)
        if dist.get(v, sys.maxsize) + map[w] < dist.get(w, sys.maxsize):
            dist[w] = dist.get(v, sys.maxsize) + map[w]
            pq.heappush(queue, (dist[w], w))
            prev[w] = v

    # Bottom
    if v[0] < mapsize - 1:
        w = (v[0] + 1, v[1])
        if dist.get(v, sys.maxsize) + map[w] < dist.get(w, sys.maxsize):
            dist[w] = dist.get(v, sys.maxsize) + map[w]
            pq.heappush(queue, (dist[w], w))
            prev[w] = v

    # Right
    if v[1] < mapsize - 1:
        w = (v[0], v[1] + 1)
        if dist.get(v, sys.maxsize) + map[w] < dist.get(w, sys.maxsize):
            dist[w] = dist.get(v, sys.maxsize) + map[w]
            pq.heappush(queue, (dist[w], w))
            prev[w] = v

# Get shortest path

path = list()
done = False
current = goal
while True:
    path.append(current)
    current = prev[current]
    if current == (0, 0):
        break

# Print path costs

print(sum([map[v] for v in path]))


