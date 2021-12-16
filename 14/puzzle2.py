#!/usr/bin/env python3

# Parse input

with open("14/input.txt", "r") as fd:
    seq = list(fd.readline().rstrip())
    fd.readline()
    line = fd.readline().rstrip()
    instr = dict()
    while line:
        i = tuple([x for x in line.split(" -> ")])
        instr[i[0]] = i[1]
        line = fd.readline().rstrip()


# Simulate Polymer
# Count initial pairs
counts = dict()
for i, k in zip(seq, seq[1:]):
    pair = "".join([i, k])
    counts[pair] = counts.get(pair, 0) + 1

# Simulate pairwise counts
for i in range(40):
    copy = dict()
    for k, v in counts.items():
        if k in instr.keys():
            r = instr[k]
            copy[f"{k[0]}{r}"] = copy.get(f"{k[0]}{r}", 0) + v
            copy[f"{r}{k[1]}"] = copy.get(f"{r}{k[1]}", 0) + v
        
    counts = copy


# Count occurences of characters
element_count = dict()
for k, v in counts.items():
    for c in k:
        element_count[c] = element_count.get(c, 0) + v

element_count[seq[0]] += 1
element_count[seq[-1]] += 1

max_e = int(max(element_count.values()) / 2)
min_e = int(min(element_count.values()) / 2)
print(max_e - min_e)