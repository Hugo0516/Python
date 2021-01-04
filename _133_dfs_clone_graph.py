# Definition for a Node.
import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        node_copy = self.dfs(node, dict())
        return node_copy

    def dfs(self, node, hashd):
        if not node:
            return None
        if node in hashd:
            return hashd[node]

        node_copy = Node(node.val, [])
        hashd[node] = node_copy

        for n in node.neighbors:
            n_copy = self.dfs(n, hashd)
            if n_copy:
                node_copy.neighbors.append(n_copy)

        return node_copy


class Solution2(object):

    def __init__(self):
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        # If the node was already visited before.
        # Return the clone from the visited dictionary.
        if node in self.visited:
            return self.visited[node]

        # Create a clone for the given node.
        # Note that we don't have cloned neighbors as of now, hence [].
        clone_node = Node(node.val, [])

        # The key is original node and value being the clone node.
        self.visited[node] = clone_node

        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node


class Solution3:

    def cloneGraph(self, node: 'Node') -> 'Node':
        que = collections.deque()
        hashd = dict()
        que.append(node)
        node_copy = Node(node.val, [])
        hashd[node] = node_copy

        while que:
            t = que.popleft()
            if not t:
                continue

            for n in t.neighbors:
                if n not in hashd:
                    hashd[n] = Node(n.val, [])
                    que.append(n)
                hashd[t].neighbors.append(hashd[n])

        return node_copy


class Solution4:

    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = collections.deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]


"""
解題思路：
1. 找到圖中所有的點
2. 複製所有找到的點, 並一一對應 => 一一對應, 想到 Map 映射關係 !
3. 複製點的邊

Approach 1: DFS

Time Complexity:
Space Complexity:

Approach 2 : Leetcode DFS

Time Complexity: O(N+M), where N is the number of nodes and M is the number of edges

Space Complexity: O(N),This space is occupied by the visited hash map and in addition to that, 
space would also be occupied by the recursion stack since we are adopting a recursive approach here. 
The space occupied by the recursion stack would be equal to O(H) 
where H is the height of the graph. Overall, the space complexity would be O(N). 

Approach 3: BFS

Time Complexity:
Space Complexity:

Approach 4: Leetcode BFS 

Time Complexity: O(N+M), where N is the number of nodes and M is the number of edges

Space Complexity: O(N),This space is occupied by the visited hash map and in addition to that, 
space would also be occupied by the recursion stack since we are adopting a recursive approach here. 
The space occupied by the recursion stack would be equal to O(H) 
where H is the height of the graph. Overall, the space complexity would be O(N). 

"""

if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()
    demo3 = Solution3()
    demo4 = Solution4()

    root = Node(1)
    root2 = Node(2)
    root3 = Node(3)
    root4 = Node(4)
    root.neighbors = [root2, root4]
    root2.neighbors = [root, root3]
    root3.neighbors = [root2, root4]
    root4.neighbors = [root, root3]

    res = demo.cloneGraph(root)
    res2 = demo2.cloneGraph(root)
    res3 = demo3.cloneGraph(root)
    res4 = demo4.cloneGraph(root)
