import itertools
from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = max_cost = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i - 1]:
                max_cost = 0
            res += min(max_cost, cost[i])
            max_cost = max(max_cost, cost[i])
        return res


"""
Approach 1: Greedy

Intuition
For a group of continuous same characters,
we need to delete all the group but leave only one character.

Explanation
For each group of continuous same characters,
we need cost = sum_cost(group) - max_cost(group)
=> 每一次都要貪心的把 max_cost 取出, 然後將其扣掉

Time Complexity: O(N)
Space Complexity: O(1)

https://www.youtube.com/watch?v=n6fUMuVS-X8
https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/discuss/831588/JavaC%2B%2BPython-Straight-Forward

不是很好懂= =

"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "abaac"
    cost_1 = [1, 2, 3, 4, 5]
    input_2 = "abc"
    cost_2 = [1, 2, 3]
    input_3 = "aaaaabaaaaa"
    cost_3 = [1, 2, 5, 3, 4, 4, 1, 2, 3, 4, 5]

    print(demo.minCost(input_1, cost_1))
    print(demo.minCost(input_2, cost_2))
    print(demo.minCost(input_3, cost_3))
