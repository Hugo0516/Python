# Definition for a Node.
import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        queue = collections.deque()
        queue.append(root)

        while queue:
            _len = len(queue)
            for i in range(_len):
                node = queue.popleft()
                if i < _len - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


"""
    這議題是用 level-order traversal 的概念下去做
    116 我是寫 pre-order版本, 但是我覺得也可以寫成level-order 版本, 感覺也很直觀
    
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79560379
"""

