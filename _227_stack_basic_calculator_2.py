class Solution:

    def calculate(self, s: str) -> int:
        stack = []
        pre_op = '+'
        num = 0

        for i, each in enumerate(s):
            if each.isdigit():
                num = 10 * num + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                pre_op = each
                num = 0

        return sum(stack)


"""
Approach 1(負雪)

Time Complexity: O(n), where n is the length of the string s. We iterate over the string s at most twice.
Space Complexity: O(n), where n is the length of the string s.
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "3+2*2"
    input_2 = " 3/2 "
    input_3 = " 3+5 / 2 "

    print(demo.calculate(input_1))
    print(demo.calculate(input_2))
    print(demo.calculate(input_3))
