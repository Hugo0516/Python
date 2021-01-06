import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        # status: 0=unknown, 1=visiting, 2=visited
        visited = [0] * numCourses
        for i in range(numCourses):
            if not self._dfs(i, graph, visited):
                # 代表有 cycle
                return False

        return True

    def _dfs(self, curr, graph, visited) -> bool:
        if visited[curr] == 1:  # visiting
            return False
        if visited[curr] == 2:  # visited
            return True

        visited[curr] = 1

        for _next in graph[curr]:
            if not self._dfs(_next, graph, visited):
                return False

        visited[curr] = 2
        return True


"""
2021 / 01 / 07 updated:
這一題思路就是找出： "有沒有環", 而不是真正的 topological sort

*** 和 210 互相參照 ***
Hua Hua:
這一題採用 topological sort, 
然後 請記得 topological sort template!!!

Topological sorting:

for each node:
    if not marked:
        if (dfs(node) == CYCLE) return CYCLE
return OK

dfs(node):
    if node is marked as visited: return OK
    if node is marked as visiting: return CYCLE
    mark node as visiting
    for each new_node in node.neighbors:
        if dfs(new_node) == CYCLE: return CYCLE
    marked node as visited
    
    add node to the head of ordered_list
    return OK

和 dfs 的差異在 有兩個額外數組 visited 和 visiting 要維持
    
    Time Complexity: O(n) / O(E+V)
    Space Complexity: ? / O(E+V)
    
-----------
Leetocde 解法:

L = Empty list that will contain the sorted elements
S = Set of all nodes with no incoming edge

while S is non-empty do
    remove a node n from S
    add n to tail of L
    for each node m with an edge e from n to m do
        remove edge e from the graph
        if m has no other incoming edges then
            insert m into S

if graph has edges then
    return error   (graph has at least one cycle)
else 
    return L   (a topologically sorted order)


"""

if __name__ == '__main__':
    demo = Solution()
    print(demo.canFinish(2, [[1, 0]]))
    print(demo.canFinish(2, [[1, 0], [0, 1]]))
    print(demo.canFinish(8, [[1, 0], [2, 6], [1, 7], [5, 1], [6, 4], [7, 0], [0, 5]]))

    print('---')


