from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass


class Solution2(object):
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        left_min = prices[0]
        right_max = prices[-1]

        length = len(prices)
        left_profits = [0] * length
        # pad the right DP array with an additional zero for convenience.
        right_profits = [0] * (length + 1)

        # construct the bidirectional DP array
        for l in range(1, length):
            left_profits[l] = max(left_profits[l - 1], prices[l] - left_min)
            left_min = min(left_min, prices[l])

            r = length - 1 - l
            right_profits[r] = max(right_profits[r + 1], right_max - prices[r])
            right_max = max(right_max, prices[r])

        max_profit = 0
        for i in range(0, length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])

        return max_profit


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        hold_1, sold_1, hold_2, sold_2 = float('-inf'), 0, float('-inf'), 0
        # hold1, 代表有"一"個股票在手中
        # hold_1 要為無限小, 因為#51, 我們若是設為0, 那hold_1會等於0, 但是這樣不對, 因為你不能有股票卻不用付任何錢!!!

        for price in prices:
            hold_1 = max(0 - price, hold_1)
            sold_1 = max(hold_1 + price, sold_1)
            hold_2 = max(sold_1 - price, hold_2)
            sold_2 = max(hold_2 + price, sold_2)

        return max(sold_1, sold_2)


"""
Solution 2: <Leetcode> Bi-directional DP
=> 我沒看

Solution 3: DP
Reference: https://www.youtube.com/watch?v=gsL3T9bI1RQ&t=833s

Time Complexity: O(n)
Space Complexity: O(1)

    hold1[k] = max(0-price[k], hold[k-1])
    sold1[k] = max(hold[k-1]+p, sold1[k-1])
    hold2[k] = max(sold[k-1]-p, hold2[k-1])
    sold2[k] = max(hold2[k-1]+p, sold2[k-1])
    => max(sold1, sold2)
    
*** 與714 ***
"""

if __name__ == '__main__':
    demo2 = Solution2()
    demo3 = Solution3()

    input_1 = [3, 3, 5, 0, 0, 3, 1, 4]
    print(demo2.maxProfit(input_1))
    print(demo3.maxProfit(input_1))
