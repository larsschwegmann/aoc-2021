#!/usr/bin/env python3

# Digit -> segment count mapping
#
# 0 -> 6   abc efg
# 1 -> 2     c  f     <- Unique
# 2 -> 5   a cde g
# 3 -> 5   a cd fg
# 4 -> 4    bcd f     <- Unique
# 5 -> 5   ab d fg
# 6 -> 6   ab defg
# 7 -> 3   a c  f     <- Unique
# 8 -> 7   abcdefg    <- Unique
# 9 -> 6   abcd fg

# Parse input

input_segments = []
output_segments = []

with open("8/input.txt", "r") as fd:
    for line in fd:
        input_segments.append(line.rstrip().split(" | ")[0].split(" "))
        output_segments.append(line.rstrip().split(" | ")[1].split(" "))

# Calculate output values by deduction
output_values = []
for i in range(len(input_segments)):
    searchspace = [set(x) for x in input_segments[i] + output_segments[i]]
    digits = dict()
    digits[1] = next((x for x in searchspace if len(x) == 2), None)
    digits[4] = next((x for x in searchspace if len(x) == 4), None)
    digits[7] = next((x for x in searchspace if len(x) == 3), None)
    digits[8] = next((x for x in searchspace if len(x) == 7), None)
    # 5 digits
    digits[3] = next((x for x in searchspace if len(x) == 5 and digits[1].issubset(x)), None)
    four_edge = digits[4] - digits[1]
    digits[5] = next((x for x in searchspace if len(x) == 5 and four_edge.issubset(x)), None)
    digits[2] = next((x for x in searchspace if len(x) == 5 and x != digits[3] and x != digits[5]), None)
    # 6 digits
    digits[9] = next((x for x in searchspace if len(x) == 6 and digits[1].issubset(x) and four_edge.issubset(x)), None)
    digits[0] = next((x for x in searchspace if len(x) == 6 and digits[1].issubset(x) and not four_edge.issubset(x)), None)
    digits[6] = next((x for x in searchspace if len(x) == 6 and x != digits[9] and x != digits[0]), None)

    reversed = dict()
    for key, value in digits.items():
        reversed[frozenset(value)] = key

    order = 1000
    output = 0
    for x in output_segments[i]:
        output += order * reversed[frozenset(x)]
        order = int(order / 10)

    print(f"Line {i} Output: {output}")
    output_values.append(output)


# Sum the outputs and print
print("Result:")
print(sum(output_values))
