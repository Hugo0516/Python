from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):  # 這邊的 first=1, 因為我們題目是從1開始做組合
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return  # prune unused call stack !!!!
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        backtrack()
        return output


"""
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Time Complexity: O( k * C(k取n) )
Space Complexity: O( C(k取n) )
"""

if __name__ == '__main__':
    demo = Solution()
    n = 4
    k = 2
    print(demo.combine(n, k))
