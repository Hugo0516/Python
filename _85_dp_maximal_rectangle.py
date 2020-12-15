from typing import List


class Solution:

    # Get the maximum area in a histogram given its heights
    def leetcode84(self, heights):
        stack = [-1]

        max_area = 0
        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix: return 0

        max_area = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # update the state of this row's histogram using the last row's histogram
                # by keeping track of the number of consecutive ones

                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

            # update maxarea with the maximum area from this row's histogram
            max_area = max(max_area, self.leetcode84(dp))
        return max_area


class Solution2:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n  # initialize left as the leftmost boundary possible
        right = [n] * n  # initialize right as the rightmost boundary possible
        height = [0] * n

        max_area = 0

        for i in range(m):

            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                max_area = max(max_area, height[j] * (right[j] - left[j]))

        return max_area


"""
解題思路：
    => 這題是 leetcode 84. 的進階題, 因此我們可以用 84 code 來 build 這一題
        https://www.youtube.com/watch?v=2Yk3Avrzauk
        
    Approach 1: <Stack>
    Time Complexity: O(NM), Running leetcode84 on each row takes M (length of each row) time. This is done N times for O(NM).
    Space Complexity: O(M), We allocate an array the size of the the number of columns to store our widths at each row. 
    
    Approach 2: <DP> DP可以與 leetcode 221 參考
    Time Complexity: O(NM), In each iteration over N we iterate over M a constant number of times.
    Space Complexity: O(M), M is the length of the additional arrays we keep.
    
    left[]: 從左到右, 出現連續 '1' 的 string 的第一個座標
    right[]: 從右到左, 出現連續 '1' 的 string 的最後一個座標
    height[]:從上到下的高度
    res: (right[j] - left[j]) * heights[j]
    
    height:             left:               right:
    1 0 1 0 0           0 0 2 0 0           1 5 3 5 5
    2 0 2 1 1           0 0 2 2 2           1 5 3 5 5
    3 1 3 2 2           0 0 2 2 2           1 5 3 5 5
    4 0 0 3 0           0 0 0 3 0           1 5 5 4 5
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(demo.maximalRectangle(input_1))

    demo2 = Solution2()
    print(demo2.maximalRectangle(input_1))
