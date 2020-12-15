from typing import List
from functools import lru_cache
import copy


class Solution1:
    def minCost(self, costs):

        def paint_cost(n, color):
            if (n, color) in self.memo:
                return self.memo[(n, color)]

            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0:
                total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
            elif color == 1:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
            else:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            self.memo[(n, color)] = total_cost
            return total_cost

        if costs == []:
            return 0

        self.memo = {}
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))


# In Python, we can use the lru_cache decorator from the functools package.
class Solution2:
    def minCost(self, costs):

        @lru_cache(maxsize=None)
        def paint_cost(n, color):
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0:
                total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
            elif color == 1:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
            else:
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            return total_cost

        if costs == []:
            return 0

        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))


class Solution3:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0

        for n in range(len(costs) - 2, -1, -1):
            # Total cost of painting nth house red.
            costs[n][0] += min(costs[n + 1][1], costs[n + 1][2])
            # Total cost of painting nth house green.
            costs[n][1] += min(costs[n + 1][0], costs[n + 1][2])
            # Total cost of painting nth house blue.
            costs[n][2] += min(costs[n + 1][0], costs[n + 1][1])

        return min(costs[0])  # Return the minimum in the first row.


class Solution4:
    def minCost(self, costs: List[List[int]]) -> int:

        if len(costs) == 0:
            return 0

        previous_row = costs[-1]
        for n in reversed(range(len(costs) - 1)):
            current_row = copy.deepcopy(costs[n])
            # Total cost of painting nth house red?
            current_row[0] += min(previous_row[1], previous_row[2])
            # Total cost of painting nth house green?
            current_row[1] += min(previous_row[0], previous_row[2])
            # Total cost of painting nth house blue?
            current_row[2] += min(previous_row[0], previous_row[1])
            previous_row = current_row

        return min(previous_row)


"""
Input: costs = [[17,2,17],
                [16,16,5],
                [14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.

Approach 1: <Memoization>
Approach 2: <Memoization> 的 python 用 functool 改良版
Time Complexity: O(n)
Space Complexity: O(n)

Approach 3: <DP>
Time Complexity: O(n)
Space Complexity: O(1)

Approach 4: <DP>, with less space complexity

Dynamic programming is iterative, unlike memoization, which is recursive.
Problems that have optimal substructure can be solved with greedy algorithms. 
If they also have overlapping subproblems, then they can be solved with dynamic programming algorithms.


"""

if __name__ == '__main__':
    demo = Solution1()
    input_1 = [[17, 2, 17],
               [16, 16, 5],
               [14, 3, 19]]

    input_2 = []
    input_3 = [[7, 6, 2]]
    print(demo.minCost(input_1))
    print(demo.minCost(input_2))
    print(demo.minCost(input_3))

    demo2 = Solution2()
    demo3 = Solution3()
    print(demo2.minCost(input_1))
    print(demo3.minCost(input_1))
