from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans


"""
Greedy + 利用 Hash table 做加速

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Time Complexity: O(n)
Space Complexity: O(26/128)

如果用 brute force:
Time Complexity: O(n^2)
Space Complexity: O(1)

Hua Hua, 的方法裡面在 c++, java, 裡面用的結構是用 array, 然後搭配 ascii code,
(因為, 一個字母有自己的 ascii code, 所以就把那個位置(ascii code 號碼), 改變成字母最後出現的位置)
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "ababcbacadefegdehijhklij"
    print(demo.partitionLabels(input_1))

