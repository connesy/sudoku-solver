#!/usr/bin/env python

from itertools import product

import matplotlib.pyplot as plt


def plot_lines(ax):
    for i in range(10):
        color = "k" if i % 3 == 0 else [3 / 256, 165 / 256, 252 / 256]
        ax.vlines(x=i + 0.5, ymin=0.5, ymax=9.5, colors=color)
        ax.hlines(y=i + 0.5, xmin=0.5, xmax=9.5, colors=color)


def plot_sudoku(sudoku):
    fig, ax = plt.subplots()

    # Set axes equal and make the plot square
    ax.set_aspect("equal", "box")

    # Remove ticks and tick labels
    ax.set(xticks=[], xticklabels=[], yticks=[], yticklabels=[])

    # Remove axes
    ax.set_axis_off()

    # Plot horizontal and vertical sudoku lines
    plot_lines(ax)

    for y, x in product(range(9), range(9)):
        # Place annotations at coordinates 1-9
        ax.annotate(
            text=str(sudoku[y, x]),
            xy=(x + 1, 9 - y),
            horizontalalignment="center",
            verticalalignment="center",
        )

    plt.show()


if __name__ == "__main__":
    from solver import sudoku, solve_sudoku

    plot_sudoku(sudoku=sudoku)
    solve_sudoku(sudoku)
    plot_sudoku(sudoku=sudoku)
