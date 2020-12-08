from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def could_place(row, col):
            return not (cols[col] + dale_diagonals[row - col] + hill[row + col])
            # 只要 cols, dale, hill 其中一個不為0, 那麼就不能擺放這個位置

        def place_queen(row, col):
            # 將他們設為1, 表示已經被佔據
            queens.add((row, col))
            cols[col] = 1
            dale_diagonals[row - col] = 1
            hill[row + col] = 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            dale_diagonals[row - col] = 0
            hill[row + col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                # 為了完美顯示在[] 裡面, 需要思考一下如何擺放
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        def backtrack(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        dale_diagonals = [0] * (2 * n - 1)
        hill = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output


"""
To backtrack. That means to come back, to change the position of the previously placed queen and try to proceed again.
If that would not work either, backtrack again.

For all "hill" diagonals row + column = const, (右上到左下)
and for all "dale" diagonals row - column = const. (左上到右下)

Time Complexity: O(N!), There is N possibilities to put the first queen, 
not more than N (N - 2) to put the second one, not more than N(N - 2)(N - 4) for the third one etc. 
In total that results in O(N!) time complexity.

Space Complexity: O(N) to keep an information about diagnoals and rows

** if we use brute force => Time Complexity: O(N^N)

Input: n = 4
Output: [[".Q..",
          "...Q",
          "Q...",
          "..Q."],
        ["..Q.",
         "Q...",
         "...Q",
         ".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
    
Input: n = 1
Output: [["Q"]]

"""

if __name__ == '__main__':
    demo = Solution()
    print(demo.solveNQueens(4))
    print(demo.solveNQueens(1))
