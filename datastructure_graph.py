# Create the dictionary with graph elements
graph = {"a": ["b", "c"],
         "b": ["a", "d"],
         "c": ["a", "d"],
         "d": ["e"],
         "e": ["d"]
         }

# Print the graph
print(graph, '\n')


# Display graph vertices
class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

    # Display graph edges
    def edges(self):
        return self.findedges()

    # Add the new edge
    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

    # Find the distinct list of edges
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

    # Add the vertex as a key
    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []


# Create the dictionary with graph elements
graph_elements = {"a": ["b", "c"],
                  "b": ["a", "d"],
                  "c": ["a", "d"],
                  "d": ["e"],
                  "e": ["d"]
                  }

g = graph(graph_elements)
print(g.getVertices(), '\n')

# Display graph edges
print(g.edges(), '\n')

g.addVertex("f")
print(g.getVertices(), '\n')

g.AddEdge({'a', 'e'})
g.AddEdge({'a', 'c'})
print(g.edges(), '\n')

"""
    normally, graph is implemented by adjacency matrix or adjacent list;however,
    in python, we used dictionary to implement graph.
    generally, graph can be implemented by adjacent matrix and adjacent linked-list
    
    adjacency matrix => 用在 complete graph 佳, 判斷邊是否存在 O(1)
    adjacency list => 用在 頂點個數多 邊數極少的 Sparse matrix 佳, 判斷邊要 O(e) 較麻煩
    
"""