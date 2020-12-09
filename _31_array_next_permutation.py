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
    Time Complexity: O(n), In worst case, only two scans of the whole array are needed.
    Space Complexity: O(1), No extra space is used. In place replacements are done.
    
    舉個例子，當前組合為12431，可以看出431是遞減的，同時4>2，這樣我們把431倒序，組合就變為12134，
    然後從134中找出第一個大於2的數字和2交換，這樣就得到了下一個組合13124。對於完全遞減的組合例如4321在倒序之後就可以結束了。
    
    這題很 tricky, 要先找出規則, 如果知道規則難度就會下降了, 反正就是先逆序再交換
    
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

    input_4 = [1, 2, 4, 3, 1]
    demo.nextPermutation(input_4)
    print(input_4)

    input_5 = [4, 3, 2, 1]
    demo.nextPermutation(input_5)
    print(input_5)