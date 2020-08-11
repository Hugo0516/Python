from collections import defaultdict
from heapq import *


def Prim(vertexs, edges, start_node):
    adjacent_vertex = defaultdict(list)
    for v1, v2, length in edges:
        adjacent_vertex[v1].append((length, v1, v2))
        adjacent_vertex[v2].append((length, v2, v1))

    mst = []
    closed = set(start_node)

    i = 1

    adjacent_vertexs_edges = adjacent_vertex[start_node]
    heapify(adjacent_vertexs_edges)

    while adjacent_vertexs_edges:
        # print(i)
        i += 1
        w, v1, v2 = heappop(adjacent_vertexs_edges)
        if v2 not in closed:
            closed.add(v2)
            mst.append((v1, v2, w))

            for next_vertex in adjacent_vertex[v2]:
                if next_vertex[2] not in closed:
                    heappush(adjacent_vertexs_edges, next_vertex)

    return mst


vertexs = list("ABCDEFG")
edges = [("A", "B", 7), ("A", "D", 5),
         ("B", "C", 8), ("B", "D", 9),
         ("B", "E", 7), ("C", "E", 5),
         ("D", "E", 15), ("D", "F", 6),
         ("E", "F", 8), ("E", "G", 9),
         ("F", "G", 11)]

print('prim:', Prim(vertexs, edges, 'A'))

# ****************************************************


node = {}
rank = {}


def make_set(point):
    node[point] = point
    rank[point] = 0


def find(point):    # O(LogV)
    if node[point] != point:
        node[point] = find(node[point])
    return node[point]


def merge(point1, point2):
    root1 = find(point1)
    root2 = find(point2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            node[root2] = root1
        else:
            node[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def Kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    mst = set()
    i = 1

    edges = list(graph['edges'])
    edges.sort()    # O(ELogE)
    for edge in edges:  # O(E)
        # print(i)
        i += 1
        weight, v1, v2 = edge
        if find(v1) != find(v2):
            merge(v1, v2)
            mst.add(edge)
    return mst


graph = {
    'vertices': ['A', 'B', 'C', 'D'],
    'edges': {(1, 'A', 'B'), (5, 'A', 'C'), (3, 'A', 'D'), (4, 'B', 'C'), (2, 'B', 'D'), (1, 'D', 'C')}
}

print('Kruskal', Kruskal(graph))

"""
    To find a minimum-cost spanning tree.
    minimum-cost spanning tee:
    1. Can only use the edge of graph
    2. we could only use exactly n-1 edges
    3. The edges we chose can't produce any circle
    
    Prim: 與 Kruskal 不一樣，整個演算法的過程中，被選出的邊只形成一棵樹!!(即每次選最短的邊加入)(像貪心)，
    相較之下 Kruskal 演算法的過程中選出的邊形成樹林
    (因為是樹！！！, 所以圖是沒有方向的)
    
    Kruskal 的圖變成這樣：
                        c(2) 
                       / \
                      B(1) D(0)
                     /
                    A(0) (線條都為一條由下往上指的箭頭) (括號為 rank 的值)
    According to the data structure textbook:
    The technique that Kruskal used is called: union-find !!!
    rank findset makeset union 的觀念可以看底下這部：
    https://www.youtube.com/watch?v=ID00PMy0-vEhttps://www.youtube.com/watch?v=ID00PMy0-vE
    
    Time Complexity of Kruskal: O(ELogE) + O(E* LogV) ~= O(ELogE)
    Space Complexity = O(E)
    
    Time Complexity of Prim = O(V^2), if we use binary heap(priority queue) to optimize it then would be O(ELogE)
    
    https://www.itread01.com/content/1549869855.html
    
    https://zhuanlan.zhihu.com/p/61628249
"""
