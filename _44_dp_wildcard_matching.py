class Solution:

    def isMatch(self, s, p):
        m, n = len(s), len(p)
        # 狀態數組，表示從s的i到p的j是否可以匹配
        dp = [[False for j in range(n + 1)] for i in range(m + 1)]
        dp[0][0] = True
        # 當s為空時必須有*才可能滿足匹配，並且他的真值一定和去掉*及其前面的符號相同

        for j in range(1, n + 1):
            dp[0][j] = p[j - 1] == '*' and dp[0][j - 1]     # 注意一下，p = *a*b 的話, 因為a, b會破壞 match~~

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 當 p上一個字符為'？ '或者p上一個字符等於s上一個字符，則當前真值與上一位相同
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                # p上一個字符為'*'時，則*可表示p往後走一位或者s往後走一位
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        # 返回s[0->len(s)] 與 p[0->len(p)]的真值
        return dp[m][n]

"""
    解題思路：
            這題跟 LeetCode 10. 很像
            '?' Matches any single character.
            '*' Matches any sequence of characters (including the empty sequence).
            Input:
            s = "adceb"
            p = "*a*b"
            Output: true
            Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
            
            https://blog.csdn.net/L141210113/article/details/88613909
"""

if __name__ == '__main__':
    s1 = "adceb"
    p1 = "*a*b"
    sol = Solution()
    print(sol.isMatch(s1, p1), end='')
