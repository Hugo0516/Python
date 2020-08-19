from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Create Graph
        graph_dic = {}

        for start, end in edges:
            if start not in graph_dic:
                graph_dic[start] = [end]
            else:
                graph_dic[start].append(end)
            if end not in graph_dic:
                graph_dic[end] = [start]
            else:
                graph_dic[end].append(start)

        # DFS to detect cycles
        visited = set()
        stack = [(0, -1)]
        while stack:
            node, parent = stack.pop()
            visited.add(node)
            if node in graph_dic:
                for next_node in graph_dic[node]:
                    if next_node not in visited:
                        stack.append((next_node, node))
                    else:
                        if next_node != parent:
                            return False
                        # 因為現在是預期要在 node 和 next_node 之間建立一條edge
                        # 但是呢我們發現 next_node 已經在 visited 裡面惹, 所以我們就要想說他是不是 node 的 parent,
                        # 因為他若不是parent那就代表 next_node 和 爸爸有連結
                        # 而 node 本身就是有和爸爸連結
                        # =>那現在 node 跟 parent 有連結
                        #   next_node 也跟 parent 有連結
                        # 那不就變成 node, next_node, parent 三個彼此有連結
                        # 這樣就會形成cycle

        # check if we can traverse all node
        if len(visited) != n:
            return False
            # False means that maybe we left some nodes,
            # so maybe we have more than one connected component

        return True


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

    def validTree2(self, n: int, edges: List[List[int]]) -> bool:
        s = UnionFindSet(len(edges))  # 一條 edge 會有 2個 node 所以 34行才要+1
        for edge in edges:
            if not s.union(edge[0], edge[1]):  # if 成立代表這兩個node的最終parent都一樣, 所以會導致circle
                # return edge
                return False
        return None


"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false ([1, 3] => cycle)

Note: you can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
---------------------------------------------------------------------------------------------------------

這道題給了一個無向圖，讓我們來判斷其是否為一棵樹，
如果是樹的話，所有的節點必須是連接的，也就是說必須是連通圖，而且不能有環，所以焦點就變成了驗證是否是連通圖和是否含有環。
=> The graph has no cycles, and the graph has only one connected component
no cycles means that: if there are n vertices it should have n-1 edges

Therefore, check that there are n-1 edges and all vertices are connected

It is an important problem,how to detect cycles in the graph

這題應該也可以用 Union Find to solve !!
---------------------------------------------------------------------------------------------------------
Leetcode 684 就是 261 的變形題!!!!!
261 傳 true or false
684 傳 那個edge

https://www.youtube.com/watch?v=994TPE325bs

"""
if __name__ == '__main__':
    demo = Solution()
    input_1 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    # print(demo.validTree(5, input_1))

    demo_2 = Solution2()
    input_2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(demo_2.validTree2(5, input_2))
