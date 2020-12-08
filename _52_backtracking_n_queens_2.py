class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        def is_not_under_attack(row, col):
            return not (rows[col] or hills[row - col] or dales[row + col])

        def place_queen(row, col):
            rows[col] = 1
            hills[row - col] = 1  # "hill" diagonals
            dales[row + col] = 1  # "dale" diagonals

        def remove_queen(row, col):
            rows[col] = 0
            hills[row - col] = 0  # "hill" diagonals
            dales[row + col] = 0  # "dale" diagonals

        def backtrack(row=0, count=0):
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack(row + 1, count)
                    remove_queen(row, col)
            return count

        rows = [0] * n
        hills = [0] * (2 * n - 1)  # "hill" diagonals
        dales = [0] * (2 * n - 1)  # "dale" diagonals
        return backtrack()


"""
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Input: n = 1
Output: 1

Time Complexity: O(N!), There is N possibilities to put the first queen, 
not more than N (N - 2) to put the second one, not more than N(N - 2)(N - 4) for the third one etc. 
In total that results in O(N!) time complexity.

Space Complexity: O(N) to keep an information about diagnoals and rows

** if we use brute force => Time Complexity: O(N^N)

參考 51 題
"""

if __name__ == '__main__':
    demo = Solution()
    print(demo.totalNQueens(4))
    print(demo.totalNQueens(1))