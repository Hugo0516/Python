import collections
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root == None:
            return res

        queue = [root]
        print(len(queue))
        while len(queue) != 0:
            res.append([node.val for node in queue])
            new_q = []
            # queue.pop(0)
            for node in queue:
                if node.left:
                    new_q.append(node.left)
                    # queue.append(node.left)
                if node.right:
                    new_q.append(node.right)
                    # queue.append(node.right)
            # queue.pop(0)
            queue = new_q

        return res

    def levelOrder2(self, root):
        res = []
        if not root:
            return res

        queue = collections.deque()
        abc = deque()
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res


"""
    解題思路:
            https://blog.csdn.net/coder_orz/article/details/51363095
            
            https://blog.csdn.net/fuxuemingzhu/article/details/79616156
            
"""

if __name__ == '__main__':
    demo = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # print(demo.levelOrder(root))
    print(demo.levelOrder2(root))
