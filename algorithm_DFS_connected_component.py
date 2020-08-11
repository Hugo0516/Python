# Python program to print connected
# components in an undirected graph
class Graph:

    # init function to declare class variables
    def __init__(self, nums):
        self.nums = nums
        self.adj = [[] for i in range(nums)]

    # method to add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def DFSUtil(self, temp, v, visited):
        # Mark the current vertex as visited
        visited[v] = True
        # Store the vertex to list
        temp.append(v)

        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp

    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []  # connected component
        for i in range(self.nums):
            visited.append(False)
        for v in range(self.nums):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc

    # Driver Code

    def dfs2(self, graph, node, visited, temp):
        visited.add(node)
        temp.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                temp = self.dfs2(graph, neighbor, visited, temp)
        return temp

    def connected(self, graph, visited):
        conected_component = []
        for index in range(self.nums):  # 就這一行跟DFS 的觀念有出入！！！！！ 注意！！
            if index not in visited:
                temp = []
                conected_component.append(self.dfs2(graph, index, visited, temp))
        return conected_component



if __name__ == "__main__":
    # Create a graph given in the above diagram
    # 5 vertices numbered from 0 to 4
    g = Graph(5);
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(3, 4)
    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc, '\n')

    res = set()
    cc2 = g.connected(g.adj, res)
    print(cc2)

"""
    Time complexity of above solution is O(V + E) as it does simple DFS for given graph.
    
    這一題的思路跟資結課本可以說是99% 一樣，而DFS 也是跟這個很像
    
    https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
"""
