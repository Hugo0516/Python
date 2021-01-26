# Python program to check if a given directed graph is strongly
# connected or not

from collections import defaultdict


# This class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by isSC() to perform DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

            # Function that returns reverse (or transpose) of this graph

    def getTranspose(self):

        g = Graph(self.V)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)

        return g

    # The main function that returns true if graph is strongly connected
    def isSC(self):

        # Step 1: Mark all the vertices as not visited (For first DFS)
        visited = [False] * (self.V)

        # Step 2: Do DFS traversal starting from first vertex.
        self.DFSUtil(0, visited)

        # If DFS traversal doesnt visit all vertices, then return false
        if any(i == False for i in visited):
            return False

        # Step 3: Create a reversed graph
        gr = self.getTranspose()

        # Step 4: Mark all the vertices as not visited (For second DFS)
        visited = [False] * (self.V)

        # Step 5: Do DFS for reversed graph starting from first vertex.
        # Staring Vertex must be same starting point of first DFS
        gr.DFSUtil(0, visited)

        # If all vertices are not visited in second DFS, then
        # return false
        if any(i == False for i in visited):
            return False

        return True


# Python implementation of Kosaraju's algorithm to print all SCCs

from collections import defaultdict


# This class represents a directed graph using adjacency list representation
class Graph2:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        print(v)
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    # The main function that finds and prints all strongly
    # connected components
    def printSCCs(self):

        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited = [False] * (self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

            # Create a reversed graph
        gr = self.getTranspose()

        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * (self.V)

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited)
                print("")


"""
How to check whether the graph is strongly connected or not?
1. If a graph is undirected:
1-1 It is easy for undirected graph, we can just do a BFS and DFS starting from any vertex.
1-2 If BFS or DFS visits all vertices, then the given undirected graph is connected.

2. If a graph is directed:
2-1 A directed graph is strongly connected if there is a path between any two pair of vertices.
2-2 We cannot just use DFS or BFS to traverse it.

==> We have 3 solutions:
3-1 A simple idea is to use a all pair shortest path algorithm like Floyd Warshall or
find Transitive Closure of graph. Time complexity of this method would be O(v3).

3-2 We can also do DFS V times starting from every vertex. If any DFS,
doesn’t visit all vertices, then graph is not strongly connected.
This algorithm takes O(V*(V+E)) time which can be same as transitive closure for a dense graph.

3-3 A better idea can be Strongly Connected Components (SCC) algorithm.
We can find all SCCs in O(V+E) time. If number of SCCs is one, then graph is strongly connected.
The algorithm for SCC does extra work as it finds all SCCs.

*** We use 3-2 as a solution over here ***
Time Complexity: O(V+E)

Reference: https://www.geeksforgeeks.org/connectivity-in-a-directed-graph/?ref=lbp
"""

if __name__ == '__main__':
    # Create a graph given in the above diagram
    g1 = Graph(5)
    g1.addEdge(0, 1)
    g1.addEdge(1, 2)
    g1.addEdge(2, 3)
    g1.addEdge(3, 0)
    g1.addEdge(2, 4)
    g1.addEdge(4, 2)
    print("Yes" if g1.isSC() else "No")  # Yes

    g2 = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    print("Yes" if g2.isSC() else "No")  # No

    # Create a graph given in the above diagram
    g = Graph2(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(3, 4)

    print("Following are strongly connected components " +
          "in given graph")
    g.printSCCs()
