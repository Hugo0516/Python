from typing import List


# Method 1
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = [0] * (len(edges) + 1)
        s = [1] * (len(edges) + 1)

        def find(u):
            while p[u] != u:
                p[u] = p[p[u]]
                u = p[u]
            return u

        for u, v in edges:
            if p[u] == 0: p[u] = u
            if p[v] == 0: p[v] = v
            pu, pv = find(u), find(v)

            if pu == pv:
                return [u, v]

            if s[pv] > s[pu]: u, v = v, u
            p[pv] = pu
            s[pu] += s[pv]

        return []


# Method 2
class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n + 1)]  # 一開始每個結點的 parent 都為他自己 => 代表每一個點都是獨立的node
        # 也就是說 假如n = 5, 那麼現在就有5個forest的感覺,且每個forest就是只有一個node(所以此node也等於此樹的root)
        self._ranks = [1 for i in range(n + 1)]  # 因為上面一行的初始,所以rank 設成0(我覺得或許與可以設成1??)

    def find(self, u):  # 返回 u 的主先
        while u != self._parents[u]:  # 表示 u 不是根結點
            self._parents[u] = self._parents[self._parents[u]]  # 順便做 pass compresion
            u = self._parents[u]
        return u

    def union(self, u, v):
        root_x, root_y = self.find(u), self.find(v)
        if root_x == root_y:
            return False

        if self._ranks[root_x] < self._ranks[root_y]:
            self._parents[root_x] = root_y
        elif self._ranks[root_x] > self._ranks[root_y]:
            self._parents[root_y] = root_x
        else:
            self._parents[root_y] = root_x  # 假如 rank 相同, 將 pv 放到 pu 底下
            self._ranks[root_x] += 1

        return True


class Solution2:
    def findRedundantConnection2(self, edges):
        s = UnionFindSet(len(edges))  # 一條 edge 會有 2個 node 所以 34行才要+1
        for edge in edges:
            if not s.union(edge[0], edge[1]):  # if 成立代表這兩個node的最終parent都一樣, 所以會導致circle
                return edge
        return None

# 不能跑 我不知道錯在哪
class Solution3:
    def findRedundantConnection3(self, edges):

        def dfs(graph, node, visited, temp):
            visited.add(node)
            temp.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(graph, neighbor, visited, temp)
            return temp

        graph = {}
        for edge in edges:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]

        connected_component = []
        visited = set()
        for i in range(1, len(graph) + 1):
            if i not in visited:
                temp = []
                connected_component.append(dfs(graph, i, visited, temp))

        print(connected_component)
        return connected_component[-1]


"""
    Input: [[1,2], [1,3], [2,3]]
    Output: [2,3]
    Explanation: The given undirected graph will be like this:
      1
     / \
    2 - 3
    
    Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
    Output: [1,4]
    Explanation: The given undirected graph will be like this:
    5 - 1 - 2
        |   |
        4 - 3
        
    此題和 737 為 Union Find 的經典應用
    
    Union Find 的應用題型 常常也可以用 DFS 來解！！！
    EX 737
"""

if __name__ == '__main__':
    demo_1 = Solution()
    demo_2 = Solution2()
    demo_3 = Solution3()
    input_1 = [[1, 2], [1, 3], [2, 3]]
    input_2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(demo_1.findRedundantConnection(input_1))
    print(demo_2.findRedundantConnection2(input_2))
    print(demo_3.findRedundantConnection3(input_1))
