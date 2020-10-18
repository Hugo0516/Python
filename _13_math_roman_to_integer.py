# class Solution:
#     def romanToInt(self, s: str) -> int:
#         m = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
#              'C': 100, 'D': 500, 'M': 1000}
#         ans = m[s[0]]
#         for c, p in zip(s[1:], s[0:-1]):
#             ans += m[c]
#             if m[c] > m[p]: ans -= 2 * m[p]
#         return ans

"""
    解題思路：
            Input: "LVIII" / Output: 58 / Explanation: L = 50, V= 5, III = 3.
            要看一下 zip 的用法 !!!!!!
            Time Complexity: O(n) / Space Complexity: O(1)
            https://www.youtube.com/watch?v=joFpSO_sHnU
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i > 0 and m[s[i]] > m[s[i - 1]]:
                result += m[s[i]] - 2 * m[s[i - 1]]
            else:
                result += m[s[i]]

        return result

    # 我自己想的!!
    # Time Complexity: O(n), n=length of input/
    # Space Complexity: O(1), Because only a constant number of single-value variables are used
    def romanToInt2(self, s: str) -> int:
        dict_1 = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50,
                  'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        start, end = 0, 2
        ans = 0
        length_1 = len(s)

        while length_1 > 0:
            if s[start:end] in dict_1:
                ans += dict_1[s[start:end]]
                start += 2
                end += 2
                length_1 -= 2
            else:
                end -= 1
                ans += dict_1[s[start:end]]
                start += 1
                end += 2
                length_1 -= 1
        return ans


"""
    解題思路：
            這個版本好像快了點
            Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
            https://www.youtube.com/watch?v=MBfPfAH6jdE
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "LVIII"  # 58
    print(demo.romanToInt(input_1))
