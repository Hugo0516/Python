class Solution:
    def __init__(self):
        self.has_obstacle = {(1, 3): 2, (1, 7): 4, (1, 9): 5, (2, 8): 5, (3, 7): 5, (3, 1): 2, (3, 9): 6, (4, 6): 5,
                             (6, 4): 5, (7, 1): 4, (7, 3): 5, (7, 9): 8, (8, 2): 5, (9, 7): 8, (9, 3): 6, (9, 1): 5}

    def numberOfPatterns(self, m: int, n: int) -> int:
        self.validPatterns = 0

        for num in range(1, 10):  # 代表要從哪個點出發
            self.visited = set()
            self._getValidWays(num, 1, m, n)

        return self.validPatterns

    def _getValidWays(self, num, count, m, n):
        # consider the valid patterns only in length (m to n)
        if m <= count <= n:
            self.validPatterns += 1
        # after reaching path count 'n', we need not go on any further.
        if count == n:
            return

        self.visited.add(num)
        for nextNum in range(1, 10):
            if nextNum not in self.visited:
                # if a nextNum has an obstacle while starting from num, and is not visited previously, don't consider this path.
                if (num, nextNum) in self.has_obstacle and self.has_obstacle[(num, nextNum)] not in self.visited:
                    continue
                self._getValidWays(nextNum, count + 1, m, n)
        self.visited.remove(num)


"""
Input: m = 1, n = 1
Output: 9

Input: m = 1, n = 2
Output: 65

Time Complexity: O(n!), where n is maximum pattern length
The algorithm computes each pattern once and no element can appear in the pattern twice. 
The time complexity is proportional to the number of the computed patterns.

Space Complexity: O(n), where n is maximum pattern length In the worst case the maximum depth of recursion is n. 
Therefore we need O(n) space used by the system recursive stack

Time Complexity 的部分,  我有疑問= =

Reference: https://leetcode.com/problems/android-unlock-patterns/discuss/475868/Python-DFS-readable-code.
"""

if __name__ == '__main__':
    demo = Solution()
    print(demo.numberOfPatterns(1, 3))
