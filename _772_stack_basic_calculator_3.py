class Solution:
    def calculate(self, s: str) -> int:
        def update(op, num):
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            elif op == '/':
                stack.append(int(stack.pop() / num))

        stack = []
        op = '+'
        num = 0
        opset = set('+-/*')

        for c in s + '+':
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in opset or c == ')':
                update(op, num)
                num = 0
                op = c
                if c == ')':
                    tmp_num = 0
                    while stack[-1] not in opset:
                        tmp_num += stack.pop()
                    update(stack.pop(), tmp_num)
            elif c == '(':
                stack.append(op)
                num = 0
                op = '+'
        return sum(stack)


"""
Reference:

Time Complexity:
Space Complexity:
"""

if __name__ == '__main__':
    demo = Solution()

    input_1 = "1 + 1"
    input_2 = " 6-4 / 2 "
    input_3 = "2*(5+5*2)/3+(6/2+8)"
    input_4 = "(2+6* 3+5- (3*14/7+2)*5)+3"
    input_5 = "0"

    print(demo.calculate(input_1))
    print(demo.calculate(input_2))
    print(demo.calculate(input_3))
    print(demo.calculate(input_4))
    print(demo.calculate(input_5))
