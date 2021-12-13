#!/usr/bin/env python3

# Parse input

points = set()
fold_instr = list()

with open("13/input.txt", "r") as fd:
    past_points = False
    for line in fd:
        if line == "\n":
            past_points = True
            continue
    
        if not past_points:
            points.add(tuple(int(x) for x in line.rstrip().split(",")))
        else:
            [axis, value] = line.lstrip("fold along ").split("=")
            fold_instr.append((axis, int(value)))

# Follow fold instructions

def debug_points():
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)

    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            if (x, y) not in points:
                line = line + "."
            else:
                line = line + "#"
        
        print(line)

    print()
        
print("Initial points:")
debug_points()

for i in fold_instr[:1]:
    a = 0 if i[0] == "x" else 1 # axis index
    updated_points = set()

    for p in points:
        if p[a] > i[1]:
            # Fold point
            diff = p[a] - i[1]
            if i[0] == "x":
                p_star = (p[0] - 2 * diff, p[1])
            else:
                p_star = (p[0], p[1] - 2 * diff)

            updated_points.add(p_star)
        else:
            updated_points.add(p)
        
    points = updated_points
    print(f"Points after folding {i}:")
    debug_points()


# Print amount of points left

print(len(points))