from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if (matrix is None) or len(matrix) == 0:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        grid = [[0] * cols for i in range(rows)]
        res = 0

        def buildHistogram(matrix: List[List[str]], grid: List[List[int]]):
            for j in range(len(matrix[0])):
                grid[0][j] = (1 if matrix[0][j] == '1' else 0)

                # 就如函式名稱一樣，這裡是在做建構 histogram 的地方
            for i in range(1, len(matrix)):
                for j in range(len(matrix[0])):
                    grid[i][j] = grid[i - 1][j] + 1 if matrix[i][j] == '1' else 0

        def maxRec(grid: List[List[int]], buttom: int) -> int:
            stack = list()
            stack.append(-1)
            res_1 = 0
            curindex = 0

            while curindex < len(grid[buttom]):
                while stack[-1] != -1 and grid[buttom][curindex] <= grid[buttom][stack[-1]]:
                    res_1 = max(res_1, grid[buttom][stack.pop()] * (curindex - stack[-1] - 1))
                stack.append(curindex)
                curindex += 1

            while stack[-1] != -1:
                res_1 = max(res_1, grid[buttom][stack.pop()] * (len(grid[buttom]) - stack[-1] - 1))

            return res_1

        buildHistogram(matrix, grid)
        for i in range(rows):
            res = max(res, maxRec(grid, i))

        return res

"""
解題思路：
        https://www.youtube.com/watch?v=9NZuhGL0SlU
        
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(demo.maximalRectangle(input_1), end='')
    print('\nQQ')