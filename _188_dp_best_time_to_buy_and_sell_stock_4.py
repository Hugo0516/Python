import math
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # solve special cases
        if not prices or k == 0:
            return 0

        # 這個 if, 是和 Leetocde 122 一樣的寫法!!
        if 2 * k > n:
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            # for i, j in zip(prices[1:], prices[:-1]):
            #     res += max(0, i - j)
            return res

        # dp[i][used_k][ishold] = balance
        # ishold: 0 nothold, 1 hold
        dp = [[[-math.inf] * 2 for _ in range(k + 1)] for _ in range(n)]

        # set starting value
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]

        # fill the array
        for i in range(1, n):
            for j in range(k + 1):
                # transition equation
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                # you can't hold stock without any transaction
                if j > 0:
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        res = max(dp[n - 1][j][0] for j in range(k + 1))
        # j=0, 1, 2 => 第零次交易, 第一次, 第二次
        return res


class Solution2:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # solve special cases
        if not prices or k == 0:
            return 0

        # Leetcode 122 !!
        if 2 * k >= n:
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            # for i, j in zip(prices[1:], prices[:-1]):
            #     res += max(0, i - j)
            return res

        # dp[i][used_k][ishold] = balance
        # ishold: 0 nothold, 1 hold
        dp = [[[-math.inf] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

        # set starting value
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]
        dp[1][0][0] = 0
        dp[1][1][1] = -prices[0]
        # 沒有 62, 63 也可以 work

        # fill the array
        for i in range(1, n + 1):  # 第 1~n 天
            for j in range(k + 1):  # 第 0 ~ k次交易
                # transition equation
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
                # you can't hold stock without any transaction
                if j > 0:
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])

        res = max(dp[n][j][0] for j in range(k + 1))
        # j=0, 1, 2 => 第零次交易, 第一次, 第二次
        return res


"""
We can either store the dp results in a dict or an array. 
Array costs less time for accessing and updating than dict, so we always prefer an array when possible.

Because of three needed characteristics (day number, transaction number used, stock holding status), 
a three-dimensional array is our choice. 

We can use dp[day_number][used_transaction_number][stock_holding_status] to represent our states, 
where stock_holding_status is a 0/1 number representing whether you hold the stock or not.

The value of dp[i][j][l] represents the best profit we can have at the end of the i-th day, 
with jth transactions you make and l stocks you hold.
(只要一"買入", 就算一次 transaction)

The next step is finding out the so-called "transition equation", 
which is a method that tells you how to jump from one state to another.

We start with dp[0][0][0] = 0 and dp[0][0][1]=-prices[0], 
and our final aim is max of dp[n-1][j][0] from j=0 to j=k. 

Now, we need to fill out the entire array to find out the result. 
Assume we have gotten the results before day i, and we need to calculate the profit of day i. 
There are only four possible actions we can do on day i: 
1. keep holding the stock, 
2. keep not holding the stock, 
3. buy the stock, or 
4. sell the stock. 

The profit is easy to calculate.
=>
1. Keep holding the stock:
dp[i][j][1] = dp[i-1][j][1]
2. Keep not holding the stock:
dp[i][j][0] = dp[i-1][j][0]
3. Buying, when j > 0:
dp[i][j][1] = dp[i-1][j-1][0]
4. Selling
dp[i][j][0] = dp[i-1][j][1] + prices[i]

Therefore:
=>
dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])

There a few points you should notice from the code above:

Take care of the initial values in dp array. 
Generally, it's ok to initialize them to zero. 
However, in this case, we need to make them -inf to mark impossible situations, such as dp[0][0][1].

You can reverse the order of filling the dp array, 
with some modifications in the transition equation. For example, decreasing j instead of increasing it.

Some state-compressed method can be applied if you want. 
For example, we only need dp[i-1], when calculating dp[i], 
therefore we can delete other useless dp to save memory. 
Just using two arrays to storing dp[i-1] and dp[i] and refreshing them every iteration will do.

The code above is not the fastest because we prioritize the readability. 
It would be faster if you put the larger dimension in the inner array since it uses CPU cache more efficiently.

Time Complexity: O(nk) if 2k <= n, O(n) if 2k > n, where n is the length of the prices sequence, 
since we have two for-loop. 

Space Complexity: O(nk), without state-compressed, and O(k) with state-compressed, 
where n is the length of the prices sequence.

*** 關於 2k >= n 這個部分, 原本Leetocde official 是寫 2k > n, 但是我看了其他回覆, 我覺得 2k>=n 比較好

"""

if __name__ == '__main__':
    demo = Solution()
    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    prices_2 = [2, 4, 1]
    print(demo.maxProfit(k, prices))
    print(demo.maxProfit(k, prices_2))
