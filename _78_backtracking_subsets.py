from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(degree, start, cur):
            if len(cur) == degree:
                ans.append(cur.copy())
                return

            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(degree, i + 1, cur)
                cur.pop()

        for i in range(len(nums) + 1):
            dfs(i, 0, [])
        return ans

    def subsets2(self, nums):
        res = []
        self.dfs2(nums, 0, res, [])
        return res

    def dfs2(self, nums, index, res, path):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs2(nums, i + 1, res, path + [nums[i]])

    def subsets3(self, nums):
        res = []
        path = []
        self.helper(nums, res, path, 0)
        return res

    def helper(self, nums, res, path, start):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.helper(nums, res, path, i + 1)
            path.pop()


"""
    method 1:
    degree = 遞迴深度
    https://zxi.mytechroad.com/blog/searching/leetcode-78-subsets/
    我這裡, 其實好像沒有用到 backtracking 的技巧(?
    
    
    method 2:
    recursion method
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79359540
    
    method 3:
    backtracking method
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79359540
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 2, 3]
    print(demo.subsets(input_1))
    print(demo.subsets2(input_1))
    print(demo.subsets3(input_1))
