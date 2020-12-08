from collections import defaultdict


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or \
                        d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            """
            Remove a number which didn't lead
            to a solution
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'

        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion
            to continue to place numbers
            till the moment we have a solution
            """
            # if we're in the last cell
            # that means we have the solution
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            # if not yet
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                # go to the next column
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            """
            Backtracking
            """
            # if the cell is empty
            if board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)

        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n) * n + col // n

        # init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = False
        backtrack()


"""
Approach 0: Brute Force

The first idea is to use brut-force to generate all possible ways to fill the cells with numbers from 1 to 9, 
and then check them to keep the solution only. That means 9^81 operations to do, 
where 9 is a number of available digits and 81 is a number of cells to fill. 
Hence we're forced to think further how to optimize. 

Approach 1: Backtracking

There are two programming conceptions here which could help.

1-1. The first one is called constrained programming.
That basically means to put restrictions after each number placement. 
One puts a number on the board and that immediately excludes this number from further usage in the current row, 
column and sub-box. That propagates constraints and helps to reduce the number of combinations to consider.

=> constraints propagation: EX: I put "1" at [0,2], then no more "1" in rows[0], column[2] and boxes[0]

1-2 Backtracking
Let's imagine that one has already managed to put several numbers on the board. 
But the combination chosen is not the optimal one and there is no way to place the further numbers. 
What to do? To backtrack. That means to come back, to change the previously placed number and try to proceed again. 
If that would not work either, backtrack again.

Time Complexity: O((9!)^9)
Space Complexity: 81
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    demo.solveSudoku(input_1)
    print(input_1)
