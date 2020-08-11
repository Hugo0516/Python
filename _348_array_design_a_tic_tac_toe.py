class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here
        """
        self.row, self.col, self.diag1, self.diag2, self.n = [0] * n, [0] * n, 0, 0, n
        # diag1 = 左上到右下斜, diag2 = 右上到左下斜

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            offset = 1
        else:
            offset = -1

        self.row[row] += offset
        self.col[col] += offset

        if row == col:
            self.diag1 += offset
        if row + col == self.n - 1:
            self.diag2 += offset

        if self.n in [self.row[row], self.col[col], self.diag1, self.diag2]:
            return 1
        if -self.n in [self.row[row], self.col[col], self.diag1, self.diag2]:
            return 2
        return 0

"""
    不用創建網格,只需記錄每個行、列和兩條對角線的下棋的值。
    對於每個下棋，對於玩家1的下棋賦值是1，對於玩家2的下棋賦值是-1。
    然後我們只需要檢查當前所在的行/列/對角線的下棋的值是否等於n或-n。
"""

"""
    Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

    TicTacToe toe = new TicTacToe(3);

    toe.move(0, 0, 1); -> Returns 0 (no one wins)
    |X| | |
    | | | |    // Player 1 makes a move at (0, 0).
    | | | |

    toe.move(0, 2, 2); -> Returns 0 (no one wins)
    |X| |O|
    | | | |    // Player 2 makes a move at (0, 2).
    | | | |

    toe.move(2, 2, 1); -> Returns 0 (no one wins)
    |X| |O|
    | | | |    // Player 1 makes a move at (2, 2).
    | | |X|

    toe.move(1, 1, 2); -> Returns 0 (no one wins)
    |X| |O|
    | |O| |    // Player 2 makes a move at (1, 1).
    | | |X|

    toe.move(2, 0, 1); -> Returns 0 (no one wins)
    |X| |O|
    | |O| |    // Player 1 makes a move at (2, 0).
    |X| |X|

    toe.move(1, 0, 2); -> Returns 0 (no one wins)
    |X| |O|
    |O|O| |    // Player 2 makes a move at (1, 0).
    |X| |X|

    toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
    |X| |O|
    |O|O| |    // Player 1 makes a move at (2, 1).
    |X|X|X|
    
    
    https://blog.csdn.net/danspace1/article/details/86616981
"""
