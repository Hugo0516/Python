class Solution:

    def evaluate_expr(self, stack):

        res = stack.pop() if stack else 0

        # Evaluate the expression till we get corresponding ')'
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res

    def calculate(self, s: str) -> int:

        stack = []
        n, operand = 0, 0

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch.isdigit():

                # Forming the operand - in reverse order.
                operand = (10 ** n * int(ch)) + operand
                n += 1

            elif ch != " ":
                if n:
                    # Save the operand on the stack
                    # As we encounter some non-digit.
                    stack.append(operand)
                    n, operand = 0, 0

                if ch == '(':
                    res = self.evaluate_expr(stack)
                    stack.pop()

                    # Append the evaluated result to the stack.
                    # This result could be of a sub-expression within the parenthesis.
                    stack.append(res)

                # For other non-digits just push onto the stack. '+' or '-'
                else:
                    stack.append(ch)

        # Push the last operand to stack, if any.
        if n:
            stack.append(operand)

        # Evaluate any left overs in the stack.
        return self.evaluate_expr(stack)


class Solution2:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0  # For the on-going result
        sign = 1  # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop()  # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop()  # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand


class Solution3:

    def calculate(self, s: str) -> int:
        res = 0
        stack = []
        operand = 0
        flag = 0

        def eval(stack):
            ans = 0

            while stack:
                tmp = stack.pop()
                if tmp.isdigit():
                    ans += int(tmp)
                else:
                    if tmp == '-':
                        ans = -ans
                    if tmp == '(':
                        pass
            return ans

        for i in range(0, len(s)):
            ch = s[i]

            if ch.isdigit():
                operand = 10 * operand + int(ch)
                flag = 1

            elif ch != ' ':
                if operand != 0:
                    stack.append(str(operand))
                    operand = 0
                    flag = 0
                if ch == '(':
                    stack.append(ch)
                if ch == ')':
                    tmp = eval(stack)
                    res += tmp
                if ch == '+' or ch == '-':
                    stack.append(ch)
            elif ch == ' ':
                if flag == 1:
                    stack.append(str(operand))
                    operand = 0
                    flag = 0
        if operand:
            stack.append(str(operand))
        if stack:
            tmp = eval(stack)
            res += tmp

        return res


class Solution4:
    # 使用了res表示不包括棧里數字在內的結果，num表示當前操作的數字，
    # sign表示運算符的正負，用棧保存遇到括號時前面計算好了的結果和運算符
    def calculate(self, s: str) -> int:
        res, num, sign = 0, 0, 1
        stack = []

        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                res = res + sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res = res + sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res = res + sign * num

        return res


"""
(, ), +, -, non-negative integer, 空格, 

This problem is all about understanding the following:
1. Input always contains valid strings
2. The rules of addition and subtraction
3. Implication of precedence by parenthesis
4. Spaces do not affect the evaluation of the input expression

*** USE APPROACH 1 ***
Approach 1: Stack and String Reversal

Time Complexity: O(N)
Space Complexity: O(N)

Approach 2: Stack and No String Reversal

Time Complexity: O(N), where N is the length of the string. 
The difference in time complexity between this approach and the previous one is that 
every character in this approach will get processed exactly once. 

However, in the previous approach, each character can potentially get processed twice, 
once when it's pushed onto the stack and once when it's popped for processing of the final result (or a subexpression). 
That's why this approach is faster.

Space Complexity: O(N)

這一題可以用 Approach 1 的想法, 但是如過我很直覺的想的話我也不會用 Approach 1的算法= =
=> 事實證明, solution3, 自己寫的漏洞百出= = (solution3 是錯的)
=> 後來新 + sol4(負雪), 感覺這思路也還行, 而且 as below mentioned, 原本Approach1的測資遇到負會錯,
=> 但是 sol4 不會錯

*** 幹 這題測資有問題, 有一個測資為"-2+ 1", 媽的不能有負2阿
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "1 + 1"
    input_2 = " 2-1 + 2 "
    input_3 = "(1-(147+5+2)-3)+(6+28)"
    input_4 = "- (3 + (4 + 5))"  # failed, as the problem do not accept negative integers.

    print(demo.calculate(input_1))
    print(demo.calculate(input_2))
    print(demo.calculate(input_3))
    # print(demo.calculate(input_4))

    demo2 = Solution2()
    print(demo2.calculate(input_1))
    print(demo2.calculate(input_2))
    print(demo2.calculate(input_3))

    demo3 = Solution3()
    input_5 = "1 + 1"
    input_6 = " 2-1 + 2 "
    print(demo3.calculate(input_5))
    print(demo3.calculate(input_6))

    input_7 = "2147483647"
    # input_8 = "-2 + 1"

    demo4 = Solution4()
    print(demo4.calculate(input_3))
