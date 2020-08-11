from typing import List


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        dp = [[0 for j in range(c)] for i in range(r)]

        for i in range(c):
            if obstacleGrid[0][i] == 0:     # 遇到 obstacle 後面都一定為 False
                dp[0][i] = 1
            else:
                break
        for j in range(1, r):
            if obstacleGrid[j][0] == 0:
                dp[j][0] = 1
            else:
                break
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[r - 1][c - 1]



def main():

    obstacleGrid = [[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]
                    ]
    try_1 = Solution()
    print(obstacleGrid, obstacleGrid[0])
    print('')
    print(try_1.uniquePathsWithObstacles(obstacleGrid), end='')


if __name__ == '__main__':
    main()