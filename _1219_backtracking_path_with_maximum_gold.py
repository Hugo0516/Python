from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # Given a row and a column, what are all the neighbours?
        def options(row, col):
            if row > 0:
                yield (row - 1, col)
            if col > 0:
                yield (row, col - 1)
            if row < len(grid) - 1:
                yield (row + 1, col)
            if col < len(grid[0]) - 1:
                yield (row, col + 1)

        # Keep track of current gold we have, and best we've seen.
        self.current_gold = 0
        self.maximum_gold = 0

        def backtrack(row, col):

            # If there is no gold in this cell, we're not allowed to continue.
            if grid[row][col] == 0:
                return

            # Keep track of this so we can put it back when we backtrack.
            gold_at_square = grid[row][col]

            # Add the gold to the current amount we're holding.
            self.current_gold += gold_at_square

            # Check if we currently have the max we've seen.
            self.maximum_gold = max(self.maximum_gold, self.current_gold)

            # Take the gold out of the current square.
            grid[row][col] = 0

            # Consider all possible ways we could go from here.
            for neigh_row, neigh_col in options(row, col):
                # Recursively call backtrack to explore this way.
                backtrack(neigh_row, neigh_col)

            # Once we're done on this path, backtrack by putting gold back.
            self.current_gold -= gold_at_square
            grid[row][col] = gold_at_square

        # Start the search from each valid starting location.
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                backtrack(row, col)

        # Return the maximum we saw.
        return self.maximum_gold


"""
Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

Reference: https://leetcode.com/problems/path-with-maximum-gold/discuss/398359/Python-backtracking-approach-with-comments.

Time Complexity:
Space Complexity: 
"""

if __name__ == '__main__':
    demo = Solution()
    grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
    print(demo.getMaximumGold(grid))
