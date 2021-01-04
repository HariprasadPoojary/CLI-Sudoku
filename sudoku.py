def find_next_empty(game) -> tuple:
    # find row,col where index value -> -1 i.e. empty
    # here we return row, col from the game i.e. list of lists
    # * where no. of list is the row and index inside of this list is the col
    # * e.g. (1,3) from bleow example will be 2nd row(list), 5th value(within that list)

    # our indices will be 0-8, 9 values in a row
    for r in range(9):
        for c in range(9):
            if game[r][c] == -1:
                return r, c

    return None, None


def sudoku_solver(game):
    # solve sudoku using backtracking...
    # puzzle -> list of list
    # [
    #     [3, 9, -1,   -1,5,-1,  -1,-1,-1],
    #     [-1, 2, -1,   6,2,-1,  -1,8,-1],
    #     [..., ..., ...],
    #
    #     [..., ..., ...],
    #     [..., ..., ...],
    #     [..., ..., ...],
    #
    #     [..., ..., ...],
    #     [..., ..., ...],
    #     [..., ..., ...]
    # ]

    # 1. Choose somewhere to make a guess
    row, col = find_next_empty(game)
    pass
