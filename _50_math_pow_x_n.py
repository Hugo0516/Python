class Solution:

    # brute force
    def myPow(self, x: float, n: int) -> float:
        N = n

        if N < 0:
            x = 1 / x
            N = -N

        ans = 1
        for i in range(N):
            ans = ans * x

        return ans


class Solution2:
    # Fast Power Algorithm Recursive
    def myPow(self, x: float, n: int) -> float:
        N = n
        if N < 0:
            x = 1 / x
            N = -N
        return self.fastPow(x, N)

    def fastPow(self, x, n):
        if n == 0:
            return 1.0

        half = self.fastPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


"""
    Brute Force: 
    Time Complexity: O(n) / Space Complexity: O(1)
    
    Fast Power Algorithm Recursive: 
    Time Complexity: O(logn)  Space Complexity: O(logn)(因為 stack 空間)
    
    *** N = -N, 在別的語言可能有 overflow 風險? ***
    從 籃子王 得知, 由於我們的 input range => -(2^31) <= n <= 2^31-1, 所以如果你直接把最小的數字變成正數, 會 overflow!!!!!
    => 所以如果在其他語言, 我們要先 +1 再取負
"""

if __name__ == '__main__':
    demo = Solution()
    x = 2.00000
    n = 10

    print(demo.myPow(x, n))

    demo2 = Solution2()
    print(demo2.myPow(x, n))
