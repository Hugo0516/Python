from functools import lru_cache


class Solution:

    # recursive method & top down
    def numDecodings1(self, s: str) -> int:
        @lru_cache(None)
        def helper(n):
            if n == 0:
                return 1
            ans = 0
            if n >= 1 and s[n - 1] != '0':
                ans += helper(n - 1)
            if n >= 2 and 10 <= int(s[n - 2:n]) <= 26:
                ans += helper(n - 2)
            return ans

        return helper(len(s))

    # top down & dp approach 有兩個缺點：
    # Space Complexity: O(n)
    # 1. 還是有recursion, 但是其實不需要，以減省call stack 的呼叫
    # 2. 其實 f(n) 只與 f(n-1) f(n-2) 有關係，所以根本就不需要去存O(n) 的 memory， 因為只需要知道前一個和前前一個就夠了

    def numDecodings2(self, s: str) -> int:
        dp = [-1 for i in range(len(s) + 1)]
        dp[0] = 1   # s 為空字串，所以直接環傳一種方法
        def helper(n):
            if dp[n] != -1:
                return dp[n]
            ans = 0
            if n >= 1 and s[n - 1] != '0':
                ans += helper(n - 1)
            if n >= 2 and 10 <= int(s[n - 2:n]) <= 26:
                ans += helper(n - 2)
            dp[n] = ans
            return ans
        return helper(len(s))

    # bottom up approach
    # Time Complexity: O(n) / Space Complexity: O(1)

    def numDecodings3(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1 if s[0] != '0' else 0
        prev2 = 1
        prev1 = 1 if s[0] != '0' else 0
        for i in range(2, len(s) + 1):
            cur = 0
            if s[i-1] != '0':
                cur += prev1
            if 10 <= int(s[i-2:i]) <= 26:
                cur += prev2
            prev2 = prev1
            prev1 = cur
        return prev1

"""
    解題思路：
            Input: "12" / Output: 2 / Explanation: It could be decoded as "AB" (1 2) or "L" (12).
            recursive function?
            top down is more efficient than recursion
            bottom up is more efficient than top down
            however, top down is easier to figure out than bottom up
            
            @lru_cache 的用意就是讓電腦利用memory去儲存之前跑過的資料，其實這用意就像是你創一個DP array 去存跑過的資料這樣，
            所以其實第一種寫法 和 第二種寫法 是一樣的東西，用第二種寫法寫只是讓面試官了解你懂DP罷了  
            
            f(n) = decode ways of first n character
            
            Recursive and top down method:
            f(0) = 1
            f(n) = f(n-1) + f(n-2)
            f(n) = f(n-1)
            f(n) = f(n-2) (最後兩個數字是10, 因為 0 沒有好 decode)
            so:
                1, n = 0
                f(n-1) + f(n-2), else if n>=2 and if s[n-1]>0 and 10 <= s[n-2:n] <= 26
                f(n-1), else if n >= 1 and s[n-1] > 0 "32"
                f(n-2), else if n >= 2 and 10 <= s[n-2:n] <= 26 "10"
                0, otherwise "0"
                
            Bottom up approach:
            "2112" (ex: 211+2(f(n-1)) / 21+12(f(n-2))
            f(0) = 1
            f(1) = 1
            f(2) = f(0)((左邊數來)21符合條件) + f(1)((左邊數來)1符合條件) = 2
            f(3) = f(1) + f(2) = 1 + 2 = 3
            f(4) = f(2) + f(3) = 2 + 3 = 5
            "226"
            f(0) = 1 
            f(1) = 1 (2)
            f(2) = f(0) + f(1) = 2 (22 2+2)
            f(3) = f(1) + f(2) = 3 (2+26 22+6)            
            
            https://www.youtube.com/watch?v=hBwc-XtP8Mc&feature=youtu.be&fbclid=IwAR0ldz8mUeqey47uZ_yJtrglzR8MsUBYpMG_X9QL7EJX9nChLeHA6Mgzr0w
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "226"
    print(demo.numDecodings1(input_1))
