#!/usr/bin/env python3

from queue import PriorityQueue
import sys
import heapq as pq

# Parse input

with open("15/input.txt", "r") as fd:
    map = list()
    for line in fd:
        map.append([int(x) for x in line.rstrip()])


# Pathfinding with djikstra (ugly code ahead, quick and dirtys)

queue = []
dist = dict()
dist[(0, 0)] = 0
prev = dict()
goal = (len(map) - 1, len(map) - 1)

for i in range(len(map)):
    for j in range(len(map)):
        pq.heappush(queue, (dist.get((i, j), sys.maxsize), (i, j)))

while len(queue) > 0:
    v = pq.heappop(queue)[1]
    # Check top
    if v[0] > 0:
        w = (v[0] - 1, v[1])
        if dist.get(v, sys.maxsize) + map[w[0]][w[1]] < dist.get(w, sys.maxsize):
            dist[w] = dist.get(v, sys.maxsize) + map[w[0]][w[1]]
            pq.heappush(queue, (dist[w], w))
            prev[w] = v
    # Check Left
    if v[1] > 0:
        w = (v[0], v[1] - 1)
        if dist.get(v, sys.maxsize) + map[w[0]][w[1]] < dist.get(w, sys.maxsize):
            dist[w] = dist.get(v, sys.maxsize) + map[w[0]][w[1]]
            pq.heappush(queue, (dist[w], w))
            prev[w] = v

    # Bottom
    if v[0] < len(map) - 1:
        w = (v[0] + 1, v[1])
        if dist.get(v, sys.maxsize) + map[w[0]][w[1]] < dist.get(w, sys.maxsize):
            dist[w] = dist.get(v, sys.maxsize) + map[w[0]][w[1]]
            pq.heappush(queue, (dist[w], w))
            prev[w] = v

    # Right
    if v[1] < len(map) - 1:
        w = (v[0], v[1] + 1)
        if dist.get(v, sys.maxsize) + map[w[0]][w[1]] < dist.get(w, sys.maxsize):
            dist[w] = dist.get(v, sys.maxsize) + map[w[0]][w[1]]
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

print(sum([map[v[0]][v[1]] for v in path]))


