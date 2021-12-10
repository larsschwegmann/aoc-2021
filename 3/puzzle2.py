#!/usr/bin/env python3

oxygen_rating = 0
c02_rating = 0

width = 0
data = []

# Parse input
with open("3/data.txt", "r") as fd:
    for line in fd:
        width = len(line.rstrip())
        data.append(int(line, 2))
    
# oxygen rating

oxy_candidates = set(data)
for bitpos in range(width - 1, -1, -1):
    even = set()
    odd = set()
    for c in oxy_candidates:
        if c & (0x1 << bitpos):
            odd.add(c)
        else:
            even.add(c)

    if len(odd) > len(even):
        oxy_candidates = odd
    elif len(even) > len(odd):
        oxy_candidates = even
    elif len(odd) == len(even):
        oxy_candidates = odd

    if len(oxy_candidates) == 1:
        break

assert(len(oxy_candidates) == 1)
oxygen_rating = oxy_candidates.pop()

# c02 rating
c02_candidates = set(data)
for bitpos in range(width - 1, -1, -1):
    even = set()
    odd = set()
    for c in c02_candidates:
        if c & (0x1 << bitpos):
            odd.add(c)
        else:
            even.add(c)

    if len(odd) > len(even):
        c02_candidates = even
    elif len(even) > len(odd):
        c02_candidates = odd
    elif len(odd) == len(even):
        c02_candidates = even

    if len(c02_candidates) == 1:
        break

assert(len(c02_candidates) == 1)
c02_rating = c02_candidates.pop()

print(oxygen_rating * c02_rating)