import collections
from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        a = [0 for _ in range(256)]
        for x in s:
            a[ord(x)] += 1
        count = 0
        s, cd = '', []
        for i in range(len(a)):
            if a[i] % 2:
                s = chr(i)
                a[i] -= 1
                count += 1
                if count > 1:
                    return []
            cd += [chr(i)] * (a[i] / 2)
        ans = []
        self.helper(ans, cd, s)
        return ans

    def helper(self, ans, cd, s):
        if not cd:
            ans.append(s)
        for i in range(len(cd)):
            if i > 0 and cd[i] == cd[i - 1]:
                continue
            self.helper(ans, cd[:i] + cd[i + 1:], cd[i] + s + cd[i])


class Solution2:
    def generatePalindromes(self, s):
        ans = []
        n = len(s)
        counter = collections.Counter(s)

        def helper(tmp):
            if len(tmp) == n:
                ans.append(tmp)
                return
            for k, v in counter.items():
                if v > 0:
                    counter[k] -= 2
                    helper(k + tmp + k)
                    counter[k] += 2

        odd_item = [key for key, value in counter.items() if value % 2 != 0]
        if len(odd_item) > 1:   # 如果奇數個數的字母太多的話, 是沒有辦法做回文的
            return []
        if len(odd_item) == 1:
            # 如果只有一個奇數個數的字母, 可能有以下三種情況
            # "aab" => "aba" / "a" => "a" / "bbb" => "bbb"
            counter[odd_item[0]] -= 1
            helper(odd_item[0])
        else:
            helper('')
        return ans


"""
Input: "aabb"
Output: ["abba", "baab"]

Solution 1: https://leetcode.com/problems/palindrome-permutation-ii/discuss/69722/Python-DFS-Solution
Solution 2: https://leetcode.com/problems/palindrome-permutation-ii/discuss/120631/Short-Python-Solution-with-backtracking

**** Solution 2 ****

Time Complexity: O( (n/2)! )
Space Complexity: O(n), the depth of recursion tree can go upto n/2 in the worst case
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "aabb"
    input_2 = "abc"
    # print(demo.generatePalindromes(input_1))
    # print(demo.generatePalindromes(input_2))

    demo2 = Solution2()
    print(demo2.generatePalindromes(input_1))
    print(demo2.generatePalindromes(input_2))
    print(demo2.generatePalindromes("a"))
    print(demo2.generatePalindromes("aab"))
    print(demo2.generatePalindromes("abbbbbbccccdddd"))
    print(demo2.generatePalindromes("aabb"))

    dict_1 = {'A': 1, 'B': 2, 'C': 3}
    print(dict_1.items())
    print(dict_1.keys())
    print(dict_1.values())
