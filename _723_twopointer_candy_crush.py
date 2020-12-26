from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])
        todo = False

        # CRASH ROWS
        for r in range(R):
            for c in range(C - 2):
                if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:
                    board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])
                    todo = True

        # CRASH COLUMNS
        for r in range(R - 2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:
                    board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(board[r][c])
                    todo = True

        # CRASH GRAVITY
        # two pointer
        # falling 的部分, 這邊我們要用的視角和上面兩個 step 不一樣,
        # 這邊我們要從 下到上 左到右
        for c in range(C):  # 做一個降落的操作
            wr = R - 1      # 為一個 write pointer, 表示下一個可以 crash 的地方, 表這個後面都為 '實'
            for r in range(R - 1, -1, -1):  # r為一個 read pointer, 從下往上看, 要保證下面是 "實", 上面是 '0'
                # wr 和 r, 都是由下往上走
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0

        return self.candyCrush(board) if todo else board


"""
Approach #1: Ad-Hoc

Gravity Step

For each column, we want all the candy to go to the bottom. 
One way is to iterate through and keep a stack of the (uncrushed) candy, 
popping and setting as we iterate through the column in reverse order.

Alternatively, we could use a sliding window approach, maintaining a read and write head. 
As the read head iterates through the column in reverse order, when the read head sees candy, 
the write head will write it down and move one place. 
Then, the write head will write zeroes to the remainder of the column.

We showcase the simplest approaches to these steps in the solutions below.

*** 這一題 要搭配圖下去看, 才比較好理解解法 !!! ***

Time Complexity: O( (R*C)^2 ), where R,C is the number of rows and columns in board. 
We need O(R∗C) to scan the board, and we might crush only 3 candies repeatedly.

Space Complexity: O(1), additional complexity, as we edit the board in place.

"""

if __name__ == '__main__':
    demo = Solution()
    board = [[110, 5, 112, 113, 114],
             [210, 211, 5, 213, 214],
             [310, 311, 3, 313, 314],
             [410, 411, 412, 5, 414],
             [5,     1, 512, 3,   3],
             [610,   4, 1, 613, 614],
             [710,   1, 2, 713, 714],
             [810,   1, 2,   1,   1],
             [1,     1, 2,   2,   2],
             [4,     1, 4, 4, 1014]]

    print(demo.candyCrush(board))
