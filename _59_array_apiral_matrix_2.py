from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(n):
            matrix.append([0 for j in range(n)])

        rowBegin = 0
        rowEnd = n - 1
        colBegin = 0
        colEnd = n - 1
        number = 1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin, colEnd + 1):
                matrix[rowBegin][i] = number
                number += 1
            rowBegin += 1

            for i in range(rowBegin, rowEnd + 1):
                matrix[i][colEnd] = number
                number += 1
            colEnd -= 1

            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    matrix[rowEnd][i] = number
                    number += 1
                rowEnd -= 1

            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    matrix[i][colBegin] = number
                    number += 1
                colBegin += 1

        return matrix


""" 
    和 54 比較!!!
    https://www.youtube.com/watch?v=DVP7u6giGps
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = 3
    print(demo.generateMatrix(3))
