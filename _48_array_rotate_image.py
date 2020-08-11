from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            for i in range(rows // 2):
                for j in range(cols):
                    matrix[i][j], matrix[rows - i - 1][j] = matrix[rows - i - 1][j], matrix[i][j]
            for i in range(rows):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


"""
    解題方法
        做法挺簡單，先上下翻轉，再延左上到右下的對角線進行翻轉(鏡像操作)。

        需要注意的是上下翻轉的時候是rows-i-1，而不是rows-i。
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79451733
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    demo.rotate(input_1)
    print(input_1)