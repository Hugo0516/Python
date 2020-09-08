# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         h = {}
#         for i, num in enumerate(nums):
#             n = target - num
#             if n not in h:
#                 h[num] = i
#             else:
#                 return [h[n], i]


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


def main():
    demo = Solution()

    print(demo.twoSum([2, 7, 11, 5], 16))


if __name__ == '__main__':
    main()
