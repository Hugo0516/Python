from bisect import bisect, bisect_left
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)

"""
    t.ly/piaS
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 3, 5, 6]
    val_1 = 5
    print(demo.searchInsert(input_1, val_1))
