import collections
from typing import List


class Solution(object):
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        # 0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        path = []
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, path):
                return []
        return path

    def dfs(self, graph, visited, i, path):
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True

        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j, path):
                return False
        visited[i] = 2
        path.append(i)
        return True


"""
這一題和 207 差異在, 這裡要輸出上課的結果 !!!

Time Complexity: O(V+E)
Space Complexity: O(V+E)
"""
