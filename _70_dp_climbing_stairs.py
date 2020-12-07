class Solution:

    # dp with table
    def climbStairs(self, n: int) -> int:
        # Definition: last step is one or two !!

        if n == 1:
            return 1

        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # 最後一次走一步 or 兩步

        return dp[n]

    # brute force
    def climbStairs2(self, n: int) -> int:

        def helper(i: int, n: int):
            if i > n:
                return 0
            if i == n:
                return 1
            return helper(i + 1, n) + helper(i + 2, n)

        return helper(0, n)

    def climbStairs3(self, n: int) -> int:
        first = 1
        second = 2
        third = 0

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return third


"""
DP題型： 常常問說, 這個問題有多少個解
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

DP:
Time Complexity: O(n)
Space Complexity: O(n)
這題根本就是 Fibonacci 一模一樣

Brute Force:
Time Complexity: O(2^n)
Space Complexity: O(n), the depth of the recursion tree can go up to n.

"""

if __name__ == '__main__':
    demo = Solution()
    print(demo.climbStairs(3))
