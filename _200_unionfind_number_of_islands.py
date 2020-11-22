from typing import List


class Solution:
    # DFS version
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or len(grid) == 0 or len(grid[0]) == 0:  # 注意這些條件的順序
            return 0

        m = len(grid)
        n = len(grid[0])
        ans = 0

        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    ans += 1  # 和 547 的改良很像
                    self.__dfs(grid, x, y, n, m)
        return ans

    def __dfs(self, grid, x, y, n, m):
        if x < 0 or y < 0 or x >= n or y >= m or grid[y][x] == '0':  # x >=n, y>=m, 是因為電腦都是從0開始
            return  # 邊界條件不滿足 or 這個點是水
        grid[y][x] = '0'  # 掃過之後就把該點變成水 當然你也可以改成其他數字
        self.__dfs(grid, x + 1, y, n, m)
        self.__dfs(grid, x - 1, y, n, m)
        self.__dfs(grid, x, y + 1, n, m)
        self.__dfs(grid, x, y - 1, n, m)


class Solution2:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[i][j] = "0"
        for dir in dirs:
            nr, nc = i + dir[0], j + dir[1]
            if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                if grid[nr][nc] == "1":
                    self.dfs(grid, nr, nc)


"""
    DFS or BFS or Connected Component(Disjoint Set)
    
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1
    
      x x x 
    y 
    y 
    y 
    
    用connected component 的思路下去想
    
    Hua Hua:
    Time Complexity: O(mn) / Space Complexity: O(mn)
    http://zxi.mytechroad.com/blog/searching/leetcode-200-number-of-islands/
"""
if __name__ == '__main__':
    demo = Solution()
    input_1 = grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    input_2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(demo.numIslands(input_1))
    print(demo.numIslands(input_2))
