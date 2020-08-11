from bisect import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]

    def searchRange2(self, nums, target):
        left = self.lowwer_bound(nums, target)
        right = self.higher_bound(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]

    def lowwer_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def higher_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left


"""
    python 用 bisect 當然是最方便又快速的哦！！
    method2 是實作 bisect module content~
    
    Both method 1 and method 2:
    Time Complexity: O(logN), Space Complexity: O(1)
    https://blog.csdn.net/fuxuemingzhu/java/article/details/83273084
"""

if __name__ == '__main__':
    demo = Solution()
    nums_1 = [5, 7, 7, 8, 8, 10]
    target_1 = 8
    print(demo.searchRange(nums_1, target_1))

    print(demo.searchRange2(nums_1, target_1))
