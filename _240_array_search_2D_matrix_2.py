from typing import List


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


# divide & Conquer
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right - left) // 2

            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            x = matrix[row][mid]
            while row <= down and matrix[row][mid] <= target:
                x = matrix[row][mid]
                if matrix[row][mid] == target:
                    return True
                row += 1

            # 只需要再次搜尋 左下 or 右上 部分 即可
            return search_rec(left, row, mid - 1, down) or \
                   search_rec(mid + 1, up, right, row - 1)

        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


class Solution3:
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while hi >= lo:
            mid = (lo + hi) // 2
            if vertical:  # searching a column
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else:  # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True

        return False


class Solution4:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])

        cur_row, cur_col = 0, n - 1

        while cur_row < m and cur_col >= 0:
            if matrix[cur_row][cur_col] == target:
                return True
            if matrix[cur_row][cur_col] > target:
                cur_col -= 1
            else:
                cur_row += 1


""" 
    Approach 1: Search Space Reduction
    此解法有點 trick, 但效果卻很好
    Time Complexity: O( n+m )
    Space Complexity: O(1), since this approach only manipulate a few pointers, its memory footprint is constant
    
    **** Approach 2 ****  Divide and Conquer
    照理來說, 這一題應該要先想到 divide and conquer, 因為我們可以把 matrix 分解成 左上 右上 左下 右下 4組 metrix 下去做分析
    Time Complexity: O( nlogn )
    Space Complexity: O( nlogn )
    
    Approach 3: Bimnary Search
    和 74 題 比較, 解法完全一模一樣
    Time Complexity: O(log(n!))
    Space Complexity: O(1)
    
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79459314
    
    https://leetcode.com/problems/search-a-2d-matrix-ii/solution/
    
    Approach 4: 
    這個思維很好, 和 sol 2的思維一樣, 不過更好！！！
    因為我們知道一個數的 左邊 都比較小, 下面 都比較大; 然後我們又要過程精簡 => 所以才想到要從右上角開始！！！！！！
    Reference :https://www.youtube.com/watch?v=g4Qy83toSzc
    
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

    target_1 = 13
    target_2 = 20

    print(demo.searchMatrix(input_1, target_1), demo.searchMatrix(input_1, target_2))

    demo2 = Solution2()
    print(demo2.searchMatrix(input_1, target_1))

    input_3 = [
        [1, 4, 7, 11, 15],
        [2, 5, 6, 19, 12]
    ]
    demo3 = Solution3()
    print(demo3.searchMatrix(input_3, 19))
