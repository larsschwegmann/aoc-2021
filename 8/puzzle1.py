#!/usr/bin/env python3

out_segments = []
with open("8/input.txt", "r") as fd:
    for line in fd:
        out_segments.extend(line.rstrip().split(" | ")[1].split(" "))
    

unique_count = 0
for seg in out_segments:
    unique_count += 1 if len(seg) in [2, 4, 3, 7] else 0

print(unique_count)