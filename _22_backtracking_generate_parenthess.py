from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        result = []
        self.helper(n, n, '', result)
        return result

    def helper(self, l, r, item, result):  # l=剩餘的( , r=剩餘的)
        if r < l:
            return
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.helper(l - 1, r, item + '(', result)
        if r > 0:
            self.helper(l, r - 1, item + ')', result)


class Solution2(object):

    def generateParenthesis(self, N):
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans


"""
        output = [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]
    
    https://www.youtube.com/watch?v=XF0wh8M2A6E
    
Approach 2:
Time Complexity: O( 4^n / n^(1/2) ), Each valid sequence has at most n steps during the backtracking procedure.
Space Complexity: O( 4^n / n^(1/2) ), as described above, and using O(n) space to store the sequence. 

"""

if __name__ == '__main__':
    demo = Solution()

    output_1 = demo.generateParenthesis(3)
    for i in output_1:
        print(i, end=' ')

    print()
    demo2 = Solution2()
    print(demo2.generateParenthesis(3))
