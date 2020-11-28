import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        visited = [0] * numCourses
        for i in range(numCourses):
            if not self._dfs(i, graph, visited):
                return False

        return True

    def _dfs(self, curr, graph, visited) -> bool:
        if visited[curr] == 1:
            return False
        if visited[curr] == 2:
            return True

        visited[curr] = 1

        for _next in graph[curr]:
            if not self._dfs(_next, graph, visited):
                return False

        visited[curr] = 2
        return True


"""
    Time Complexity: O(n^2)
    Space Complexity: O(n)
"""

demo = Solution()
print(demo.canFinish(2, [[1, 0]]))
print(demo.canFinish(2, [[1, 0], [0, 1]]))
print(demo.canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]))
