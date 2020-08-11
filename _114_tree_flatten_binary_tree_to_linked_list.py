# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        self.preOrder(root, res)
        for i in range(len(res) - 1):
            res[i].left = None
            res[i].right = res[i + 1]

    def preOrder(self, root, res):
        if not root:
            return
        res.append(root)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)


"""
    看到 binary tree or binary search tree 就先想到 pre-order traversal
    https://blog.csdn.net/fuxuemingzhu/java/article/details/70241424
"""

if __name__ == '__main__':
    demo = Solution()

    root_1 = TreeNode(1)
    root_1.left = TreeNode(2)
    root_1.right = TreeNode(5)
    root_1.left.left = TreeNode(3)
    root_1.left.right = TreeNode(4)
    root_1.right.right = TreeNode(6)

    demo.flatten(root_1)
