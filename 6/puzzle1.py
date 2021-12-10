#!/usr/bin/env python3

# Parse input

fish = []

with open("6/input.txt", "r") as fd:
    fish = [int(x) for x in fd.readline().rstrip().split(",")]

# simulate fish

for i in range(80):
    for f in range(len(fish)):
        timer = fish[f]
        timer -= 1

        if timer < 0:
            timer = 6
            fish.append(8)

        fish[f] = timer

# print fish count

print("Fish count")
print(len(fish))