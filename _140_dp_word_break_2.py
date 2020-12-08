from typing import List
from collections import Counter


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # quick check on the characters,
        #   otherwise it would exceed the time limit for certain test cases.
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []

        wordSet = set(wordDict)
        print(set(Counter(s).keys()))
        print(set(Counter("".join(wordDict)).keys()))
        print(wordSet)

        # dp 第 1 個 = s 第 0 個
        dp = [[]] * (len(s) + 1)
        dp[0] = [""]  # dp, initialize
        # 如果沒有 initialize,  #28會吃不到

        for endIndex in range(1, len(s) + 1):  # 上面 initialize, 所以從 1 開始
            sublist = []
            # fill up the values in the dp array.
            for startIndex in range(0, endIndex):
                word = s[startIndex:endIndex]
                if word in wordSet:
                    for subsentence in dp[startIndex]:
                        sublist.append((subsentence + ' ' + word).strip())

            dp[endIndex] = sublist

        return dp[len(s)]


"""
We define an array called dp. 
Each element in the array (dp[i]) would be used to hold the solutions for the corresponding prefix s[0:i].
For example, for the prefix of s[0:3] = "cat", the value for the element of dp[3] would be ["cat"], as we indicated in the previous graph.

"""

if __name__ == '__main__':
    demo = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(demo.wordBreak(s, wordDict))
