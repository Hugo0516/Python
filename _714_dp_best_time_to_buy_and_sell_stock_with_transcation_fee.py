from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, sold = float('-inf'), 0

        for i in range(len(prices)):
            p = prices[i]

            hold = max(hold, sold - p)
            sold = max(sold, hold + p - fee)
        return sold


"""
Time Complexity: O(N), where N is the number of prices
Space Complexity: O(1), the space used by hold and sold
*** 與123 ***
"""

if __name__ == '__main__':
    demo = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2

    print(demo.maxProfit(prices, fee))
