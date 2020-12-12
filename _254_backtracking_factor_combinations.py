from functools import reduce
from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        self.dfs(self.factors(n)[1:-1], n, 0, [], res)
        # self.factors(n)[1:-1], [1:-1] 是因為題目限制 factors should be greater than 1 and less than n
        return res

    def dfs2(self, nums, n, index, path, res):
        tmp = reduce(lambda x, y: x * y, path, 1)
        if tmp > n:
            return  # backtracking
        if tmp == n and path:
            res.append(path)
            return  # backtracking
        for i in range(index, len(nums)):
            self.dfs2(nums, n, i, path + [nums[i]], res)

    # 上面的 dfs 可以改成這個寫法！！！！！
    def dfs(self, nums, n, index, path, res):
        tmp = reduce(lambda x, y: x * y, path, 1)
        if tmp > n:
            return  # backtracking
        if tmp == n and path:
            res.append(path[:])
            return  # backtracking
        for i in range(index, len(nums)):
            # path += [nums[i]]
            path.append(nums[i])
            # 31 32 行一樣功能, 可是在 28 就會不同功能哦
            self.dfs(nums, n, i, path, res)
            path.pop()

    def factors(self, n):
        res = []
        for i in range(1, n + 1):
            if n % i == 0:
                res.append(i)
        return res


"""
Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]

Reference: https://leetcode.com/problems/factor-combinations/discuss/68135/Python-backtracking-solution.

Time Complexity: O(N * 2^N), N is the length of nums variable
Space Complexity: O(N), N is the length of nums variable
"""

if __name__ == '__main__':
    demo = Solution()
    output_1 = demo.getFactors(27)
    print(output_1)
