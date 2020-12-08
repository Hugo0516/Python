from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        print(s)
        print(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDictSet:
                    dp[i] = True
                    print(dp)
                    print()

        return dp[len(s)]  # dp.pop()


"""
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

We also use two index pointers i and j, 
where i refers to the length of the substring (s′) considered currently starting from the beginning, 
and j refers to the index partitioning the current substring (s ′) 
into smaller substrings (0,j) and (j+1,i). 

To fill in the dp array, we initialize the element dp[0] as true,
since the null string is always present in the dictionary,
and the rest of the elements of dp as false. 

We consider substrings of all possible lengths starting from the beginning by making use of index i.
For every such substring, we partition the string into two further substrings s1 ' and s2′ 
in all possible ways using the index j (Note that the i now refers to the ending index of s2′ ). 

Now, to fill in the dp[i], we check if the dp[j] contains true, 
i.e. if the substring s1 ′ fulfills the required criteria. If so, we further check if s2′ is present in the dictionary. 
If both the strings fulfill the criteria, we make dp[i] as true, otherwise as false.

其實這個題和416. Partition Equal Subset Sum很像的，都是兩重循環，
第一重循環判斷每個位置的狀態，內層循環判斷這個狀態能不能有前面的某個狀態+一個符合題目要求的條件得到。

Time Complexity: O(n^3), two nested loops and sllice computation
Space Complexity: O(n)


"""
if __name__ == '__main__':
    demo = Solution()
    s1 = "leetcode"
    dict_1 = ["leet", "code"]

    print(demo.wordBreak(s1, dict_1))
