#!/usr/bin/env python

from collections.abc import Iterator
from itertools import product

import numpy as np

BLOCK_SIZE = 3  # 2 is a 4x4 with 2x2 blocks, 3 is a 9x9 with 3x3 blocks
sudoku = np.matrix(
    [
        [0, 0, 9, 0, 2, 8, 0, 6, 7],
        [4, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [5, 0, 0, 7, 0, 0, 0, 2, 6],
        [0, 0, 6, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 2, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 1, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 7, 0, 8, 0],
    ]
)


def is_possible(sudoku: np.matrix, row: int, col: int, n: int) -> bool:
    if (sudoku[row, :] == n).any():
        return False

    if (sudoku[:, col] == n).any():
        return False

    row0 = (row // BLOCK_SIZE) * BLOCK_SIZE
    col0 = (col // BLOCK_SIZE) * BLOCK_SIZE
    if (sudoku[row0 : row0 + BLOCK_SIZE, col0 : col0 + BLOCK_SIZE] == n).any():
        return False

    return True


def solutions(
    sudoku: np.matrix, constrained: np.matrix, prior_position: tuple[int, int] = (0, -1)
) -> Iterator[np.matrix]:
    """All solutions to the input sudoku puzzle.

    The sudoku is solved by guessing a valid value for the first empty value, then recursively trying the rest of the sudoku,
    backtracking on dead ends. Every time a valid solution is found, it is yielded.

    N.B.: To avoid copying data each time a new recursion level is entered, the input sudoku is solved in-place.
    """
    for row, col in product(range(prior_position[0], BLOCK_SIZE**2), range(BLOCK_SIZE**2)):
        if constrained[row, col]:
            # Skip prior constrained positions, as these values are locked
            continue

        if row < prior_position[0] or (row == prior_position[0] and col <= prior_position[1]):
            # Skip all "lower" positions
            continue

        for n in range(1, BLOCK_SIZE**2 + 1):
            if not is_possible(sudoku, row=row, col=col, n=n):
                continue

            sudoku[row, col] = n

            if (sudoku != 0).all():
                # Yield the current solution, then reset current position
                yield sudoku.copy()
                sudoku[row, col] = 0
                return
            else:
                # Continue to search for solutions from next position
                yield from solutions(sudoku=sudoku, constrained=constrained, prior_position=(row, col))

        else:
            # Went through all 9 options, and there are no more solutions. Reset current position and go back one
            sudoku[row, col] = 0
            return


if __name__ == "__main__":
    all_solutions = []
    for i, solution in enumerate(solutions(sudoku=sudoku.copy(), constrained=sudoku != 0)):
        all_solutions.append(solution)
        print(i)
        print(solution)
