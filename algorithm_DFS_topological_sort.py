# Python program to print topological sorting of a DAG
from collections import defaultdict


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

            # Push current vertex to stack which stores result
        stack.append(v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):  # This is where the huge difference between with normal DFS
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

            # Print contents of the stack
        print(stack[::-1])  # return list in reverse order


# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")
# Function Call
g.topologicalSort()  # 5, 4, 2, 3, 1, 0

g2 = Graph(3)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 0)
g2.topologicalSort()
print(g2.graph)
"""    
2021 / 01 / 07 updated

Approach 1: Topological sort(DFS version)

Topological sort 不能有環 只能用在 DAG !!!

Besides, 記住 topological sort 的思路是說:
def topological_sort_util():
    ...

def topological():
    for i in every node:    =>> 這一行是關鍵！！！ 我們要把每個 node 都遍歷一遍
        topological_sort_util()
    
Conclusion: 注意每個 node 都要遍歷一遍, 且, 要注意放到 stack 後 要[::-1] !!

Time Complexity: O(V+E). The above algorithm is simply DFS with an extra stack. So time complexity is the same as DFS which is.
Auxiliary space: O(V). The extra space is needed for the stack.
--------------------
比較：
Topological sort vs DFS:
1. Topological sort 需要用上面提到的, 每一個點都要遍歷, 而不是只用 for neighbor in ... 
2. Topological sort 的結果需要先用 stack 存起來, 最後再倒序 print 出來; 而 DFS 則是當下就 print 出來了

Topological sort vs Disconnected Component:
1. Disconnected Component 不能用普通的 DFS 下去做, 因為正如上面所講的普通的 DFS, 不會強迫遍歷每一點, 但是 Disconnected Component 的圖
   需要我強迫遍歷每一點才行
2. 所以, 按照第一點的觀點, Topological sort 的寫法 和 Disconnected Component 一樣, 需要強迫遍歷 !! 
--------------------
In addition, Topological sort 的思路 和 找尋 Disconnected Component 很像！！！！！

Reference:
1. Topological sort
https://www.geeksforgeeks.org/topological-sorting/

2. DFS 的相關運用以及延伸
https://www.geeksforgeeks.org/applications-of-depth-first-search/


"""
