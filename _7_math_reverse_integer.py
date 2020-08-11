class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            s = str(x)
            d = s[::-1]
            ans = int(d)
        else:
            s = str(x)
            d = s[-1:0:-1]
            d = '-' + d
        ans = int(d)
        if ans > (2 ** 31) - 1 or ans < (-2 ** 31):
            return 0
        return ans

"""
    解題思路：
            此搖要注意是否會 overflow
            In Python: 32 bit machine: -2**31 ~ 2**31 -1 / 64 bit machone: -2**63 ~ 2**63
            
            Input: -123
            Output: -321
            
            Time Complexity: O(n) / Space Complexity: O(1)
            
            https://leetcode.com/problems/reverse-integer/discuss/705939/Python3-Solution
"""


if __name__ == '__main__':
    demo = Solution()
    input_1 = -123
    print(demo.reverse(input_1))
