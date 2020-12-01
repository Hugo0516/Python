import collections
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1

        m, n = len(forest), len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:    # make sure it is not zero
                    trees.append((forest[i][j], i, j))  # 存tuple

        trees = sorted(trees)  # sorted tree by height
        count = 0
        sx, sy = 0, 0
        # Move from current position to next tree to cut
        for height, x, y in trees:
            step = self.BFS(forest, sx, sy, x, y)
            if step == -1:
                return -1
            else:
                count += step
                forest[x][y] = 1  # cut the tree
                sx, sy = x, y
        return count

    # min steps to go from (sx, sy) to (tx, ty) based on current map
    #
    def BFS(self, forest, sx, sy, tx, ty):
        m, n = len(forest), len(forest[0])

        visited = [[False for j in range(n)] for i in
                   range(m)]  # [[False, False, False], [False, False, False], [False, False, False]]
        _queue = collections.deque()
        step = -1
        _queue.append((sx, sy))

        while len(_queue) > 0:
            size = len(_queue)
            step += 1
            for i in range(size):
                x, y = _queue.popleft()
                visited[x][y] = True
                if x == tx and y == ty:
                    return step
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or forest[nx][ny] == 0 or visited[nx][ny]:
                        continue
                    _queue.append((nx, ny))
        return -1


"""
    Reference: Hua Hua
    
    這種格子題目很適合 BFS (因為最短路徑)
    Time Complexity: O(mn *mn) = O(m^2 n^2)
    Space Complexity: O(mn)
     
    python, 不會過, input太大, python跑不完 = =
"""

demo = Solution()
input_1 = [
    [1, 2, 3],
    [0, 0, 4],
    [7, 6, 5]
]

input_2 = [
    [1, 2, 3],
    [0, 0, 0],
    [7, 6, 5]
]

input_3 = [
    [3, 4, 5],
    [0, 0, 6],
    [2, 8, 7]
]

print(demo.cutOffTree(input_1))
print(demo.cutOffTree(input_2))
print(demo.cutOffTree(input_3))
