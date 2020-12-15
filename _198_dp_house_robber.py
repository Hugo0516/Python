from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif not nums:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + max(dp[:i - 1]), dp[i - 1])

        return max(dp)
        # 我原本想說能不能用 dp[-1], 後來發現不行, 因為假如只有兩個[4, 1],  那output會變成1


class Solution2:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif not nums:
            return 0

        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + max(nums[:i - 1]), nums[i - 1])

        return max(nums)


"""
轉移方程式：

dp[i] = Max money after "visiting" house[i], visiting過 不代表要搶
dp[i] = max(dp[i-2] + money[i], dp[i-1])

Time Complexity: O(n)
Space Complexity: O(n), 如果用 in-place 方法, 可縮減至 O(1) <即 solution2 方法>
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 2, 3, 1]
    input_2 = [2, 7, 9, 3, 1]
    input_3 = [2, 1, 1, 2]  # 思考此例子, 特例
    input_4 = [2, 3, 2]

    print(demo.rob(input_1))
    print(demo.rob(input_2))
    print(demo.rob(input_3))
    print(demo.rob(input_4))
