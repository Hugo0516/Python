from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            # 改成這一行速度從 6% 提升到 90% = =
            # pivot = left + ((right - left) >> 1)

            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


"""
Time Complexity: O(LogN)
Space Complexity: O(1)
"""

if __name__ == '__main__':
    pass
