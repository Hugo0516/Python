from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_row, zero_col = False, False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    zero_row = True if i == 0 else zero_row
                    zero_col = True if j == 0 else zero_col

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        if zero_row:
            for j in range(n):
                matrix[0][j] = 0

        if zero_col:
            for i in range(m):
                matrix[i][0] = 0

        return


"""
    https://www.youtube.com/watch?v=FPdM2C16Qew
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    input_2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]

    demo.setZeroes(input_1)
    demo.setZeroes(input_2)
    print(input_1, input_2)
