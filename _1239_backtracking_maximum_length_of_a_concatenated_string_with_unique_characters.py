from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.res = 0

        def inAns(s):
            return len(s) > len(set(s))

        def backtrack(arr, index, ans):
            self.res = max(self.res, len(ans))

            if index == len(arr):
                return

            for i in range(index, len(arr)):
                # 這一題的起始位置為 0, 因為 我們每個位置至多只能調用一次, 所以調用過後就得 + 1, 讓他調用下一個位置
                x = ans + arr[i]
                if inAns(ans + arr[i]):
                    continue
                backtrack(arr, i + 1, ans + arr[i])

        backtrack(arr, 0, "")
        return self.res


"""
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.


Time Complexity: 
Space Complexity:

媽的有點難分析 = =, 先從缺 
"""


if __name__ == '__main__':
    demo = Solution()
    input_1 = ["un", "iq", "ue"]
    print(demo.maxLength(input_1))
