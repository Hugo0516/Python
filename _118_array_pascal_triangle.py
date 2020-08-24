from typing import List


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append([])
            for j in range(i + 1):
                if j in (0, i):  # 表示j == 0 or j == i 的時候(即頭跟尾)
                    res[i].append(1)
                else:
                    res[i].append(res[i - 1][j - 1] + res[i - 1][j])

        return res
"""
    TIME COMPLEXITY: O(N^2) / SPACE COMPLEXITY:O(N^2) (1+...+N)(我不確定)
    https://www.youtube.com/watch?v=gq4t3cwMQbs
"""

if __name__ == '__main__':
    demo = Solution()
    res = demo.generate(5)
    print(res)
