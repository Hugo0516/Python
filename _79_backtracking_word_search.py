from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word, 0):
                    return True
        return False

    def helper(self, board, i, j, word, wordIndex):
        if wordIndex == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[wordIndex] != board[i][j]:
            # i<0, j<0 的情況表示超出[]的範圍(EX: i=-1, j=-1 or i=5, j=5)
            return False

        board[i][j] = "#"   # to avoid the same letter be used more than once

        forund = self.helper(board, i + 1, j, word, wordIndex + 1) \
                 or self.helper(board, i, j + 1, word, wordIndex + 1) \
                 or self.helper(board, i, j - 1, word, wordIndex + 1) \
                 or self.helper(board, i - 1, j, word, wordIndex + 1)
        board[i][j] = word[wordIndex]   # 因為上面把它變成#, 所以要把它變回來

        return forund

    # def exist(self, board, word):
    #     """
    #     :type board: List[List[str]]
    #     :type word: str
    #     :rtype: bool
    #     """
    #     for y in range(len(board)):
    #         for x in range(len(board[0])):
    #             if self.exit(board, word, x, y, 0):
    #                 return True
    #     return False
    #
    # def exit(self, board, word, x, y, i):
    #     if i == len(word):
    #         return True
    #     if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
    #         return False
    #     if board[y][x] != word[i]:
    #         return False
    #     board[y][x] = board[y][x].swapcase()
    #     isexit = self.exit(board, word, x + 1, y, i + 1) or \
    #              self.exit(board, word, x, y + 1, i + 1) or \
    #              self.exit(board, word, x - 1, y, i + 1) or \
    #              self.exit(board, word, x, y - 1, i + 1)
    #
    #     board[y][x] = board[y][x].swapcase()
    #     return isexit


"""
    經典題目！！！！
    method 1比較好：
    https://www.youtube.com/watch?v=1zSg1WdmhIs
    
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79386066
"""

if __name__ == '__main__':
    demo = Solution()

    input_1 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    word_1 = "ABCCED"
    word_2 = "SEE"
    word_3 = "ABCB"

    print(demo.exist(input_1, word_1))
    print(demo.exist(input_1, word_2))
    print(demo.exist(input_1, word_3))
