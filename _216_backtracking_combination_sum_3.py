from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        def backtrack(remain, tmp, next_start):
            if remain == 0 and len(tmp) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(tmp))
                return
            elif remain < 0 or len(tmp) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                tmp.append(i + 1)
                backtrack(remain - i - 1, tmp, i + 1)
                # backtrack the current choice
                tmp.pop()

        backtrack(n, [], 0)

        return results


"""
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
"""

if __name__ == '__main__':
    demo = Solution()
    k = 3
    n = 7
    print(demo.combinationSum3(k, n))
