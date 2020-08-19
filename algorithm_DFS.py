graph = {
    'a': ['b', 'c'],
    'b': ['a', 'c', 'd'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['b', 'c', 'e', 'f'],
    'e': ['c', 'd'],
    'f': ['d']
}

# Using a Python dictionary to act as an adjacency list
graph2 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

graph3 = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1, 7],
    4: [1, 7],
    5: [2, 7],
    6: [2, 7],
    7: [3, 4, 5, 6]
}


def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print(vertex, end=' ')


# DFS(graph, 'a')
# print('')
print("Iteration version")
# DFS(graph2, 'A')
print('')
DFS(graph3, 0)
print('\n')


def DFS1(graph, s, queue=[]):
    queue.append(s)
    for i in graph[s]:
        if i not in queue:
            DFS1(graph, i, queue)
    return queue


# print(DFS1(graph, 'a'))
# print('')

"""
    DFS is very similar with pre-order traversal method
    DFS 版本比 DFS1 版本好， 畢竟是用stack的概念下去，感覺比較好(個人覺得啦) !!!!
    
    Time Complexity: 
    
    https://zhuanlan.zhihu.com/p/61628249
    
    DFS 的應用：
    https://www.geeksforgeeks.org/applications-of-depth-first-search/
"""

# Using a Python dictionary to act as an adjacency list
graph2 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

graph3 = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1, 7],
    4: [1, 7],
    5: [2, 7],
    6: [2, 7],
    7: [3, 4, 5, 6]
}

visited = set()  # Set to keep track of visited nodes.
i = 1


def dfs2(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        # print(input_1)
        # input_1 += 1
        for neighbour in graph[node]:
            dfs2(visited, graph, neighbour)


def dfs3(graph, node, visited, res):
    visited.add(node)
    res.append(node)
    print(node, end=' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs3(graph, neighbor, visited, res)


# Driver Code
# dfs2(visited, graph2, 'A', i)
# dfs2(visited, graph3, 0)
# visited = set()
# print('\n')

print("Recursion version")
res = []
visited = set()
# dfs3(graph2, 'A', visited, res)
dfs3(graph3, 0, visited, res)
print('')
print(res)

"""
    Time Complexity:
    Since all the nodes and vertices are visited, the average time complexity for DFS on a graph is O(V + E),
    where V is the number of vertices and E is the number of edges.
    Space complexity : O(n) 因為每個點都存進去惹
    In case of DFS on a tree, the time complexity is O(V), where V is the number of nodes.
    
    Note: We say average time complexity because a set’s in operation has an average time complexity of O(1).
    If we used a list, the complexity would be higher.
    
    記住dfs2 或 dfs3 版本！！！！ (頂多再加 DFS 版本)
    DFS3 最棒惹
    
    這裡用有向圖當作範例
    
                    A
                  /   \
                 B     C
                / \     \
               D   E---> F
    https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
"""
