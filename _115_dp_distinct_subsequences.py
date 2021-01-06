class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # Dictionary for memoization
        memo = {}

        def uniqueSubsequences(i, j):

            M, N = len(s), len(t)

            # Base case
            if i == M or j == N or M - i < N - j:
                return int(j == len(t))

            # Check if the result is already cached
            if (i, j) in memo:
                return memo[i, j]

            # Always make this recursive call
            ans = uniqueSubsequences(i + 1, j)

            # If the characters match, make the other
            # one and add the result to "ans"
            if s[i] == t[j]:
                ans += uniqueSubsequences(i + 1, j + 1)

            # Cache the answer and return
            memo[i, j] = ans
            return ans

        return uniqueSubsequences(0, 0)


class Solution2:
    def numDistinct(self, s: str, t: str) -> int:

        M, N = len(s), len(t)

        # Dynamic Programming table
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)]

        # Base case initialization
        for j in range(N + 1):
            dp[M][j] = 0

        # Base case initialization
        for i in range(M + 1):
            dp[i][N] = 1

        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):

                # Remember, we always need this result
                dp[i][j] = dp[i + 1][j]

                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]


class Solution3:
    def numDistinct(self, s: str, t: str) -> int:

        M, N = len(s), len(t)

        # Dynamic Programming table
        dp = [0 for j in range(N)]

        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):

            # At each step we start with the last value in
            # the row which is always 1. Notice how we are
            # starting the loop from N - 1 instead of N like
            # in the previous solution.
            prev = 1

            for j in range(N - 1, -1, -1):

                # Record the current value in this cell so that
                # we can use it to calculate the value of dp[j - 1]
                old_dpj = dp[j]

                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[j] += prev

                # Update the prev variable
                prev = old_dpj

        return dp[0]


class Solution4:
    def numDistinct(self, s: str, t: str) -> int:
        ls = len(s)
        lt = len(t)
        dp = [[0 for i in range(ls + 1)] for j in range(lt + 1)]

        for i in range(ls + 1):
            dp[0][i] = 1

        for i in range(1, lt + 1):
            for j in range(1, ls + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] if s[j - 1] == t[i - 1] else dp[i][j - 1]

        return dp[lt][ls]


class Solution5:
    def numDistinct(self, s: str, t: str) -> int:
        l1, l2 = len(s) + 1, len(t) + 1
        cur = [0] * l2
        cur[0] = 1

        for i in range(1, l1):
            pre = cur[:]
            for j in range(1, l2):
                cur[j] = pre[j] + pre[j - 1] * (s[i - 1] == t[j - 1])
        return cur[-1]


"""
Approach 4:     *** Remember this one ***
解題思路：
Reference: Hua Hua =>
dp[i][j] = num of subseq of S[1:j] equals T[1:i]

*** 注意 ***, 因為是 num of subseq of s[1:j] => 是 t 要去比對 s, 所以 s 的部分才可以決定捨棄與否
=> 代表我們只能用 dp[?][j-1] 這樣!!!!

Initial: dp[0][*] = 1
Transition:
            if t[i] == s[j]:
                dp[i][j] = dp[i-1][j-1] # match s[j], t[i]
                         + dp[i][j-1] # skip s[j]
            else:
                dp[i][j] = dp[i][j-1]   # skip s[j]
Ans: dp[|T|][|S|] (表 T 的長度 和 S 的長度)

Time Complexity: O(n^2)
Space Complexity: O(n^2) -> 可以縮減到 O(n)

Approach 5: DP with O(n) space

Reference: https://leetcode.com/problems/distinct-subsequences/discuss/37322/Python-dp-solutions-(O(m*n)-O(n)-space).

--------------------------------------  Below is Leetcode provided.
Approach 1: Recursion + Memoization

Time Complexity: O(M*N), M and N represent the lengths of the two strings.
Space Complexity: O(M*N), The maximum space is utilized by the dictionary that 
we are using and the size of that dictionary would also be controlled by 
the total possible combinations of i and j which turns out to be O(M×N) as well. 

Approach 2: Iterative Dynamic Programming

Time Complexity: O
Space Complexity: O

Approach 3: Space optimized Dynamic Programming

Time Complexity: O(M*N)
Space Complexity: O(N)

"""
if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()
    demo3 = Solution3()

    s = "rabbbit"
    t = "rabbit"
    print(demo2.numDistinct(s, t))  # 3

    s2 = "babgbag"
    t2 = "bag"
    print(demo3.numDistinct(s2, t2))  # 5

    demo4 = Solution4()
    print(demo4.numDistinct(s, t))
