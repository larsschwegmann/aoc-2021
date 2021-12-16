#!/usr/bin/env python3

# Parse input

from collections import Counter


with open("14/input.txt", "r") as fd:
    seq = list(fd.readline().rstrip())
    fd.readline()
    line = fd.readline().rstrip()
    instr = dict()
    while line:
        i = tuple([x for x in line.split(" -> ")])
        instr[i[0]] = i[1]
        line = fd.readline().rstrip()


# SImulate Polymer

print(seq)

for i in range(10):
    copy = list()
    for k in range(len(seq) - 2, -1, -1):
        pair = "".join(seq[k:k+2])
        copy.append(pair[1])
        if pair in instr.keys():
            copy.append(instr[pair])

    copy.append(seq[0])
    seq = list(reversed(copy))

# Count occurences

cnt = Counter(seq)
stats = cnt.most_common()
print(stats[0][1] - stats[-1][1])