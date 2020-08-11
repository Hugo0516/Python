# class Solution:
#     """
#     将数字0-9和字符串做一一对应，从而变成int型，然后相加
#     """
#     def addStrings(self, num1: str, num2: str) -> str:
#
#         num_num1 = self.num(num1)
#         num_num2 = self.num(num2)
#         return str(num_num1+num_num2)
#
#     def num(self, num1):
#         """
#         str变成int型
#         """
#         dic_num = {'1': 1,
#                    '2': 2,
#                    '3': 3,
#                    '4': 4,
#                    '5': 5,
#                    '6': 6,
#                    '7': 7,
#                    '8': 8,
#                    '9': 9,
#                    "0": 0 }
#         num_num1 = 0
#         a = 0
#         for i in num1:  # 多少位数
#             a += 1
#         for i in num1:
#             a -= 1
#             num_num1 += dic_num[i]*10**a
#         return num_num1
# 464ms

# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         if len(num1) < len(num2):
#             num1,num2 = num2,num1
#         num1 = num1[::-1]
#         num2 = num2[::-1]
#         ans = []
#         carry = 0
#         i = 0
#         while i < max(len(num1),len(num2)):
#             if i < len(num1) and i < len(num2):
#                 sumV = ord(num1[i]) - ord("0") + ord(num2[i]) - ord("0") + carry
#             else:
#                 sumV = ord(num1[i]) - ord("0") + carry
#             carry = sumV//10
#             ans.append(str(sumV%10))
#             i += 1
#         if carry:
#             ans.append(str(carry))
#         return "".join(ans[::-1])

# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         carry = 0
#         s = ""
#         i, j = len(num1) - 1, len(num2) - 1
#         while i >= 0 or j >= 0 or carry:
#             digit1 = int(num1[i]) if i >= 0 else 0
#         digit2 = int(num2[j]) if j >= 0 else 0
#         cur_sum = digit1 + digit2 + carry
#         carry, rem = divmod(cur_sum, 10)
#         s = str(rem) + s
#         i, j = i - 1, j - 1
#
#         return s

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry, i, j = 0, len(num1) - 1, len(num2) - 1
        res = []
        while i >= 0 or j >= 0 or carry > 0:
            carry += int(num1[i]) if i >= 0 else 0
            carry += int(num2[j]) if j >= 0 else 0

            res.append(str(carry % 10))
            carry //= 10

            i -= 1
            j -= 1

        return "".join(reversed(res))
# 40ms

def main():
    solution_1 = Solution()
    input_1 = input()
    input_2 = input()

    print(solution_1.addStrings(input_1, input_2))

if __name__ == '__main__':
    main()