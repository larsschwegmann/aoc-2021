#!/usr/bin/env python3

gamma_rate = 0x0
epsilon_rate = 0x0

width = 0
data = []

# Parse input
with open("3/data.txt", "r") as fd:
    for line in fd:
        width = len(line.rstrip())
        data.append(int(line, 2))
    

for bitpos in range(width):
    counter = 0
    for i in range(len(data)):
        if data[i] & (0x1 << bitpos) > 0:
            # Bit at bitpos is set
            counter += 1

        if counter > len(data) / 2:
            break

    if counter > len(data) / 2:
        gamma_rate = gamma_rate | 0x1 << bitpos

mask = pow(2, width) - 1
epsilon_rate = ~gamma_rate & mask

print(epsilon_rate * gamma_rate)