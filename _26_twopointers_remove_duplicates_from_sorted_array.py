from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return N
        left, right = 0, 1

        while right < N:
            while right < N and nums[right] == nums[left]:
                right += 1
            left += 1
            if right < N:
                nums[left] = nums[right]
        return left


"""
    注意是sorted array 所以要特別想一下性質
    慢指針指向應該放入元素的位置，每次移動一格。快指針找到應該放哪個元素，每次找到下一個新的元素。
    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] >> [0, 1, 2, 3, 4]
    和 80 題互相參照
    
    https://blog.csdn.net/fuxuemingzhu/java/article/details/51346776
"""

if __name__ == '__main__':
    dmeo = Solution()
    input_1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    input_2 = [0, 1, 3, 3, 6, 6, 9, 9]
    input_3 = [0, 3, 4]
    print(dmeo.removeDuplicates(input_2))
