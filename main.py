#
#
#
# SUDOKU SOLVER CARLOS AND MICHAL
#
# still working on it
import math

counterTries = 0


def solveSudoku(currentBoard):
    empty = findEmpty(currentBoard)
    if not empty:
        return True
    else:
        row = empty[0]
        cell = empty[1]
    possible_number = [*range(1, 10)]
    validSudoku(possible_number, row, cell, currentBoard)
    for i in range(1, 10):
        if validSudoku(i, row, cell, currentBoard):
            board[row][cell] = i

            if solveSudoku(currentBoard):
                return True

            board[row][cell] = 0

    return False


# Finding 0 in the grid
def findEmpty(currentBoard):
    for i in range(len(currentBoard)):
        for j in range(len(currentBoard[i])):
            if currentBoard[i][j] == 0:
                return [i, j]
    return None


def validSudoku(nr, row, cell, current_board):
    for i in range(len(current_board[row])):

        if current_board[row].__contains__(nr):  # or board[1][0]==(i+1)  :
            return False
        # possible_number.remove(i+1)
        elif current_board[i][cell] == nr:
            return False

    squareX = math.floor(row / 3)
    squareY = math.floor(cell / 3)
    for j in range(3):
        for z in range(3):
            # print(board[j + 3 * squareX][z + 3 * squareY])
            if current_board[j + 3 * squareX][z + 3 * squareY] == nr:
                return False

    return True


def print_SudokuBoard(currentlyboard):
    topOfSquare = "═══╤═══╤═══╦"
    middleOfSquare = " 0 │"

    print("╚═══╧═══╩═══╝")
    topOfSquare = "╔" + topOfSquare * 2 + topOfSquare.replace("╦", "╗", 1)

    middleOfSquare = "║" + middleOfSquare

    print(topOfSquare)
    # Creating boafrd
    for i in range(len(currentlyboard)):
        print("║", end="")
        for j in range(len(currentlyboard[i])):
            if j % 3 == 2:
                formatting = " ║"
            else:
                formatting = " │"
            print("{}{}{}".format(" ", currentlyboard[i][j], formatting), end="")

        print("")
        if i % 3 == 2:
            print("╠" + "═══╪═══╪═══╬" * 2 + "═══╪═══╪═══╣")
        else:
            print("╟" + "───┼───┼───╫" * 2 + "───┼───┼───╢")

        # if i % 3 == 2 and i != 0:


__name__ = '__main__'

while __name__ == '__main__':
    print("Welcome To Sudoku Solver")
    print("""Please select one of the following options:
    Solve Grid Number: 1
    Solve Grid Number: 2
    Solve Grid Number: 3
    Solve Grid Number: 4
    """)
    gridNr = input("Solve grid number:")
    if gridNr == "1":
        __name__ = "valid"
        board = [
            [0, 0, 0, 0, 6, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 4, 9, 0, 2],
            [0, 0, 9, 0, 1, 5, 7, 0, 8],
            [7, 0, 0, 9, 4, 6, 0, 5, 0],
            [0, 0, 0, 7, 0, 1, 4, 9, 0],
            [9, 0, 6, 5, 2, 0, 8, 7, 1],
            [4, 9, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 9, 0, 6, 0, 0],
            [6, 0, 7, 4, 0, 0, 5, 8, 9]
        ]
    elif gridNr == "2":
        __name__ = "valid"
        board = [
            [2, 0, 0, 0, 0, 6, 3, 4, 0],
            [3, 0, 7, 0, 0, 0, 6, 2, 5],
            [0, 1, 0, 3, 0, 0, 7, 9, 8],
            [8, 3, 4, 2, 0, 0, 1, 5, 0],
            [1, 5, 0, 8, 0, 0, 0, 0, 6],
            [0, 0, 0, 5, 9, 1, 0, 0, 0],
            [9, 6, 3, 0, 7, 0, 0, 0, 0],
            [7, 8, 5, 0, 0, 2, 0, 0, 0],
            [4, 0, 1, 9, 0, 0, 0, 0, 0]
        ]
    elif gridNr == "3":
        __name__ = "valid"
        board = [
            [0, 3, 0, 0, 6, 2, 4, 0, 0],
            [0, 9, 0, 8, 5, 0, 0, 2, 6],
            [0, 2, 0, 0, 7, 9, 1, 0, 0],
            [0, 5, 0, 7, 0, 0, 0, 0, 0],
            [0, 4, 0, 2, 8, 6, 0, 0, 5],
            [2, 0, 9, 0, 0, 0, 6, 7, 0],
            [5, 6, 0, 9, 0, 0, 8, 1, 7],
            [4, 0, 8, 0, 0, 7, 5, 9, 2],
            [0, 0, 0, 5, 0, 8, 3, 6, 0]
        ]
    elif gridNr == "4":
        __name__ = "valid"
        board = [
            [0, 8, 0, 4, 0, 0, 1, 2, 0],
            [0, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
    else:
        print("\nSorry I do not understand\n")
        __name__ = "__main__"

print_SudokuBoard(board)
solveSudoku(board)
print_SudokuBoard(board)
