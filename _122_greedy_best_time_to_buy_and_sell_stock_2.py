from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total += prices[i] - prices[i - 1]

        return total


"""

Time Complexity: O(n), single pass
Space Complexity: O(1), constant space needed

"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 7, 2, 3, 6, 7, 6, 7]
    print(demo.maxProfit(input_1))
