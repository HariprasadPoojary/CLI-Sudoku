# solve sudoku using backtracking...
# puzzle -> list of list
# [
#     [3, 9, -1,   -1,5,-1,  -1,-1,-1],
#     [-1, 2, -1,   6,-1,-1,  -1,8,-1],
#     [-1, -1, -1   -1,-1,-1   3,-1,-1],
#
#     [..., ..., ...],
#     [..., .5., ...],
#     [..., ..., ...],
#
#     [..., ..., ...],
#     [..., ..., ...],
#     [..., ..., ...]
# ]


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

    return None, None  # if no empty spaces in puzzle (-1)


def is_valid_guess(game, guess, row, col) -> bool:
    # * Check if the gussed number is already present in the row, col and the 3x3 matrix
    # checking row
    row_values = game[row]
    if guess in row_values:
        return False
    # checking col
    # * creating a list of values in column where we're looping through rows but the column index is same
    col_values = [game[i][col] for i in range(9)]
    if guess in col_values:
        return False
    # checking 3x3 matrix
    # * get the index of the row set (1st, 2nd or 3rd) by row // 3 then get the exact row by * 3, same for cols
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    # check the values
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if game[r][c] == guess:
                return False

    # Reaching here means the guess is valid
    return True


def sudoku_solver(game):
    # Step 1 -> Choose somewhere to make a guess
    row, col = find_next_empty(game)
    # Step 1.1 -> of there is no empty space
    if row is None:
        return True
    # Step 2 -> There is empty space and we've to put a number 1-9
    for guess in range(1, 10):
        # Step 3 -> check if the guess is valid
        if is_valid_guess(game, guess, row, col):
            # Step 3.1 -> Place the guess
            game[row][col] = guess
            # Step 4 -> Call this function recursively to solve till there is no empty(-1) values in the game
            if sudoku_solver(game):
                return True
        
        # Step 5 -> If our guess is not valid then backtrack and try a new number
        game[row][col] = -1 # reset the guess
    
    # Step 6 -> If none of the numbers are valid then this puzzle is UNSOLVABLE 💔
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

    print(sudoku_solver(example_board))
    print(example_board)