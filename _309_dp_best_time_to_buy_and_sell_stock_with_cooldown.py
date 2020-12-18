from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = float('-inf'), float('-inf'), 0

        for price in prices:
            # Alternative: the calculation is done in parallel.
            # Therefore no need to keep temporary variables
            # sold, held, reset = held + price, max(held, reset-price), max(reset, sold)

            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)

        return max(sold, reset)


"""
這題要畫 state machine !!!! 下去了解
Transfer function:
hold[i] = max(hold[i-1], rest[i-1] - prices[i])
sold[i] = hold[i-1] + prices[i]
rest[i] = max(rest[i-1], sold[i-1])

initial: rest[0] = sold[0] = 0, hold[0] = -infinity
ans: max(rest[i], sold[i])

Time Complexity: O(n)
Space Complexity: O(n) -> O(1)
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 2, 3, 0, 2]
    print(demo.maxProfit(input_1))
