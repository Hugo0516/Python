# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        def dfs_leftmost(node):
            if (not node.left) and (not node.right):
                # trick: avoid leaf nodes in this pass
                return
            boundary.append(node.val)
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)

        def dfs_leaves(node):
            if (not node.left) and (not node.right):
                boundary.append(node.val)
            if node.left:
                dfs_leaves(node.left)
            if node.right:
                dfs_leaves(node.right)

        def dfs_rightmost(node):
            if (not node.left) and (not node.right):
                return
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        if root.left:
            dfs_leftmost(root.left)
            dfs_leaves(root.left)
        if root.right:
            dfs_leaves(root.right)
            dfs_rightmost(root.right)
        return boundary


"""
Reference: https://leetcode.com/problems/boundary-of-binary-tree/discuss/101308/python-dfs-solution

tricky point=> What does "if not node or not node.left and not node.right:" check?
It checks whether it is a leaf node or not. We are only checking boundary nodes for non-leaf nodes in the left and right functions.

=> 這一題, 搭配圖下去做思考, 就可以想出來, 但是一定要看著圖 (我覺得啦)

Time Complexity: O(n)
Space Complexity: O(n) 
< I guess >
"""

if __name__ == '__main__':
    demo = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)
    root.right.left.left = TreeNode(9)
    root.right.left.right = TreeNode(10)

    print(demo.boundaryOfBinaryTree(root))
