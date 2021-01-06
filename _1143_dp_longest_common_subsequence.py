class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        dp = [[0 for i in range(l1 + 1)] for j in range(l2 + 1)]
        res = float('-inf')

        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if text1[j - 1] == text2[i - 1] else max(dp[i][j - 1], dp[i - 1][j])
                res = max(res, dp[i][j])

        return res


"""
This is a nice problem, as unlike some interview questions, this one is a real-world problem! 
Finding the longest common subsequence between two strings is useful for checking the difference between two files (diffing). 
Git needs to do this when merging branches. 
It's also used in genetic analysis (combined with other algorithms) as a measure of similarity between two genetic codes.

By this point, it's hopefully clear that we're dealing with an optimization problem. We need to generate a common 
subsequence that has the maximum possible number of letters. Using our analogy of drawing lines between the words, 
we could also phrase it as maximizing the number of non-crossing lines. 

There are a couple of strategies we use to design a tractable (non-exponential) algorithm for an optimization problem.

Identifying a greedy algorithm Dynamic programming There is no guarantee that either is possible. Additionally, 
greedy algorithms are strictly less common than dynamic programming algorithms and are often more difficult to 
identify. However, if a greedy algorithm exists, then it will almost always be better than a dynamic programming one. 
You should, therefore, at least give some thought to the potential existence of a greedy algorithm before jumping 
straight into dynamic programming. 

The best way of doing this is by drawing an example and playing around with it. One idea could be to iterate through 
the letters in the first word, checking whether or not it is possible to draw a line from it to the second word (
without crossing lines). If it is, then draw the left-most line possible. 

Applying Dynamic Programming to a Problem

While it's very difficult to be certain that there is no greedy algorithm for your interview problem, 
over time you'll build up an intuition about when to give up. You also don't want to risk spending so long trying to 
find a greedy algorithm that you run out of time to write a dynamic programming one (and it's also best to make sure 
you write a working solution!). 

Besides, sometimes the process used to develop a dynamic programming solution can lead to a greedy one. So, 
you might end up being able to further optimize your dynamic programming solution anyway. 

Recall that there are two different techniques we can use to implement a dynamic programming solution; memoization 
and tabulation. 

Memoization is where we add caching to a function (that has no side effects). In dynamic programming, it is typically 
used on recursive functions for a top-down solution that starts with the initial problem and then recursively calls 
itself to solve smaller problems. Tabulation uses a table to keep track of subproblem results and works in a 
bottom-up manner: solving the smallest subproblems before the large ones, in an iterative manner. Often, people use 
the words "tabulation" and "dynamic programming" interchangeably. 

For most people, it's easiest to start by coming up with a recursive brute-force solution and then adding memoization 
to it. After that, they then figure out how to convert it into an (often more desired) bottom-up tabulated algorithm. 



Reference: https://www.youtube.com/watch?v=CEnb7Ho7TYc 

Time Complexity:
Space Complexity:
"""

if __name__ == '__main__':
    demo = Solution()
    text1 = "abcde"
    text2 = "ace"

    print(demo.longestCommonSubsequence(text1, text2))

    text3 = "ezupkr"
    text4 = "ubmrapg"
    print(demo.longestCommonSubsequence(text3, text4))
