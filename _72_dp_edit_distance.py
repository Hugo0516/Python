class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1, L2 = len(word1), len(word2)
        dp = [[0] * (L2 + 1) for i in range(L1 + 1)]

        for i in range(L1 + 1):
            dp[i][0] = i        # 做 insert 動作
        for j in range(L2 + 1):
            dp[0][j] = j        # 做 insert 動作
        for i in range(1, L1 + 1):
            for j in range(1, L2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    # 這一題跟 LeetCode 10. 很像，只是 10 的general case 是用 or
                    # 這裡是用 min 因為畢竟要求所有動作的最小值，所以用min合理
        return dp[L1][L2]


"""
    解題思路：
            
            Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
            You have the following 3 operations permitted on a word:
            Insert a character / Delete a character / Replace a character
            
            Input: word1 = "intention", word2 = "execution"
            Output: 5
            Explanation: 
            intention -> inention (remove 't')
            inention -> enention (replace 'i' with 'e')
            enention -> exention (replace 'n' with 'x')
            exention -> exection (replace 'n' with 'c')
            exection -> execution (insert 'u')
            
            https://www.youtube.com/watch?v=We3YDTzNXEk
"""


if __name__ == '__main__':
    sol = Solution()
    word_1 = "intention"
    word_2 = "execution"
    print(sol.minDistance(word_1, word_2))