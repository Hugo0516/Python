from typing import List


class Solution:
    def removeInvalidParentheses(self, s):

        left = 0
        right = 0

        # First, we find out the number of misplaced left and right parentheses.
        for char in s:

            # Simply record the left one.
            if char == '(':
                left += 1
            elif char == ')':
                # If we don't have a matching left, then this is a misplaced right, record it.
                right = right + 1 if left == 0 else right

                # Decrement count of left parentheses because we have found a right
                # which CAN be a matching one for a left.
                left = left - 1 if left > 0 else left

        result = {}

        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            # If we reached the end of the string, just check if the resulting expression is
            # valid or not and also if we have removed the total number of left and right
            # parentheses that we should have removed.
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    result[ans] = 1
            else:

                # The discard case. Note that here we have our pruning condition.
                # We don't recurse if the remaining count for that parenthesis is == 0.
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    recurse(s, index + 1, left_count, right_count, left_rem - (s[index] == '('),
                            right_rem - (s[index] == ')'), expr)

                expr.append(s[index])

                # Simply recurse one step further if the current character is not a parenthesis.
                if s[index] != '(' and s[index] != ')':
                    recurse(s, index + 1, left_count, right_count, left_rem, right_rem, expr)
                elif s[index] == '(':
                    # Consider an opening bracket.
                    recurse(s, index + 1, left_count + 1, right_count, left_rem, right_rem, expr)
                elif s[index] == ')' and left_count > right_count:
                    # Consider a closing bracket.
                    recurse(s, index + 1, left_count, right_count + 1, left_rem, right_rem, expr)

                # Pop for backtracking.
                expr.pop()

                # Now, the left and right variables tell us the number of misplaced left and

        # right parentheses and that greatly helps pruning the recursion.
        recurse(s, 0, 0, 0, left, right, [])
        return list(result.keys())


class Solution2:

    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0:
                    right += 1
                else:
                    left -= 1

        def dfs(index, left, right, left_rem, right_rem, cur):
            if index == len(s):
                if left == right and left_rem == right_rem == 0:
                    self.ans.add(cur)
                    return
            else:  # s[depth] can only be either a left paren, right paren or a letter
                if s[index] == "(":
                    if left_rem > 0:  # if we can remove a left paren
                        dfs(index + 1, left, right, left_rem - 1, right_rem, cur)
                    dfs(index + 1, left + 1, right, left_rem, right_rem, cur + "(")  # keep current left paren
                elif s[index] == ")":
                    if right_rem > 0:  # if we can remove a right paren
                        dfs(index + 1, left, right, left_rem, right_rem - 1, cur)
                    if left > right:  # if we can keep the right paren, see LC 22. Generate Parentheses
                        dfs(index + 1, left, right + 1, left_rem, right_rem, cur + ")")
                else:
                    dfs(index + 1, left, right, left_rem, right_rem, cur + s[index])  # we must keep the letter

        self.ans = set()
        dfs(0, 0, 0, left, right, "")
        return list(self.ans)


"""

1. index which represents the current character that we have to process in the original string.
2. left_count which represents the number of left parentheses that have been added to the expression we are building.
3. right_count which represents the number of right parentheses that have been added to the expression we are building.
4. left_rem is the number of left parentheses that remain to be removed.
5. right_rem represents the number of right parentheses that remain to be removed. 
Overall, for the final expression to be valid, left_rem == 0 and right_rem == 0.
----------

Look Solution2, 比較好懂 = =
Time Complexity: O( 2^n ), 每一個符號都有兩種選擇(捨棄 or 留下 )
Space Complexity: O(n)

"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "()())()"
    input_2 = "(a)())()"
    input_3 = ")("

    print(demo.removeInvalidParentheses(input_1))
    print(demo.removeInvalidParentheses(input_2))
    print(demo.removeInvalidParentheses(input_3))

    demo2 = Solution2()
    input_1 = "()())()"
    print(demo2.removeInvalidParentheses(input_1))
