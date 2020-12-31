"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        pass


class Solution2:
    def maxDepth(self, root: 'Node') -> int:

        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1


class Solution3:
    def maxDepth(self, root: 'Node') -> int:

        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                for c in root.children:
                    stack.append((current_depth + 1, c))

        return depth


"""
Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Approach 2: Recursion

Time Complexity: O(N)
Space Complexity: O(LogN)

Approach 3: Iteration

Time Complexity: O(N)
Space Complexity: O(N)

"""
