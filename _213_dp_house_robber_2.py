from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif not nums:
            return 0

        left = nums[:-1]
        right = nums[1:]

        left_res = self.dp_program(left)
        right_res = self.dp_program(right)

        return max(left_res, right_res)

    def dp_program(self, nums):
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


"""
*** 這題還蠻有趣的 ***
這一題基本思路和 198 題一樣, 只是 nums 必須做點小改變

Time Complexity: O(N)
Space Complexity: O(N), 也可以變成O(1), 就看我dp_program 要不要改成 in-place 寫法
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [2, 3, 2]
    input_2 = [4, 1, 2]

    print(demo.rob(input_1))
    print(demo.rob(input_2))