from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        result = []
        self.helper(n, n, '', result)
        return result

    def helper(self, l, r, item, result):   # l=剩餘的( , r=剩餘的)
        if r < l:
            return
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.helper(l - 1, r, item + '(', result)
        if r > 0:
            self.helper(l, r - 1, item + ')', result)

"""
        output = [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]
    
    https://www.youtube.com/watch?v=XF0wh8M2A6E
"""

if __name__ == '__main__':
    demo = Solution()

    output_1 = demo.generateParenthesis(3)
    for i in output_1:
        print(i, end=' ')