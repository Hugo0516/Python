import itertools
from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        ops = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y}

        def ways(s):
            ans = []
            for i in range(len(s)):
                if s[i] in "+-*":
                    ans += [ops[s[i]](l, r) for l, r in itertools.product(ways(s[0:i]), ways(s[i + 1:]))]
                    # itertool.product, 即為笛卡兒積的 library
            if not ans:
                ans.append(int(s))
            return ans

        return ways(input)


class Solution2:
    def diffWaysToCompute(self, inp):
        def helper(l, r):
            ans = []
            for i in range(l, r):
                if inp[i] not in ops:
                    continue
                ans += [ops[inp[i]](le, ri) for le in helper(l, i)
                        for ri in helper(i + 1, r)]
            return ans if len(ans) != 0 else [int(inp[l:r])]

        ops = {
            '-': lambda x, y: x - y,
            '+': lambda x, y: x + y,
            '*': lambda x, y: x * y,
        }
        return helper(0, len(inp))


"""
解題思路： 記憶化遞歸 
記憶化遞歸 和 迪卡兒積
=> sol1 and sol2 都沒有用到 dp, 所以若是 input 太大, 就會跑不出來

Sol 1: Hua Hua
Sol 2: Leetocde 路人

sol 1 比 sol 2快, 但是所用到的方法都是一樣的, 所以我猜是因為 itertool 有做優化
https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66428/Python-recursive-solution.-Easy-understand

Time Complexity:
Space Complexity: 
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "2-1-1"
    input_2 = "2*3-4*5"

    print(demo.diffWaysToCompute(input_1))
    print(demo.diffWaysToCompute(input_2))
