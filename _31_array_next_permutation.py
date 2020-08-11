from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        self.reverse(nums, i, n - 1)
        if i > 0:
            for j in range(i, n):
                if nums[j] > nums[i - 1]:
                    self.swap(nums, i - 1, j)
                    break

    def reverse(self, nums, i, j):
        """
        contains i and j.
        """
        for k in range(i, (i + j) // 2 + 1):
            self.swap(nums, k, i + j - k)

    def swap(self, nums, i, j):
        """
        contains i and j.
        """
        nums[i], nums[j] = nums[j], nums[i]


"""
    https://blog.csdn.net/fuxuemingzhu/java/article/details/82113409
"""

if __name__ == '__main__':

    demo = Solution()
    input_1 = [1, 2, 3]
    input_2 = [3, 2, 1]
    input_3 = [1, 1, 5]
    demo.nextPermutation(input_1)
    demo.nextPermutation(input_2)
    demo.nextPermutation(input_3)

    print(input_1, input_2, input_3)