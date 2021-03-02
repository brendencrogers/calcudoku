"""Calcudoku functions tests
CPE 101
Spring 2020
Author: Brenden Rogers
"""

import calcudoku

cages_1 = [[4, 3, 0, 1, 6], [8, 3, 2, 7, 12], [14, 3, 3, 4, 8],
           [15, 4, 5, 10, 11, 15], [14, 6, 9, 13, 14, 18, 19, 24],
           [11, 3, 16, 20, 21], [9, 3, 17, 22, 23]]
cages_2 = [[7, 3, 0, 1, 2], [12, 4, 3, 4, 8, 9], [17, 6, 5, 7, 10, 11, 12, 13],
           [5, 1, 6], [11, 3, 14, 19, 24], [7, 2, 15, 20], [5, 3, 16, 17, 21], [11, 3, 18, 22, 23]]
grid_val = [[1, 2, 3, 4, 5], [3, 1, 4, 5, 2], [2, 5, 1, 3, 4], [5, 4, 2, 1, 3], [4, 3, 5, 2, 1]]
grid_non = [[1, 5, 3, 4, 5], [1, 1, 4, 5, 2], [2, 4, 1, 3, 4], [5, 5, 2, 3, 3], [4, 3, 6, 2, 1]]
grid_non_2 = [[1, 4, 3, 4, 5], [2, 1, 2, 5, 2], [2, 5, 1, 3, 1], [5, 3, 2, 1, 3], [4, 4, 5, 2, 4]]

assert calcudoku.validate_all(grid_val, cages_1) is True
assert calcudoku.validate_all(grid_val, cages_2) is False
assert calcudoku.validate_all(grid_non, cages_1) is False

assert calcudoku.validate_rows(grid_val) is True
assert calcudoku.validate_rows(grid_non) is False
assert calcudoku.validate_rows(grid_non_2) is False

assert calcudoku.validate_cols(grid_val) is True
assert calcudoku.validate_cols(grid_non) is False
assert calcudoku.validate_cols(grid_non_2) is False

assert calcudoku.validate_cages(grid_val, cages_1) is True
assert calcudoku.validate_cages(grid_non, cages_1) is False
assert calcudoku.validate_cages(grid_val, cages_2) is False
