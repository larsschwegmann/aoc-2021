#!/usr/bin/env python3

# Parse input

lines = []
with open("10/input.txt", "r") as fd:
    for line in fd:
        lines.append(line.rstrip())

illegal = []
for line in lines:
    stack = list()
    for c in line:
        if c == "(":
            stack.append(")")
        elif c == "[":
            stack.append("]")
        elif c == "{":
            stack.append("}")
        elif c == "<":
            stack.append(">")
        else:
            # Closing
            if len(stack) == 0:
                illegal.append(c)
                break

            expected = stack.pop()
            if c != expected:
                illegal.append(c)
                break

mapping = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

print(sum([mapping[x] for x in illegal]))