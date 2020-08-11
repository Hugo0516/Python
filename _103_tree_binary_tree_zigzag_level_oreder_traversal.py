# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return []
        queue = collections.deque()
        queue.append(root)
        order = 1

        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if order % 2 == 0:
                res.append(level[::-1])
                order += 1
            else:
                res.append(level)
                order += 1

        return res

"""
    這一題是我自己想出來的喔！！！！
    嘻嘻
"""

if __name__ == '__main__':
    demo = Solution()
    root_1 = TreeNode(3)
    root_1.left = TreeNode(9)
    root_1.right = TreeNode(20)
    root_1.right.left = TreeNode(15)
    root_1.right.right = TreeNode(7)

    root_2 = TreeNode(3)
    root_2.left = TreeNode(9)
    root_2.right = TreeNode(20)
    root_2.left.left = TreeNode(6)
    root_2.left.right = TreeNode(8)
    root_2.right.left = TreeNode(15)
    root_2.right.right = TreeNode(7)

    print(demo.zigzagLevelOrder(root_1))
    print(demo.zigzagLevelOrder(root_2))
