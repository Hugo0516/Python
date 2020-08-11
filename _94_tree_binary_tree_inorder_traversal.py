# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res


if __name__ == '__main__':
    demo = Solution()
    root = TreeNode(1)
    right_1 = TreeNode(2)
    right_2 = TreeNode(3)
    root.right = right_1
    right_1.left = right_2

    print(demo.inorderTraversal(root))
