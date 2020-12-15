from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        N = len(nums)
        cur, prev = 0, 0
        res = float("-inf")
        for i in range(N):
            cur = nums[i] + (prev if prev > 0 else 0)
            prev = cur
            res = max(res, cur)
        return res


# 明顯的DP方法去解決。
#
# 通過構建一個和原長一樣長的數組， dp數組的含義是以dp[i]為結尾的最大子數組的和。
#
# 狀態轉移公式：
#
# dp[i] = dp[i - 1] + nums[i] 當nums[i] >= 0 。
# dp[i] = nums[i] 當nums[i] < 0 。


class Solution1:
    def cross_sum(self, nums, left, right, p):
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p, left - 1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(p + 1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]

        p = (left + right) // 2

        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)

        return max(left_sum, right_sum, cross_sum)

    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)


class Solution2:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum


class Solution3:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)

        return max_sum


class Solution4:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        # 轉移方程式：
        # dp[i] = maxSubArray(0..i) 的值, 用到前i個元素(包含第i個) 最大可以為多少
        # dp[i] = dp[i-1] > 0 ? nums[i] + dp[i-1] : nums[i]

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            if dp[i - 1] > 0:
                dp[i] = max(dp[i - 1] + nums[i], nums[i])
            else:
                dp[i] = nums[i]

        return max(dp)


"""
和 152 很像

Solution: Michelle 解法

Approach 1: Divede and Conquer

Time Complexity: O(NlogN), 
Space Complexity: O(logN), to keep the recursion stack.

Approach 2: Greedy
Time Complexity: O(N), since it's one pass along the array
Space Complexity: O(1), since it's a constant space solution

Approach 3: DP
Time Complexity: O(N), since it's one pass along the array
Space Complexity: O(1), since it's a constant space solution

Approach 4: DP, Hua Hua 版本, 與 Approach 3 的 DP 差異在說, Approach 4 有另外多存一個數組
而 Approach 3 則是用 in-place 解法
"""

if __name__ == '__main__':
    input_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    print(sol.maxSubArray(input_1), end='')

    demo2 = Solution2()
    demo3 = Solution3()
    demo4 = Solution4()

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(demo2.maxSubArray(nums))
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(demo3.maxSubArray(nums))
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(demo4.maxSubArray(nums))
