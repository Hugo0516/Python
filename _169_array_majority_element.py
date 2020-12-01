class Solution(object):

    def majorityElement(self, nums):
        index, cnt = 0, 1
        for i in range(1, len(nums)):
            if nums[index] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    index = i
                    cnt = 1

        return nums[index]


"""
    Reference: Michelle
    
    Time Complexity: O(n)
    Space Complexity: O(1)
"""

demo = Solution()
input_1 = [3, 2, 3]
print(demo.majorityElement(input_1))
