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
                # temp = self.dfs2(graph, neighbor, visited, temp)
                self.dfs2(graph, neighbor, visited, temp)
        # return temp

    def connected(self, graph, visited):
        conected_component = []
        for index in range(self.nums):  # 就這一行跟DFS 的觀念有出入！！！！！ 注意！！
            if index not in visited:
                temp = []  # 這個也很重要, 要確保新的乾淨的[]
                # conected_component.append(self.dfs2(graph, index, visited, temp))
                self.dfs2(graph, index, visited, temp)
                conected_component.append(temp)
                # conected_component += temp    # += 會以concatenate 的方式一一取出elements 然後再放入List裡面
        return conected_component


# 我上面註解的地方 可以多想想, 看到底自己喜歡哪一種格式

"""
    Time complexity of above solution is O(V + E) as it does simple DFS for given graph.
    
    這一題的思路跟資結課本可以說是99% 一樣，而DFS 也是跟這個很像
    
    思路：為何要54行?
    假設現在圖： 0-1-2-3 連在一起, 4-5-6-7連在一起 (所以有兩個forest)
    那麼54行低一次跑的時候發現 0不在 visited 裡面, 所以對0做dfs, 做完後會發現 0-1-2-3連在一起, 並且 0,1,2,3皆變成 visited
    所以之後1-2-3不用再重做DFS, 所以到4的時候又要做DFS, 結果發現4-5-6-7連在一起這樣
    
    注意：graph 表示方法：
    method1 : graph = { '0':[....],
                        '1':[....],
                            .....
                                    }
    method 2: [[...], [.....], [,,,,,]]
    總結！！！！！！！！ List 和 graph裡面都必須包 List!!!!!!!!!!!!
    
    https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
"""

if __name__ == "__main__":
    # Create a graph given in the above diagram
    # 5 vertices numbered from 0 to 4
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(3, 4)
    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc, '\n')

    res = set()
    cc2 = g.connected(g.adj, res)
    print(cc2)
