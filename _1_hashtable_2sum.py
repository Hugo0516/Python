# Brute Force
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         array_len = len(nums)
#
#         for i in range(0, array_len-1):
#             for j in range(i+1, array_len):
#                 if(nums[i] + nums[j] == target):
#                     return(i, j)

class Solution:
    def twoSum(self, nums, target):
        dict_1 = {}
        for i, num in enumerate(nums):
            tar_num = target - num
            if tar_num in dict_1:
                return [dict_1[tar_num], i]
            dict_1[num] = i

    def twoSum2(self, nums, target):
        dict_2 = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict_2:
                return [dict_2[complement], i]
            dict_2[nums[i]] = i


def main():
    demo = Solution()

    print(demo.twoSum([2, 7, 11, 5], 16))
    print(demo.twoSum2([2, 7, 11, 5], 16))


'''
    Both twoSum and twoSum2 are One-pass Hash Table
    Time Complexity: O(n) / Space Complexity: O(n) 
'''

if __name__ == '__main__':
    main()
