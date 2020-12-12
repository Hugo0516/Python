from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.helper(s, [], ans)
        return ans

    def helper(self, s, temp, ans):
        if not s:
            ans.append(temp)
        for i in range(len(s)):
            x, y = s[:i + 1], s[:i + 1][::-1]
            if s[:i + 1] == s[:i + 1][::-1]:
                w, z = s[i + 1:], temp + [s[:i + 1]]
                self.helper(s[i + 1:], temp + [s[:i + 1]], ans)


class Solution2:
    def partition(self, s):
        if not s:
            return []

        output = []
        self.findPartition(s, output, [])

        return output

    def findPartition(self, s, output, temp):
        if not s:
            output.append(temp[:])
            return

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                temp.append(s[:i])
                self.findPartition(s[i:], output, temp)
                temp.pop()

    def isPalindrome(self, string):
        return string == string[::-1]


"""
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Input: s = "a"
Output: [["a"]]

Approach 2 才是我心目中正統的 解法 ！！！

Solution 1: https://leetcode.com/problems/palindrome-partitioning/discuss/42024/Python-DFS-greater-DP
Solution 2: https://leetcode.com/problems/palindrome-partitioning/discuss/42149/Python-DFS-solution

Time Complexity: O( N * 2^N ), where N is the length of string s. This is the worst-case time complexity when all the possible substrings are palindrome.

Space Complexity: O(N), where N is the length of the string s. This space will be used to store the recursion stack. 
For s = aaa, the maximum depth of the recursive call stack is 3 which is equivalent to N.
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "aab"
    print(demo.partition(input_1))

    demo2 = Solution2()
    print(demo2.partition(input_1))
