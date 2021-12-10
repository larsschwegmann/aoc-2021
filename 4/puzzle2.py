#!/usr/bin/env python3

from pprint import pprint
import sys
from typing import Tuple, List, Set

# Parse input

draw_order = []
boards_raw = []

with open("4/input.txt", "r") as fd:
    draw_order = [int(x) for x in fd.readline().rstrip().split(",")]
    fd.readline()

    board_index = 0
    board_line = 0
    boards_raw.append([])

    while fd:
        line = fd.readline()
        if line == "":
            break

        if line == "\n":
            board_index += 1
            board_line = 0
            boards_raw.append([])
            continue


        boards_raw[board_index].append([int(x.strip()) for x in line.split(" ") if x != ""])
        board_line += 1

print(f"Input Sequence: {draw_order}")
print("Input Boards:")
pprint(boards_raw)

# Determine winning board

# Board helper class:

class Board:
    _raw_board: List[List[int]]

    def __init__(self, raw_board: List[List[int]]):
        self._raw_board = raw_board
        pass

    def steps_to_win(self, seq: List[int]) -> Tuple:
        marks = set()

        # Loop though input sequence
        for i in range(len(seq)):
            draw = seq[i]
            pos = (-1, -1)
            # Loop though board rows
            for j in range(len(self._raw_board)):
                # Loop though board columns
                for k in range(len(self._raw_board[j])):
                    if self._raw_board[j][k] == draw:
                        pos = (j, k)
                        break
                else:
                    continue

                break
            else:
                # Loop completed without breaking, number not found
                # Continue input sequence loop
                continue

            # At this point, we have found the current input i in our board
            # Position of i is in pos

            # Mark position
            marks.add(pos)

            # Check if we have completed a horizontal or vertical line
            # Horizontal
            horizontal = True
            for j in range(5):
                if not (pos[0], j) in marks:
                    horizontal = False
                    break

            if horizontal:
                return (i, marks)

            # Vertical
            vertical = True
            for j in range(5):
                if not (j, pos[1]) in marks:
                    vertical = False
                    break

            if vertical:
                return (i, marks)



        return (-1, None)

    def score(self, marked: Set[Tuple[int, int]], last_called: int) -> int:
        all = set()
        for i in range(5):
            for j in range(5):
                all.add((i, j))
        
        not_marked = all - marked
        
        unmarked_sum = sum([self._raw_board[pos[0]][pos[1]] for pos in not_marked])
        return unmarked_sum * last_called



boards = [Board(raw_board=x) for x in boards_raw]
board_winning_steps = [b.steps_to_win(draw_order) for b in boards]

# Find board with maximum steps to win
max_index = -1
max = -1
for b in range(len(board_winning_steps)):
    if board_winning_steps[b][0] > max:
        max_index = b
        max = board_winning_steps[b][0]


winning_board = boards[max_index]
winning_steps = board_winning_steps[max_index]

winning_score = winning_board.score(winning_steps[1], draw_order[winning_steps[0]])

print("Score:")
print(winning_score)
