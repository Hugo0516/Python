from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        _len = len(nums)
        prod = 1
        for i in range(_len):
            answer.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(_len - 1, -1, -1):
            answer[i] *= prod
            prod *= nums[i]
        return answer


"""
    Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array
     (including the whole array) fits in a 32 bit integer.
    
    Note: Please solve it without division and in O(n).
    
    Follow up:
    Could you solve it with constant space complexity? 
    (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

if __name__ == '__main__':
    demo = Solution()
    print(demo.productExceptSelf([1, 2, 3, 4]))
