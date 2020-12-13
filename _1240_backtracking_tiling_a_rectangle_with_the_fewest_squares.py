import functools


class Solution:
    # brute force solution
    def tilingRectangle(self, n: int, m: int) -> int:
        self.n = n
        self.m = m
        board = [[0] * n for _ in range(m)]
        self.res = float('inf')
        self.dfs(board, 0)
        return self.res

    def dfs(self, board, count):
        if count >= self.res:
            return
        i, j = self.find_next(board)
        if i == -1 and j == -1:
            self.res = min(self.res, count)
            return
        max_length = self.find_max_length(board, i, j)
        for k in range(1, max_length + 1)[::-1]:
            self.assign(board, i, j, k, 1)
            self.dfs(board, count + 1)
            self.assign(board, i, j, k, 0)

    def assign(self, board, i, j, length, val):
        for row in range(i, i + length):
            for col in range(j, j + length):
                board[row][col] = val

    def find_max_length(self, board, i, j):
        max_length = 1
        while i + max_length - 1 < self.m and j + max_length - 1 < self.n:
            for row in range(i, i + max_length):
                if board[row][j + max_length - 1] != 0:
                    return max_length - 1
            for col in range(j, j + max_length):
                if board[i + max_length - 1][col] != 0:
                    return max_length - 1
            max_length += 1
        return max_length - 1

    def find_next(self, board):
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 0:
                    return i, j
        return -1, -1


class Solution2:
    def tilingRectangle(self, n: int, m: int) -> int:
        INF = m * n

        # I already have `state` filled. How many more squares do I need to build n * m?
        @functools.lru_cache(None)
        def dp(state):
            if n == min(state):
                return 0
            state = list(state)
            mn = min(state)
            start = state.index(mn)
            res = INF
            for end in range(start, m):
                if state[end] != mn:
                    break
                side = end - start + 1
                if mn + side > n:
                    break
                state[start: end + 1] = [mn + side] * side
                res = min(res, dp(tuple(state)))
            return res + 1

        if m > n:
            m, n = n, m
        return dp(tuple([0] * m))


class Solution3:
    def tilingRectangle(self, width, height):

        # use area_left as a heuristic function to eliminate unworthy search branches
        # remove the memo used to cache best usedCount obtained for each skyline state,
        # it seems that the collision is quite scarse compared to all the states we had to store.

        # The main idea is that, if there exists a solution,
        # we can always fill in the squares from bottom up.
        # That means any state during this "filling" process can
        # be encoded as a skyline (array of heights at each position)
        # NOTE
        # y = skyline[x] contributes a line at y, from x to x + 1. This eliminates
        # ambiguity at the edge, where there may be edges of 2 square at 1 x position.
        # e.g.
        # placing a 1x1 square at bottom left of 2x1 rectangle,
        # the skyline is [1, 0]

        # heuristic: given area left to be filled,
        # calculate the least number of squares that can sum up to it.
        # this will be the absolute lower bound for that area.
        # store the result for faster access
        total_area = width * height
        dp = [-1 for i in range(total_area + 1)]
        dp[0] = 0
        for i in range(1, total_area + 1):
            # try each possible k
            dp[i] = 1 + min(dp[i - k ** 2] for k in range(1, int(i ** 0.5) + 1))
        self.res = total_area

        def dfs(skyline, usedCount, area_left):
            # [List Int], Int, Int -> Void
            # - given state as skyline,
            # - the number of squares already used,
            # - area left to be filled
            # try to find the min square tiling
            # continuing from this point.

            # no need to search further if the best we can do with this path
            # is no better than the best result so far
            if usedCount + dp[area_left] >= self.res:
                return;

            # solution found iff skyline overlaps with the ceiling
            filled = True
            # the algorithm places squares at left first, so we consider heights only on right edge
            # minimum height and the position.
            min_pos = 0
            min_height = skyline[0]
            for pos in range(width):
                # not filled if any skyline doesn't touch the ceiling
                if (skyline[pos] < height):
                    filled = False
                # update lowest spot
                if (skyline[pos] < min_height):
                    min_pos = pos
                    min_height = skyline[pos]

            # already filled, another solution found.
            if filled:
                self.res = min(usedCount, self.res)
                return

            # try to fill the leftmost lowest void, find the maximum size of square
            # we can put there. end represents the x-coordinate of right edge
            # NOTE x = end is where the right edge of this newly placed square will be
            end = min_pos + 1;
            # in order to increment end:
            # - right edge stays in the rectangle
            # - bottom edge must have same height
            # - top edge stays in the rectangle
            while (end < width and \
                   skyline[end] == min_height and \
                   (end - min_pos + 1 + min_height) <= height):
                end += 1

            # try fill with larger square first, to exhaust more void
            # and potentially yield better search.
            for right_pos in range(end, min_pos, -1):
                # calcualte size of the square to be used
                sqr_height = right_pos - min_pos

                new_skyline = list(skyline)
                # increase the skyline at relavent positions
                for i in range(min_pos, right_pos):
                    new_skyline[i] += sqr_height
                # continue dfs from here.
                dfs(new_skyline, usedCount + 1, area_left - sqr_height * sqr_height)

        skyline = [0 for i in range(width)]
        dfs(skyline, 0, total_area)

        return self.res;

    # TODO more optimizations
    # - store only (start_x, height) tuples instead, instead of the entire skyline
    #   this is bascially compression. Hopefully saves memory and reduces iteration time.
    # - Use A* algorithm. DFS with heuristics may still dives to unworthy states first.


class Solution4:
    def tilingRectangle(self, width, height):
        n, m = width, height
        if n > m:
            return self.tilingRectangle(m, n)
        ans = n * m

        height = [0] * n

        def dfs(curr):
            if curr >= ans:
                return


"""

Approach 1: https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/discuss/414194/Python-backtrack-solution
Approach 2: https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/discuss/414260/8ms-Memorized-Backtrack-Solution-without-special-case!
Approach 3: https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/discuss/415423/No-magic-a-dfs-solution-with-heuristic

思路：這一題光看前面兩個圖, 你會想到說dp說不定可以, 但是實際上, 看到第三個圖你會發現有特例,
代表說, 你不能用子問題去求解問題, 因為就是有特例

所以有兩種思路：
1.一樣用 DP, 只是特例另外直接給出答案
2. 用 backtracking, 但是backtracking 的時間複雜度可能能會很大, 所以有可能沒辦法通過測資
但是在面試的時候, 沒差
"""

if __name__ == '__main__':
    demo = Solution()
    n1 = 2
    m1 = 3
    print(demo.tilingRectangle(n1, m1))

    n2 = 11
    m2 = 13
    print(demo.tilingRectangle(n2, m2))

    demo2 = Solution2()
    demo3 = Solution3()

    print(demo2.tilingRectangle(n2, m2))
    print(demo3.tilingRectangle(n2, m2))
