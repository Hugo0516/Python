# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # recursive method
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

    # iterative method
    def invertTree2(self, root):
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
        return root


"""
    Reference: Michelle
    t.ly/IcU8
    
    Time Complexity:
    Space Complexity: 
"""

demo = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

output_1 = demo.invertTree(root)

