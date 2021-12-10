#!/usr/bin/env python3

lines = []

with open("data.txt", "r") as fd:
    for line in fd:
        lines.append(int(line))


increase_count = 0
previous = None
for i in range(len(lines) - 2):
    window_sum = lines[i] + lines[i + 1] + lines[i + 2]
    if previous and previous < window_sum:
        increase_count += 1
    previous = window_sum

print(increase_count)
