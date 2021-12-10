#!/usr/bin/env python3

h_pos = 0
depth = 0

with open("input.txt", "r") as fd:
    for line in fd:
        [instr, arg] = line.split(" ")
        
        if instr == "forward":
            h_pos += int(arg)
        elif instr == "up":
            depth -= int(arg)
        elif instr == "down":
            depth += int(arg)

print(h_pos * depth)