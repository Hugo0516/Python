class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        while True:
            if row < rows and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else:
                    col -= 1
            else:
                return False


"""
    和 74 題 比較, 解法完全一模一樣
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79459314
"""
if __name__ == '__main__':
    demo = Solution()
    input_1 = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    target_1 = 5
    target_2 = 20

    print(demo.searchMatrix(input_1, target_1), demo.searchMatrix(input_1, target_2))
