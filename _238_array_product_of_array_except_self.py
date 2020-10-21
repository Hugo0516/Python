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
    Input:  [1,2,3,4]
    Output: [24,12,8,6]
    這一題好難的想法，過幾天再 follow up 一遍
    
    Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array
     (including the whole array) fits in a 32 bit integer.
    
    Note: Please solve it without division and in O(n).
    
    Follow up:
    Could you solve it with constant space complexity? 
    (The output array does not count as extra space for the purpose of space complexity analysis.)
    
    思路：
    num = [1, 2, 3, 4]
    num[0] 的 output 可以看成num[0] 左邊所有數字乘積(因為剛好在最左邊, 所以設成1) * num[0] 右邊所有數字乘積(即2*3*4)
    => 所以 num[0] = 1(左) * 24(右)
    num[1~3] 以此類推
    
    
    Time complexity : O(N) 
    where N represents the number of elements in the input array. 
    We use one iteration to construct the array L, 
    one to construct the array R and one last to construct the answer array using L and R.
    
    Space complexity : O(N) 
    used up by the two intermediate arrays 
    that we constructed to keep track of product of elements to the left and right. 
"""

if __name__ == '__main__':
    demo = Solution()
    print(demo.productExceptSelf([1, 2, 3, 4]))
