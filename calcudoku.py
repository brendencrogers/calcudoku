"""Calcudoku Project 2
CPE 101
Spring 2020
Author: Brenden Rogers
"""


def main():
    """To solve Calcudoku puzzle"""
    cage_num = get_num_cages()
    cages = get_cage_info(cage_num)
    grid = create_grid()
    i = 0
    j = 0
    while i < 5:
        grid[i][j] += 1
        if validate_all(grid, cages) is True and grid[i][j] < 6:
            if j == 4:
                j = 0
                i += 1
            else:
                j += 1
        else:
            if grid[i][j] > 5:
                grid[i][j] = 0
                if j == 0:
                    j = 4
                    i -= 1
                else:
                    j -= 1
    string = ''
    for a in grid:
        for b in a:
            string += str(b)
            string += ' '
        string = string.strip()
        print(string)
        string = ''


def get_num_cages():
    """Asks user to set number of cages

    Returns:
        int: number of cages
    """
    while True:
        cage_num = input()
        if cage_num.isdigit():
            return cage_num


def get_cage_info(num):
    """Returns list of lists after user enters info

    Args:
        num (int): number of lists/cages

    Returns:
        list: list of lists
    """
    i = 0
    num = int(num)
    blank = []
    while i < num:
        lst = input()
        lst_num = lst.split(' ')
        lst_num = [int(n) for n in lst_num]
        blank.append(lst_num)
        i += 1
    return blank


def validate_all(grid, cages):
    """Returns True if all 3 validation functions are True

    Args:
        grid (list): list of lists
        cages (list): list of ints

    Returns:
        bool: True if all functions True, False if else
    """
    rows = validate_rows(grid)
    cols = validate_cols(grid)
    cages = validate_cages(grid, cages)
    if rows and cols and cages is True:
        return True
    return False


def validate_rows(grid):
    """Returns True if all rows contain no duplicates

    Args:
        grid (list): list of lists

    Returns:
        bool: True if all rows contain no duplicates, false if else
    """
    i = 0
    blank = []
    while i < len(grid):
        row = grid[i]
        for n in row:
            if row.count(n) > 1 and n != 0:
                blank.append(n)
        if len(blank) > 0:
            return False
        i += 1
    return True


def validate_cols(grid):
    """Transposes columns to rows and checks validate_rows

    Args:
        grid (list): list of lists

    Returns:
        bool: True if no duplicates, False if else
    """
    grid_new = transpose_grid(grid)
    return validate_rows(grid_new)


def validate_cages(grid, cages):
    """Return True if sum in cage is correct, or sum in partial cage is less than sum final

    Args:
        grid (list): list of lists
        cages (list): list of lists

    Returns:
        bool: True if sum correct, false if else
    """
    grid_val = []
    empty = False
    valid = True
    sum = 0
    for i in cages:
        for j in i[2:]:
            value = grid[j // 5][j % 5]
            grid_val.append(value)
        for num in grid_val:
            if num == 0:
                empty = True
            sum += num
        grid_val = []
        if empty is False:
            if sum != i[0]:
                valid = False
        elif empty is True:
            if sum >= i[0]:
                valid = False
        sum = 0
        empty = False
    return valid


def transpose_grid(grid):
    """Turns rows to cols and cols to rows in list of lists

    Args:
        grid (list): list of lists

    Returns:
        list: transposed list of lists
    """
    i = 0
    blank_0 = []
    blank_1 = []
    blank_2 = []
    blank_3 = []
    blank_4 = []
    while i < len(grid):
        rows_0 = grid[i][0]
        blank_0.append(rows_0)
        rows_1 = grid[i][1]
        blank_1.append(rows_1)
        rows_2 = grid[i][2]
        blank_2.append(rows_2)
        rows_3 = grid[i][3]
        blank_3.append(rows_3)
        rows_4 = grid[i][4]
        blank_4.append(rows_4)
        i += 1
    return [blank_0, blank_1, blank_2, blank_3, blank_4]


def print_grid(grid):
    """Print list of lists in matrix form

    Args:
        grid (list): list of lists

    Returns:
        list: matrix
    """
    for i in grid:
        print(i)


def create_grid():
    """Initializes grid

    Args:
        dim (int): dimension

    Returns:
        list: list of lists
    """
    return [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


if __name__ == "__main__":
    main()
