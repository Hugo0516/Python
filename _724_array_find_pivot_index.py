from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)

        for i in range(len(nums)):
            r -= nums[i]

            if l == r:
                return i

            l += nums[i]

        return -1


"""
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
    The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
    Also, 3 is the first index where this occurs.
"""

if __name__ == '__main__':
    demo = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    print(demo.pivotIndex(nums))
