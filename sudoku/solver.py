#!/usr/bin/env python

import numpy as np
from itertools import product


num_tries = 0
sudoku = np.matrix(
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
)


def check_if_possible(sudoku: np.matrix, x: int, y: int, n: int):
    global num_tries
    num_tries += 1
    # print(f"Trying {y = }, {x = }, {n = }")

    if (sudoku[:, x] == n).any():
        return False

    if (sudoku[y, :] == n).any():
        return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    if (sudoku[y0 : y0 + 3, x0 : x0 + 3] == n).any():
        return False

    return True


def solve_sudoku(sudoku: np.matrix):
    """Solve the input sudoku puzzle recursively by guessing a number and then trying to solve the remaining puzzle.

    N.B.: To avoid copying data each time a new recursion level is entered, the input sudoku is solved in-place.
    """
    for y, x in product(range(9), range(9)):
        if sudoku[y, x] != 0:
            # Number already placed
            continue

        for n in range(1, 10):
            if check_if_possible(sudoku, x=x, y=y, n=n):
                # Try solving sudoku, now with `n` at position [y, x]
                sudoku[y, x] = n
                solved = solve_sudoku(sudoku)

                if solved:
                    # If the sudoku is solved, return True
                    return True

                # If the sudoku was not solved, reset the number at [y, x]
                sudoku[y, x] = 0
        else:
            # If there are no more options to try at the position, it's because an earlier number is wrong.
            # Return False
            return False

    # When all x and y are exhausted, the sudoku has been solved
    return True


if __name__ == "__main__":
    solved = solve_sudoku(sudoku)
    print()
    print(sudoku)
    print()
    print(num_tries)
