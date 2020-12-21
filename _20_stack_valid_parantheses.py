class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for parantheses in s:
            if parantheses in lookup:  # 假如你今天輸入 (, {, [ 理所當然要input 進去
                stack.append(parantheses)
            elif len(stack) == 0 or lookup[stack.pop()] != parantheses:
                # 今天你輸入), }, ], 你的stack沒東西=False(因為不能沒東西),有東西但是pop出來跟你不符也錯
                return False

        return len(stack) == 0  # len != 0 表示還有剩東西, 是錯的QQ

    # Finished by myself 57% 有點慢
    def isValid2(self, s: str) -> bool:
        # Input: s = "([)]"
        # Output: false
        stack = []

        dict_1 = {')': '(', '}': '{', ']': '['}
        list_1 = ['(', '[', '{']
        match = 0
        stack_num = 0

        for i in range(len(s)):
            item = s[i]
            if item in list_1:
                stack.append(item)
                match -= 1
                stack_num += 1
            elif item in dict_1:
                if stack_num == 0:
                    return False

                ch = dict_1[item]
                if stack[stack_num - 1] == ch:
                    match += 1
                    stack.pop()
                    stack_num -= 1
        if stack_num != 0:
            return False
        elif match == 0:
            return True
        else:
            return False

    # win 90%
    # Time Complexity: O(n)
    # Space Complexity: as we push all opening brackets onto the stack and in the worst case,
    # we will end up pushing all the brackets onto the stack. e.g. ((((((((((.
    def isValid3(self, s: str) -> bool:
        stack = []
        mapping = {'}': '{', ')': '(', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


class Solution2(object):
    def isValid(self, s: str) -> bool:

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack


"""
    解題思路：
            Input: "()[]{}" / Output: true
            https://www.youtube.com/watch?v=4z5fmKMr9lU
    
記住 Solution 2:

Time Complexity: O(n), 
because we simply traverse the given string one character at a time 
and push and pop operations on a stack take O(1) time.

Space Complexity: O(n), as we push all opening brackets onto the stack and in the worst case, 
we will end up pushing all the brackets onto the stack. e.g. ((((((((((.

"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = ")"
    print(demo.isValid(input_1))

    input_2 = "()"
    print(demo.isValid2(input_2))

    input_3 = "()[]{}"
    print(demo.isValid2(input_3))

    input_4 = "]"
    input_5 = "(])"
