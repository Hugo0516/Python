class Solution:

    def longestValidParentheses(self, s: str) -> int:
        dp, res = [0] * len(s), 0  # 初始化dp、定義最優結果變量
        for i in range(len(s)):
            if s[i] == ')':  # 只考慮以')'結尾的子串
                if i > 0 and s[i - 1] == '(':  # 第一中情況，直接加 2
                    dp[i] = dp[i - 2] + 2
                if i > 0 and s[i - 1] == ')':  # 第二種情況，
                    if i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                        if i - dp[i - 1] - 1 > 0:  # 當前合法子串，前面還有子串，的情況
                            dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                        else:  # 當前合法子串，前面--沒有--子串，的情況
                            dp[i] = dp[i - 1] + 2
                res = max(res, dp[i])  # 更新最長的合法子串
        return res


"""
This is DP version

*** 記住這個版本 !!!!!! ***

Transfer function:
dp array where ith element of dp represents the length of the longest valid substring ending at ith index. 
We initialize the complete dp array with 0's.

看到這個問題的時候，第一想法就是那個最長回文子串問題，也就是可以使用動態規劃的思想來解決。大概過程如下:
（1）設dp[i]表示以第i個字符結尾的最長合法字串的長度，初始化全為0。
（2）對整個字符串進行一次遍歷操作，遇到'('時，不用操作，因為以'('結尾的子串一定不是合法的。
（3）當遇到的字符是')'時，要具體分析，因為以')'結尾的串可能是合法的也可能是不合法的。
A、如果s[i-1] == '('則，dp[i] = dp[i-1] + 2 ,因為前一個是非法結尾，可以形成一對合法的括號，所以直接加2。
B、如果s[i-1] == ')' 則，在當前字串前，可能存在一個合法的子串，也可能不存在合法的子串。
a、現在我們要找到s[i - 1 - dp[i - 1]]這個字符，判斷它是否=='('，如果等於說明這個合法的子串在兩端還可以添加一對括號，所以總的長度還可以增加2。
b、此外，還有一個情況，就是，在s[i - 1 - dp[i - 1]] =='('的位置之前，
如果也存在一個合法的子串，那麼現在也應該把他添加到dp[i]中，所以dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2。
（需要注意的是，要判斷向前查找的過程，數字不要越界）
Both time complexity and space complexity are O(n)

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

Time Complexity: O(n), n is the length of the given string.
Space Complexity: O(n), the size of stack can go up to n.

"""


class Solution2:

    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        dp = [0] * len(s)

        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    if (i - dp[i - 1]) >= 2:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i - 1] + 2
            ans = max(ans, dp[i])

        return ans


"""
Leetcode 版本的 DP 寫法, 應該和 sol 1 的 transfer function 定義一樣才對

Time Complexity: O(n), n is the length of the given string.
Space Complexity: O(n), the size of stack can go up to n.
"""

# class Solution:
#
#     def longestValidParentheses(self, s):
#         stack, res = [-1], 0
#         for i, e in enumerate(s):
#             if e == '(':
#                 stack.append(i)
#             elif e == ')':  # 出棧
#                 stack.pop()
#                 if not stack:  # 如果棧為空，當前 位置索引 進棧，做為一個新的子串的開始（主要用作求合法子串的長度）
#                     stack.append(i)
#                 else:
#                     res = max(res, i - stack[-1])  # 更新合法子串的長度
#         return res


# 這是討論區的說的另一種方法，就是用棧的方法，其實自己一開始也想到了用棧，但是沒想通用棧去存什麼才能計算出長度。
# 思路大致如下：
# （1）我們用一個棧去儲存字符串的下標索引，用於後期的長度的推算。
# （2）遇到'('就進棧，遇到')'就出棧，在出棧的時候要分情況談論。
# （3）當遇到')'就出棧，如果此時，出棧後，棧已經為空，那麼就把當前i值（位置索引）放入棧中，相當於入棧了一個')' ，為什麼？
#     它可以作為一個新子串的開始，用於後期合法子串的長度的計算。
# （4）當遇到')'就出棧，如果此時，出棧後，棧不為空，當前合法子串長度為：
# i - stack[-1]，為什麼是i - stack[-1] ？
# 這個很好理解，stack[-1]是棧頂元素，即離當前合法子串左邊最近的一個字符，i是當前位置的索引，也就是')'的位置，
# 所以差就是合法子串的長度，隨著不斷進棧或者出棧，長度也會發生變化，我們保留最長的一個就可以了。


if __name__ == '__main__':
    # s = ')()())'
    s = '))()((()())))'
    #    0123456789101112
    stack = []
    print(bool(stack), bool(not stack), end='')
    print('')
    solu = Solution()
    print(solu.longestValidParentheses(s))

    s2 = "(()"
    s3 = ")()())"
    s4 = "())((())"
    demo2 = Solution2()
    print(demo2.longestValidParentheses(s2))
    print(demo2.longestValidParentheses(s3))
    print(demo2.longestValidParentheses(s4))
