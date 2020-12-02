from typing import List


class Solution:
    # Brute Force
    def maxProfit(self, prices: List[int]) -> int:
        # [7, 1, 5, 3, 6, 4]
        max_profit = 0

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit

    # One Pass
    def maxProfit2(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit


"""
    Brute Force:
    Time Complexity: O(n(n-1)/2)
    Space Complexity: O(1)
    
    One Pass:
    Time Complexity: O(n)
    Space Complexity: O(1)
"""
if __name__ == '__main__':
    demo = Solution()
    input_1 = [7, 1, 5, 3, 6, 4]
    print(demo.maxProfit2(input_1))
