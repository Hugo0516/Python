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
        str = str.strip()  # remove front space and rear space, if strip('0')=> remove front 0 and rear 0

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

    # Write by myself
    def myAtoi2(self, s: str) -> int:
        int_max = 2147483647
        int_min = -2147483648
        s1 = s.strip()
        start, sign = 0, 1
        ans = 0

        if not s1:
            return 0

        if s1[0] is '+':
            start += 1
        elif s1[0] is '-':
            sign = -1
            start += 1

        for i in range(start, len(s1)):
            if not s1[i].isdigit():
                break
            if s1[i].isdigit():
                ans = ans * 10 + ord(s1[i]) - ord('0')

        ans *= sign
        if ans > int_max:
            return int_max
        elif ans < int_min:
            return int_min

        return ans


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
    input_2 = "-91283472332"
    input_3 = "words and 987"
    input_4 = "4193 with words"
    print(demo.myAtoi(input_1))
    print(demo.myAtoi(input_2))
    print(demo.myAtoi(input_3))
    print(demo.myAtoi(input_4))
