#!/usr/bin/env python3

# Parse input

fish = []

with open("6/input.txt", "r") as fd:
    fish = [int(x) for x in fd.readline().rstrip().split(",")]

population = dict()
for f in fish:
    population[f] = population.get(f, 0) + 1

# simulate fish

for i in range(256):
    reset_fish = 0
    for j in range(9):
        fish_count = population.get(j, 0)
        if j in population.keys():
            del population[j];

        if j == 0:
            reset_fish = fish_count
        else:
            population[j - 1] = fish_count

    population[6] = population.get(6, 0) + reset_fish
    population[8] = reset_fish

# print fish count

print("Fish count")
fish_count = 0
for f in population.values():
    fish_count += f
print(fish_count)