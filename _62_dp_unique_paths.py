class Solution:

    def uniquePaths(self, m: int, n: int) -> int:

        if (m <= 0 or n <= 0):
            return False
        dp = [[1 for x in range(n)] for x in range(m)]
        #        min (dp[i][j] = dp[i-1][j] + dp[i][j-1])
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

"""
O(m*n) space complexity solution
"""


# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         if (m <= 0 or n <= 0):
#             return False
#
#         dp = [1 for x in range(n)]
#         #        min (dp[i][j] = dp[i-1][j] + dp[i][j-1])
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[j] = dp[j - 1] + dp[j]
#         return dp[-1]
#
# # O(n) space complexity solution

def main():
    m, n = 3, 2
    demo = Solution()
    print(demo.uniquePaths(m, n), end='')


if __name__ == '__main__':
    main()
