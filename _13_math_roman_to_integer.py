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
            if i > 0 and m[s[i]] > m[s[i-1]]:
                result += m[s[i]] - 2*m[s[i-1]]
            else:
                result += m[s[i]]

        return result

"""
    解題思路：
            這個版本好像快了點
            Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
            https://www.youtube.com/watch?v=MBfPfAH6jdE
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "LVIII"   #58
    print(demo.romanToInt(input_1))