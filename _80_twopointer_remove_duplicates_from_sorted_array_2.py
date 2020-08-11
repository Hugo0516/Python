from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
        return i


"""
    可以和 26題互相參照
    幹你娘好難 = =
    https://blog.csdn.net/fuxuemingzhu/java/article/details/82829709
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 1, 1, 2, 2, 3]
    input_2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]

    print(demo.removeDuplicates(input_1))
    print(demo.removeDuplicates(input_2))
