from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Mark the round / level, _i.e_ the ticker of timestamp
        # this is like an anchor make us know this current round is finished
        queue.append((-1, -1))

        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # We finish one round of processing
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                # then it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1


class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Step 2). start the rotting process via BFS
        minutes_elapsed = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            tmp = fresh_oranges
            row, col = queue.popleft()
            # this is a rotten orange
            # then it would contaminate its neighbors

            for d in directions:
                neighbor_row, neighbor_col = row + d[0], col + d[1]
                if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                    if grid[neighbor_row][neighbor_col] == 1:
                        # this orange would be contaminated
                        grid[neighbor_row][neighbor_col] = 2
                        fresh_oranges -= 1
                        # this orange would then contaminate other oranges
                        queue.append((neighbor_row, neighbor_col))

            if tmp != fresh_oranges:
                minutes_elapsed += 1

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1


"""
*** 這題要注意的點: 酸然一看會是覺得典型 BFS 題型, 但是你會發現一輪當中會有多個 rotten orange,
    而我們不能說從一個 rotten orange 開始就 minutes+1, 這樣子不對, 這也是為什麼我寫的 solution2 錯
*** 

Time Complexity:
Space Complexity:
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(demo.orangesRotting(input_1))

    input_1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    demo2 = Solution2()
    print(demo2.orangesRotting(input_1))

    input_2 = [[1, 2, 1, 1, 2, 1, 1]]
    print(demo2.orangesRotting(input_2))