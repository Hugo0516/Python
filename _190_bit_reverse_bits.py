class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1

        return ans


"""
Reference: Hua Hua,

Bit operation:
Base-10 time case:
ans = ans * 10 + n % 10
n /= 10

Base-2 is exact the same if n is positive:
ans = ans * 2 + n % 2
n /= 2

or use bit operators:
ans = (ans << 1) | (n & 1)
n >>= 1

Time Complexity: O(logn)
Space Complexity: O(1) 

"""

if __name__ == '__main__':
    demo = Solution()
    n = 0b0000010100101000001111010011100
    print(demo.reverseBits(n))
