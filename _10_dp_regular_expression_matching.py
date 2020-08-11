# class Solution(object):
#     def isMatch(self, text, pattern):
#         x = len(pattern) + 1
#         y = len(text) + 1
#         dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
#
#         dp[-1][-1] = True
#         for i in range(len(text), -1, -1):
#             for j in range(len(pattern) - 1, -1, -1):
#                 first_match = i < len(text) and pattern[j] in {text[i], '.'}
#                 if j + 1 < len(pattern) and pattern[j + 1] == '*':
#                     dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
#                 else:
#                     dp[i][j] = first_match and dp[i + 1][j + 1]
#
#         return dp[0][0]

class Solution:
    def isMatch(self, text: str, pattern: str):
        if text == '' or pattern == '':
            return False

        row, col = len(text), len(pattern)  # 11, 10
        dp = [[False for j in range(col + 1)] for i in range(row + 1)]
        dp[0][0] = True

        for j in range(1, col + 1):
            if pattern[j - 1] == '*':  # 因為題目規定 * 前面一定會接一個字 (initialization)
                dp[0][j] = dp[0][j - 2]

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if pattern[j - 1] == '.' or pattern[j - 1] == text[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[j - 1] == '*':
                    if pattern[j - 2] == text[i - 1] or pattern[j - 2] == '.':  # 這個條件會導致 ?* 表示成more sequence(0個或多個)
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]  # dp[i-1][j] 表示 text 比較長 pattern 比較短 所以 ?* 表多個,
                        # 而 dp[i][j-2] 表示 text 比較短 pattern 比較長 所以 ?* 表0個
                        # 就是因為 37 行的結果不知道是要表0個還是多個 所以用 or 有一個true就true
                    else:  # 這裡表 pattern[j-2] != text[i-1]
                        dp[i][j] = dp[i][j - 2]  # 跟 29 行一樣 ?* 是由前兩個所決定
        return dp[row][col]


"""
解題思路：
        往畫出dp表格那裡開始想，標準的dp表格，所以要想初始化的條件，
        然後再去拼湊出dp[i][j] = dp[i-1][j], dp[i][j-1], dp[i-1][j-1] 之類的互相關係
        中心思想是我們認為 dp[i][j] 是 matched!!!! 所以解題思路也是以dp[i-1][j], dp[i][j-1] 是matched的
        舉例：41行的 ?* 我認為一定會繼續matched ，所以就直接認為 dp[i][j] = dp[i][j-2]
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        
        Input:
        s = "aab"
        p = "c*a*b"
        Output: true
        Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
        
        https://www.youtube.com/watch?v=DqhPJ8MzDKM&t=620s
"""


# class Solution(object):
#     def isMatch(self, s, p, memo={("", ""): True}):
#         if not p and s:      return False
#         if not s and p:      return set(p[1::2]) == {"*"} and not (len(p) % 2)
#         if (s, p) in memo:    return memo[s, p]
#
#         char, exp, prev = s[-1], p[-1], 0 if len(p) < 2 else p[-2]
#         memo[s, p] = \
#             (exp == '*' and ((prev in {char, '.'} and self.isMatch(s[:-1], p, memo)) or self.isMatch(s, p[:-2], memo))) \
#             or \
#             (exp in {char, '.'} and self.isMatch(s[:-1], p[:-1], memo))
#         return memo[s, p]

def main():
    demo_1 = Solution()
    s = "mississippi"  # 11 位數
    p = "mis*is*p*."  # 9 位數
    s1 = 'ab'
    p1 = '.*c'
    s2 = 'aab'
    p2 = 'c*a*b'
    print(demo_1.isMatch(s1, p1))


if __name__ == '__main__':
    main()
