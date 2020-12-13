from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # step 1). initialize the conditions for backtracking
        #   i.e. initial state and final state
        non_obstacles = 0
        start_row, start_col = 0, 0
        for row in range(0, rows):
            for col in range(0, cols):
                cell = grid[row][col]
                if cell >= 0:
                    non_obstacles += 1
                if cell == 1:
                    start_row, start_col = row, col

        # count of paths as the final result
        path_count = 0

        # step 2). backtrack on the grid
        def backtrack(row, col, remain):
            # we need to modify this external variable
            nonlocal path_count

            # base case for the termination of backtracking
            if grid[row][col] == 2 and remain == 1:
                # reach the destination
                path_count += 1
                return

            # mark the square as visited. case: 0, 1, 2
            temp = grid[row][col]
            grid[row][col] = -4
            remain -= 1  # we now have one less square to visit

            # explore the 4 potential directions around
            for ro, co in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row, next_col = row + ro, col + co

                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    # invalid coordinate
                    continue
                if grid[next_row][next_col] < 0:
                    # either obstacle or visited square
                    continue

                backtrack(next_row, next_col, remain)

            # unmark the square after the visit
            grid[row][col] = temp

        backtrack(start_row, start_col, non_obstacles)

        return path_count


"""
Whenever we see the context of grid traversal,
the technique of backtracking or DFS (Depth-First Search) should ring a bell.

Approach 1: Backtracking

Intuition

We can consider backtracking as a state machine, where we start off from an initial state,
each action we take will move the state from one to another,
and there should be some final state where we reach our goal.

As a result, let us first clarify the initial and the final states of the problem.

1. Initial State

There are different types of squares/cells in a grid.

There are an origin and a destination cell, which are not given explicitly.

Initially, all the cells are not visited.

2. Final State

We reach the destination cell, i.e. cell filled with the value 2.

We have visited all the non-obstacle cells, including the empty cells (i.e. filled with 0) and the initial cell (i.e. 1).

More specifically, 
we could summarise the steps to implement the backtracking algorithm for this problem in the following pseudo code.
=>>
    def backtrack(cell):
        1. if we arrive at the final state:
             path_count ++
             return

        2. mark the current cell as visited

        3. for next_cell in 4 directions:
             if next_cell is not visited and non-obstacle:
                 backtrack(next_cell)

        4. unmark the current cell
        
Here we would like to highlight some important design decisions we took in the above implementation. 
As one can imagine, with different decisions, one would have variations of backtracking implementations.

1. In-place Modification

This is an important technique that allows us to save some space in the algorithm.

In order to mark the cell as visited, often the case we use some matrix or hashtable with boolean values 
to keep track of the state of each cell, i.e. whether it is visited or not.

With the in-place technique, we simply assign a specific value to the cell in the grid, 
rather than creating an additional matrix or hashtable.

2. Boundary Check

There are several boundary conditions that we could check during the backtracking, 
namely whether the coordinate of a cell is valid or not and whether the current cell is visited or not.

We could do the checking right before we make the recursive call, or at the beginning of the backtrack function.

We decided to go with the former one, which could save us some recursive calls when the boundary check does not pass.
------------------------------------------------------------------------
Input: [
        [1,0,0,0],
        [0,0,0,0],
        [0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Input: [[0,1],
        [2,0]]
Output: 0
Explanation:
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Time Complexity: O( 3^N ) ~= O( 4 * 3^(N-1) )
Space Complexity: O( N )

Thanks to the in-place technique, we did not use any additional memory to keep track of the state.

On the other hand, we apply recursion in the algorithm, which could incur O(N) space in the function call stack.

Hence, the overall space complexity of the algorithm is O(N).

"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]]
    print(demo.uniquePathsIII(input_1))