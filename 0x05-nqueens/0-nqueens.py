#!/usr/bin/python3
""" N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP) """

import sys

class NQueen:
    """ Class for solving the N Queen Problem """

    def __init__(self, n):
        """ Initialize the NQueen solver with board size 'n'. """
        self.n = n
        self.x = [0 for i in range(n + 1)]
        self.res = []

    def place(self, k, i):
        """ Check if it's safe to place the k-th Queen in the i-th column.

        Args:
            k (int): The queen number.
            i (int): The column number to check.

        Returns:
            bool: True if the queen can be placed, False otherwise.
        """
        for j in range(1, k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                # There is already a queen in the same column or diagonal
                return False
        return True

    def nQueen(self, k):
        """ Tries to place every queen on the board.

        Args:
            k (int): The queen number to start evaluating from (should be 1).
        """
        for i in range(1, self.n + 1):
            if self.place(k, i):
                # Queen can be placed in the i-th column
                self.x[k] = i
                if k == self.n:
                    # Placed all N Queens (A solution was found)
                    solution = []
                    for i in range(1, self.n + 1):
                        solution.append([i - 1, self.x[i] - 1])
                    self.res.append(solution)
                else:
                    # Need to place more Queens
                    self.nQueen(k + 1)
        return self.res


# Main
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(N)
res = queen.nQueen(1)

for i in res:
    print(i)
