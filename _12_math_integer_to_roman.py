class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        result = ''
        for i in range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                result += numerals[i]
        return result


"""
    解題思路：
            想到可以對應到Dictionary 之類的方面去想
            Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
            Input: 1994 / Output: "MCMXCIV" / Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
            
            Time Complexity: O(n) / Space Complexity: O(1) (我自己想的，待確認!!!)
            
            https://www.youtube.com/watch?v=RzU6tWxpPPg
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = 1994
    print(demo.intToRoman(input_1))