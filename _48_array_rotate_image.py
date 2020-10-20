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

    # 記住這方法
    # Time Complexity: O(n^2) / Space Complexity:O(1) ( 我自己想的 )
    def rotate2(self, matrix: List[List[int]]) -> None:
        h = len(matrix)  # 4
        n = h - 1  # start from 0, so n = maximum = 3

        for i in range(h // 2):     # why h//2 => 可以看圖思考, 撥洋蔥 (用 6*6 matrix 想)
            for j in range(i, n - i):   # 同上
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j][i]
                matrix[n - j][i] = matrix[n - i][n - j]
                matrix[n - i][n - j] = matrix[j][n - i]
                matrix[j][n - i] = tmp


"""
    解題方法
        做法挺簡單，先上下翻轉，再延左上到右下的對角線進行翻轉(鏡像操作)。

        需要注意的是上下翻轉的時候是rows-i-1，而不是rows-i。
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79451733
    
    
    (為 0 開始)
    Michelle:
    想：
    1. 是否該 go through 每個點？ => 2 個 for loop => 不好 => high time complexity
    2. 找規律
    new row index => old column index
    new column index => maximum - old row index
    Michelle 的解法就是, 找到規律後 => 從最外面一圈, 然後慢慢把每一層撥開漸漸往內
    https://www.youtube.com/watch?v=OlO_bzYid
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

    input_1 = [[5, 1, 9, 11],
               [2, 4, 8, 10],
               [13, 3, 6, 7],
               [15, 14, 12, 16]]

    demo.rotate2(input_1)
    print(input_1)
