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


def solve_n_queens(n):
    """Solves the N-queens puzzle and returns a list of solutions."""
    if n < 4:
        return []

    def init_board(n):
        return [[' '] * n for _ in range(n)]

    def get_solution(board):
        return [[r, c] for r in range(n)
                for c in range(n)
                if board[r][c] == 'Q']

    def recursive_solve(board, row, queens, solutions):
        if queens == n:
            solutions.append(get_solution(board))
            return solutions

        for c in range(n):
            if board[row][c] == ' ':
                tmp_board = [row[:] for row in board]
                tmp_board[row][c] = 'Q'
                for r in range(n):
                    if r != row:
                        tmp_board[r][c] = 'x'
                        diag1 = c - row + r
                        diag2 = c + row - r
                        if 0 <= diag1 < n:
                            tmp_board[r][diag1] = 'x'
                        if 0 <= diag2 < n:
                            tmp_board[r][diag2] = 'x'
                recursive_solve(tmp_board, row + 1, queens + 1, solutions)

        return solutions

    return recursive_solve(init_board(n), 0, 0, [])


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_n_queens(n)
    for soln in solutions:
        print(soln)
