from typing import List


class Solution:
    # Finished by myself
    # It is too slow, only win 7% = =
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i not in nums:
                return i
            else:
                if i == len(nums) - 1:
                    return len(nums)

    # Gauss' Formula 超屌算法 = =
    def missingNumber2(self, nums: List[int]) -> int:
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    # 我覺得這想法可以
    def missingNumber3(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


"""
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
    8 is the missing number in the range since it does not appear in nums.
    
    
    Guass:
    Time complexity : O(n)
    Although Gauss' formula can be computed in O(1) time, summing nums costs us O(n) time, 
    so the algorithm is overall linear. 
    Because we have no information about which number is missing, 
    an adversary could always design an input for which any algorithm that examines fewer than n numbers fails. 
    Therefore, this solution is asymptotically optimal.
    
    Space complexity : O(1) 
    This approach only pushes a few integers around, so it has constant memory usage.
    
    Set method:
    Time complexity : O(n)
    Because the set allows for O(1) containment queries, the main loop runs in O(n) time. 
    Creating num_set costs O(n) time, as each set insertion runs in amortized O(1) time, 
    so the overall runtime is O(n+n)=O(n).
    
    Space complexity : O(n)
    nums contains n−1 distinct elements, so it costs O(n) space to store a set containing all of them.
"""

if __name__ == '__main__':
    demo = Solution()
