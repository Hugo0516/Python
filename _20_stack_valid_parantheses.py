class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for parantheses in s:
            if parantheses in lookup:
                stack.append(parantheses)
            elif len(stack) == 0 or lookup[stack.pop()] != parantheses:
                return False

        return len(stack) == 0

"""
    解題思路：
            Input: "()[]{}" / Output: true
            https://www.youtube.com/watch?v=4z5fmKMr9lU
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "([)]"
    print(demo.isValid(input_1))