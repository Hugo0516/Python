class Solution:
        def minPathSum(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            n = len(grid)
            m = len(grid[0])
            for i in range(1, n):
                grid[i][0] = grid[i-1][0] + grid[i][0]

            for j in range(1, m):
                grid[0][j] = grid[0][j-1] + grid[0][j]

            for i in range(1, n):
                for j in range(1, m):
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
            return grid[n-1][m-1]

"""
    解題思路：
            跟經典DP題目一樣，只是最後DP的轉移方程式前面要加 min 畢竟是求 minimum path 所以要記得想!!
"""

    # def minPathSum(self, grid):
    #     if not len(grid) or not len(grid[0]):
    #         return 0
    #
    #     m, n, cache = len(grid) - 1, len(grid[0]) - 1, {}
    #
    #     return self.findMinSum(grid, m, n, cache)
    #
    # def findMinSum(self, grid, m, n, cache):
    #     if (m, n) in cache:
    #         return cache[(m, n)]
    #     elif m < 0 or n < 0:
    #         return float('inf')
    #     elif m == 0 and n == 0:
    #         return grid[0][0]
    #     else:
    #         cache[(m, n)] = grid[m][n] + min(self.findMinSum(grid, m - 1, n, cache),
    #                                          self.findMinSum(grid, m, n - 1, cache))
    #
    #         return cache[(m, n)]


def main():
    grid_1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    grid = Solution()

    print(grid.minPathSum(grid_1))

    print(ord('1'), ord('0'))


if __name__ == '__main__':
    main()
