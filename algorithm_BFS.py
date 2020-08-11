graph = {
    'a': ['b', 'c'],
    'b': ['a', 'c', 'd'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['b', 'c', 'e', 'f'],
    'e': ['c', 'd'],
    'f': ['d']
}

graph2 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


def BFS(graph, s, res):
    queue = [s]
    seen = set()
    seen.add(s)
    while queue:
        vertex = queue.pop(0)   # 這句話重要！！！！
        res.append(vertex)
        print(vertex, end=' ')
        for node in graph[vertex]:
            if node not in seen:
                queue.append(node)
                seen.add(node)


# BFS(graph, 'a')
# print('')
tmp = []
BFS(graph2, 'A', tmp)
print('')
print(tmp)
for i in tmp:
    print(i, end=' ')

"""
                    A
                  /   \
                 B     C
                / \     \
               D   E---> F
    BFS is very similar with level-order traversal 
    BFS 沒有 recursion 版本，因為 BFS 就是利用queue的性質；如果用recursion的話，一定牽扯到stack 的性質
    https://zhuanlan.zhihu.com/p/61628249
    
    https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
    
    BFS 的應用：
    https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/?ref=lbp
"""
