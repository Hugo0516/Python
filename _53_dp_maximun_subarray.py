from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
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

if __name__ == '__main__':
    input_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    print(sol.maxSubArray(input_1), end='')
