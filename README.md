# sudoku-solver
Python solver for sudoku puzzles

To use the raw sudoku solver, define the sudoku puzzle at the top of `sudoku/solver.py` and run it using `python sudoku/solver.py`. Missing numbers should be filled in as `0`'s.

You can also use it in a script by importing and calling `solve_sudoku` on an `np.matrix`:
```python
from sudoku.solver import solve_sudoku

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
solve_sudoku(sudoku)
print(sudoku)
```
This will print the solution as a matrix.

If you want to see the solution more like a "proper" sudoku, you can also use `plotter.plot_sudoku`:
```python
from sudoku.solver import solve_sudoku
from sudoku.plotter import plot_sudoku

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
solve_sudoku(sudoku)
plot_sudoku(sudoku)
```
![image](https://user-images.githubusercontent.com/13164166/146836989-825a2047-7b78-4b4f-b620-ef16e5f10a8e.png)
