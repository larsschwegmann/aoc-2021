#!/usr/bin/env python3

previous = None
increase_count = 0
with open("data.txt", "r") as fd:
    for line in fd:
        intval = int(line)

        if previous:
            if previous < intval:
                increase_count += 1
            
        previous = intval

    print(increase_count)