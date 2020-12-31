import collections
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []

        cur = [root]
        nex = []
        result = []

        while cur:
            tmp = []
            for n in cur:
                tmp.append(n.val)
                for c in n.children:
                    nex.append(c)
            result.append(tmp)
            cur = nex
            nex = []

        return result


class Solution2:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            result.append(level)
        return result


class Solution3:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        result = []
        previous_layer = [root]

        while previous_layer:
            current_layer = []
            result.append([])
            for node in previous_layer:
                result[-1].append(node.val)
                current_layer.extend(node.children)
            previous_layer = current_layer
        return result


class Solution4:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        def traverse_node(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        result = []

        if root is not None:
            traverse_node(root, 0)
        return result


"""
Approach 2: Breadth-first Search using a Queue

Time Complexity: O(N)
Space Complexity: O(N)

Approach 3: Simplified Breadth-first Search

Time Complexity: O(N)
Space Complexity: O(N)

Approach 4: Recursion

Time Complexity: O(N)
Space Complexity: O(LogN)
"""

if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()
    demo3 = Solution3()
    demo4 = Solution4()

    root = Node(1)
    root2 = Node(3)
    root3 = Node(2)
    root4 = Node(4)
    root.children = [root2, root3, root4]
    root5 = Node(5)
    root6 = Node(6)
    root2.children = [root5, root6]

    print(demo.levelOrder(root))
