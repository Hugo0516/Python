from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        for i in range(1, max(max(nums), 1) + 2):
            if i not in nums:
                return i


"""
    https://blog.csdn.net/L141210113/article/details/88527991
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 2, 0]
    print(demo.firstMissingPositive(input_1))
