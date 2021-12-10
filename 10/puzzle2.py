#!/usr/bin/env python3

# Parse input

lines = []
with open("10/input.txt", "r") as fd:
    for line in fd:
        lines.append(line.rstrip())

# Check lines

line_completions = []
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
                break

            expected = stack.pop()
            if c != expected:
                break
    else:
        if len(stack) > 0:
            line_completions.append(reversed(stack))


# Calculate score

mapping = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

scores = []

for line in line_completions:
    score = 0
    for c in line:
        score *= 5
        score += mapping[c]

    scores.append(score)


# Print score

print(sorted(scores, reverse=True)[int(len(scores)/2)])