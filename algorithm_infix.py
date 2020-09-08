# 也可以用 dictionary
def priority(operation):
    return 1 if operation in "+-" else 2 if operation in "*/" else 0


def isEmpty(stack):
    if len(stack) > 0:
        return 1
    else:
        return 0


def infixToPostfix(expression):
    for char in expression:
        if char not in "+-*/()":
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            temp = stack.pop()
            while temp != '(' and isEmpty(stack) != 0:
                output.append(temp)
                temp = stack.pop()
            if temp == '(':
                pass
        else:
            if stack:
                while stack:
                    if priority(char) <= priority(stack[-1]):
                        output.append(stack.pop())
                    elif priority(char) > priority(stack[-1]):
                        stack.append(char)
                        break
            else:
                stack.append(char)

    while stack:
        temp = stack.pop()
        output.append(temp)


def infixToPrefix(expression, stack, output):
    for char in reversed(expression):
        if char not in "+-*/()":
            output.append(char)
        elif char == ')':
            stack.append(char)
        elif char == '(':
            temp = stack.pop()
            while temp != ')' and isEmpty(stack) != 0:
                output.append(temp)
                temp = stack.pop()
            if temp == ')':
                pass
        else:
            if stack:
                while stack:
                    if priority(char) <= priority(stack[-1]):
                        output.append(stack.pop())
                    elif priority(char) > priority(stack[-1]):
                        stack.append(char)
                        break
                    if not stack:
                        stack.append(char)
                        break
            else:
                stack.append(char)

    while stack:
        temp = stack.pop()
        output.append(temp)


stack = []
output = []
infix = "(a+b)*(c+d)"
infix2 = "a+b*c"
infixToPostfix(infix)
print(output)

stack = []
output = []
infixToPostfix(infix2)
print(output)

# stack = []
# output = []
# infixToPrefix(infix2)
# print(output)

infix3 = "(a)+(b*c)"
stack = []
output = []
infixToPostfix(infix3)
print(output)

infix4 = "((a+b)-c*(d+e)+f)/(g+h*i)"
stack = []
output = []
infixToPostfix(infix4)
print(output)

stack = []
output = []
infixToPrefix(infix4, stack, output)
output.reverse()
print(output)
