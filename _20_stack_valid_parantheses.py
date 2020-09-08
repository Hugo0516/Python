class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for parantheses in s:
            if parantheses in lookup:   # 假如你今天輸入 (, {, [ 理所當然要input 進去
                stack.append(parantheses)
            elif len(stack) == 0 or lookup[stack.pop()] != parantheses:
                # 今天你輸入), }, ], 你的stack沒東西=False(因為不能沒東西),有東西但是pop出來跟你不符也錯
                return False

        return len(stack) == 0      # len != 0 表示還有剩東西, 是錯的QQ

"""
    解題思路：
            Input: "()[]{}" / Output: true
            https://www.youtube.com/watch?v=4z5fmKMr9lU
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = ")"
    print(demo.isValid(input_1))