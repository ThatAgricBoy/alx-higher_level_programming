#!/usr/bin/python3

"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""

import sys

def nqueens(N):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve(board, col, solutions):
        if col == N:
            solution = []
            for i in range(N):
                row = []
                for j in range(N):
                    row.append(str(board[i][j]))
                solution.append("".join(row))
            solutions.append(solution)
            return

        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve(board, col + 1, solutions)
                board[i][col] = 0

    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for x in range(N)] for y in range(N)]
    solutions = []
    solve(board, 0, solutions)

    for solution in solutions:
        print("\n".join(solution))
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
