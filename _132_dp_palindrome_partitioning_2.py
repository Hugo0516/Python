class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # valid[i][j] = 1 if s[i~j] is palindrome, otherwise 0
        # valid 像是在做預處理, 會預先給1, 是因為單個字元本身為回文
        valid = [[1 for i in range(n)] for i in range(n)]

        # dp[i] = min cuts of s[0~i], 其實裡面不該放n, 應該要放n-1, 因為最大切割數不可能=n
        dp = [n] * n

        # 這裡的 for 就是在做預處理的動作
        for l in range(2, n + 1):
            i = 0
            j = i + l - 1
            while j < n:
                # EX: valid[0][1] = s[0] == s[1] and valid[1][0]
                # => 回文: 從左往右看 or 從右往左看 都一樣
                valid[i][j] = s[i] == s[j] and valid[i + 1][j - 1]
                i += 1
                j += 1

        for i in range(n):
            if valid[0][i]:
                # valid = 1, 代表是回文 => 不用切割
                dp[i] = 0
                continue
            for j in range(i):
                if valid[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n - 1]


"""
思路：首先想到這是一題優化的問題, 所以你要想到 DFS / DP, 但是因為他沒數據規模, 如果數據規模 > 20, 那麼使用DFS的話,
速度就會變太慢, 因此我們選擇 DP(因為也有非常明顯的子問題結構)

Since length is unknown => DP
(Hua Hua)

Transfer function:
dp[i] = min cuts of s[0~i]
dp[i] = min{dp[j] + 1} if s[j+1~i] is a palindrome.
*** dp 是看 cut 數目, valid 是看是否為回文 ***
=> 所以要先確認 valid 再確認 dp

Time Complexity: O(n^2), #12-18 => O(n^2)
Space Complexity: O(n^2), #6 => O(n^2)
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "aab"
    input_2 = "a"
    input_3 = "ab"
    input_4 = "cabababcbc"
    print(demo.minCut(input_1))
    print(demo.minCut(input_2))
    print(demo.minCut(input_3))
    print(demo.minCut(input_4))
