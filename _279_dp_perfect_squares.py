import math


class Solution(object):
    def numSquares(self, n: int) -> int:

        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]

        dp = [float('inf')] * (n + 1)
        # bottom case
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                x, y = dp[i], dp[i - square]
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]


class Solution2:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(0, n + 1):
            for j in range(1, int(math.sqrt(n)) + 1):
                if i + j * j <= n:
                    dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)

        return dp[-1]


"""
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Time Complexity: O(n * n^1/2 ,  
In main step, we have a nested loop, where the outer loop is of n iterations 
and in the inner loop it takes at maximum n^(1/2) iterations.

Space Complexity: O(n), We keep all the intermediate sub-solutions in the array dp[]. 

DP 問題, 最重要的就是定義！！！！, 定義也是最難想出來的!!!! = =
定義想出來之後還要給予適當的初始值 = =

我們定義dp[i]為整數i最少能分解成多少個正整數的平方和。那麼有，

dp[i + j * j] = min(dp[i + j * j], dp[i] + 1).

如果一個數x可以表示為一個任意數a加上一個平方數bｘb，也就是x=a+bｘb，
那麼能組成這個數x最少的平方數個數，就是能組成a最少的平方數個數加上1（因為b*b已經是平方數了）。

"""

if __name__ == '__main__':
    demo = Solution()
    print(demo.numSquares(12))

    demo2 = Solution2()
    print(demo2.numSquares(12))
