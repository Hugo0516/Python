class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


# Bottom-up
class Solution2:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        cache = {0: 0, 1: 1}

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[N]


# Top-down
class Solution3:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        self.cache = {0: 0, 1: 1}
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        if N in self.cache.keys():
            return self.cache[N]

        self.cache[N] = self.memoize(N - 1) + self.memoize(N - 2)
        return self.memoize(N)


class Solution4:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N
        if (N == 2):
            return 1

        current = 0
        prev1 = 1
        prev2 = 1

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(3, N + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current


class Solution5:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N

        A = [[1, 1], [1, 0]]
        self.matrix_power(A, N - 1)

        return A[0][0]

    def matrix_power(self, A: list, N: int):
        if (N <= 1):
            return A

        self.matrix_power(A, N // 2)
        self.multiply(A, A)
        B = [[1, 1], [1, 0]]

        if (N % 2 != 0):
            self.multiply(A, B)

    def multiply(self, A: list, B: list):
        x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        w = A[1][0] * B[0][1] + A[1][1] * B[1][1]

        A[0][0] = x
        A[0][1] = y
        A[1][0] = z
        A[1][1] = w


# Contributed by LeetCode user mereck.
class Solution6:
    def fib(self, N):
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)


"""
Approach 1: Recursion

Time Complexity: O(2^n)
Space Complexity: O(n)

Approach 2: Bottom-Up Approach using Memoization

Time Complexity: O(n) 
Space Complexity: O(n)

Approach 3: Top-Down Approach using Memoization

Time Complexity: O(n)
Space Complexity: O(n)

Approach 4: Iterative Top-Down Approach

Time Complexity: O(n)
Space Complexity: O(1)

Approach 5: Matrix Exponentiation

Time Complexity: O(LogN)
Space Complexity: O(LogN)

Approach 6: Math

Time Complexity: O(1)
Space Complexity: O(1)
"""

if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()
    demo3 = Solution3()
    demo4 = Solution4()
    demo5 = Solution5()
