# class Solution:
#     def myAtoi(self, str: str) -> int:
#         if not str or len(str) < 1:
#             return 0
#         i = 0
#         while str[i] == " ":
#             i += 1
#         str = str[i:]
#         j = 0
#         sign = '+'
#         if str[0] == '-':
#             sign = '-'
#             j += 1
#         elif str[0] == '+':
#             j += 1
#
#         result = 0
#         while len(str) > j and '0' <= str[j] <= '9':
#             result = result * 10 + (ord(str[j]) - ord('0'))
#             j += 1
#         if sign == '-':
#             result = -result
#         if result > 2147483647:
#             return 2147483647
#         elif result < -2147483648:
#             return -2147483648
#         else:
#             return result

class Solution:
    def myAtoi(self, str: str) -> int:
        intMax = 2147483647
        intMin = -2147483648
        str = str.strip()
        if not str:
            return 0
        sign, i = 1, 0
        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            sign = -1
            i += 1
        num = 0
        while i < len(str):
            if not str[i].isdigit():
                break
            num = num * 10 + ord(str[i]) - ord('0')
            if num > intMax:
                break
            i += 1
        return min(max(sign * num, intMin), intMax)

"""
    解題思路：
            
            這題怪怪的，可是還是要會哦
            Time Complexity: O(n) / Space Complexity: O(1)(因為沒用什麼特別的額外儲存方式，皆為固定的)
            
            https://leetcode.com/problems/string-to-integer-atoi/discuss/4987/Python-easy-to-understand-solution-(logic-is-easy-to-follow).
            https://www.youtube.com/watch?v=vvua0G0eqsM          
"""


if __name__ == '__main__':
    demo = Solution()
    input_1 = '   -443212'
    print(demo.myAtoi(input_1))