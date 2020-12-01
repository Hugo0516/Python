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
"""

if __name__ == '__main__':
    demo = Solution()
    x = 2.00000
    n = 10

    print(demo.myPow(x, n))

    demo2 = Solution2()
    print(demo2.myPow(x, n))
