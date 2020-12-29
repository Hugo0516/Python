from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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


class Solution2:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # binary search
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False


"""
    和 240 題比較, 解法完全一模一樣
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79459200
    
Approach 2:Binary Search
Time Complexity: O(log(mn)), since it's a standard binary search
Space Complexity: O(1)

"""
if __name__ == '__main__':
    demo = Solution()
    input_1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target_1 = 3

    input_2 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]

    target_2 = 13

    print(demo.searchMatrix(input_1, target_1))
    print(demo.searchMatrix(input_2, target_2))

    demo2 = Solution2()
    print(demo2.searchMatrix(input_1, target_1))
