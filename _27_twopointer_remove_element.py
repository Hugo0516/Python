from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        left, right = 0, N - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left


"""
    [3, 2, 2, 3], 3 >> [2, 2], 2
    [0, 1, 2, 2, 3, 0, 4, 2], 2 >> [0, 1, 3, 0, 4], 5
    https://blog.csdn.net/fuxuemingzhu/java/article/details/51303161
"""
if __name__ == '__main__':
    demo = Solution()
    input_1 = [3, 2, 2, 3]
    val_1 = 3

    input_2 = [0, 1, 2, 2, 3, 0, 4, 2, 7 ,9]
    val_2 = 2

    print(demo.removeElement(input_1, val_1))
    print(demo.removeElement(input_2, val_2))