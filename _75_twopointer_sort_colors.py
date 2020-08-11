from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p, q = 0, 0
        k = len(nums) - 1

        while q <= k:
            if p < q and nums[q] == 0:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
            elif nums[q] == 2:
                nums[q], nums[k] = nums[k], nums[q]
                k -= 1
            else:
                q += 1


"""
    https://www.youtube.com/watch?v=L-mWbEmUnUA
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [2, 0, 2, 1, 1, 1]
    demo.sortColors(input_1)
    print(input_1)
