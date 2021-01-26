from collections import defaultdict
from typing import List


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertx = set()

    def add_edge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)
        self.vertx.add(start)
        self.vertx.add(end)

    def topological_sort_util(self, i: int, tmp: List, visited: set) -> List:
        visited.add(i)
        tmp.append(i)

        for neighbor in self.graph[i]:
            if neighbor not in visited:
                self.topological_sort_util(neighbor, tmp, visited)

        return tmp

    def topological_sort(self) -> List:
        visited = set()
        connected_component = []

        for index in self.vertx:
            if index not in visited:
                connected_component.append(self.topological_sort_util(index, [], visited))

        return connected_component


class Graph2:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertex = set()

    def add_edge(self, start, end=None):
        self.graph[start].append(end)
        self.vertex.add(start)
        if end:
            self.vertex.add(end)

    def topological_sort_util(self, i: int, tmp: List, visited: set) -> List:
        visited.add(i)
        tmp.append(i)

        for neighbor in list(self.graph.keys()):
            if neighbor not in visited:
                self.topological_sort_util(neighbor, tmp, visited)

        return tmp

    def topological_sort(self) -> List:
        visited = set()
        connected_component = []

        for index in self.vertex:
            if index not in visited:
                connected_component.append(self.topological_sort_util(index, [], visited))

        return connected_component


"""
2021 / 01 / 07, Finished by myself.
Approach 1: For undirected disconnected component

Time Complexity: O(V+E)
Space Complexity: O(V)

Approach 2: For strongly disconnected connected component

Time Complexity: O(V+E)
Space Complexity: O(V)

複雜度我猜想的 !!! 
"""
if __name__ == '__main__':
    demo = Graph()
    demo.add_edge(0, 1)
    demo.add_edge(0, 2)
    demo.add_edge(2, 3)
    demo.add_edge(1, 3)
    demo.add_edge(4, 5)
    demo.add_edge(5, 6)
    demo.add_edge(6, 7)

    print('This is an undirected dis-connected component')
    print(demo.topological_sort())  # [[0, 1, 3, 2], [4, 5, 6, 7]]

    demo2 = Graph2()
    demo2.add_edge(0, 1)
    demo2.add_edge(2)
    print('directed strongly connected component')
    print(demo2.topological_sort())
