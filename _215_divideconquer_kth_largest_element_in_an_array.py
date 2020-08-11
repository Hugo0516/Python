from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k - 1):
            nums.remove(max(nums))
        return max(nums)

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


"""
    Input: [3,2,1,5,6,4] and k = 2
    Output: 5
    
    Input: [3,2,3,1,2,4,5,5,6] and k = 4
    Output: 4
    
    Time Complexity: 
        method 1: O(n)
        method 2: O(NLogN)
    https://blog.csdn.net/fuxuemingzhu/article/details/79264797
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [3, 2, 1, 5, 6, 4]
    input_2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    print(demo.findKthLargest(input_1, 2))
    print(demo.findKthLargest2(input_2, 4))
