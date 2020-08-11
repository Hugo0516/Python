class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        q, times = 0, 0
        while dividend >= divisor:
            cur = dividend - (divisor << times)

            if cur >= 0:
                q += (1 << times)
                times += 1
                dividend = cur
            else:
                times -= 1
        return max(-2 ** 31, min(q * flag, 2 ** 31 - 1))

    # 這個會超過時間, 因為用一般減法太慢了
    def divide2(self, dividend: int, divisor: int) -> int:
        flag = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        q = 0

        while dividend >= divisor:
            cur = dividend - divisor
            q += 1
            dividend = cur

        return max(-2 ** 31, min(q * flag, 2 ** 31 - 1))

"""
    思路： 一直減，一直減
    要注意算法的操作不能花太多時間
    Time Complexity: O(n)
    https://www.youtube.com/watch?v=pf5To4GySB4
"""

if __name__ == '__main__':
    demo = Solution()
    dividend_1 = 7
    divisor_1 = -3
    print(demo.divide(dividend_1, divisor_1))
