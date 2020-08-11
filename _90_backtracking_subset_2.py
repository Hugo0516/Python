from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, res, path + [nums[i]])

    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.helper(nums, 0, res, [])
        return res

    def helper(self, nums, index, res, path):
        if index > len(nums):
            return
        res.append(path)

        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.helper(nums, i + 1, res, path[:])
            path.pop()


"""
https://blog.csdn.net/fuxuemingzhu/java/article/details/79785548
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 2, 2]
    print(demo.subsetsWithDup(input_1))
    print(demo.subsetsWithDup2(input_1))
