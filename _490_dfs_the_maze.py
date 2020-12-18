from typing import List


class Solution:
    # iteration version
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n, visit = len(maze), len(maze[0]), set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        stack = [start]
        while stack:
            curx, cury = stack.pop()
            if [curx, cury] == destination:
                return True
            for dirx, diry in directions:
                tx, ty = curx, cury
                while 0 <= tx + dirx < m and 0 <= ty + diry < n and not maze[tx + dirx][ty + diry]:
                    tx, ty = tx + dirx, ty + diry
                if (tx, ty) not in visit:
                    visit.add((tx, ty))
                    stack.append((tx, ty))
        return False


class Solution2:
    def hasPath(self, maze, start, destination):
        m, n, stopped = len(maze), len(maze[0]), set()

        def dfs(x, y):
            if (x, y) in stopped:
                return False

            stopped.add((x, y))
            if [x, y] == destination:
                return True

            for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
                newX, newY = x, y
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                if dfs(newX, newY):
                    return True

            return False

        return dfs(*start)


"""
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Reference:
Sol 1: https://maxming0.github.io/2020/08/24/The-Maze/
Sol 2: https://leetcode.com/problems/the-maze/discuss/150523/Python-elegant-DFS-solution

Time Complexity: DFS complexity is O(|V|+|E|). In our maze, O(|V|) = O(|E|) = m * n. So time complexity is O(mn).
Space Complexity: O(mn)
"""

if __name__ == '__main__':
    demo = Solution()
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [4, 4]
    print(demo.hasPath(maze, start, destination))
