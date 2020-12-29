# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root

        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)


class Solution2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right

        return root


"""
Approach 1: Recursion

Time Complexity: O(H), where H is the tree height. That results in O(LogN)
in the average case, and O(N) in the worst case.

Space Complexity: O(H) to keep the recursion stack, O(LogN) in the average case,
and O(N) in the worst case.

Approach 2: Iteration

Time Complexity: O(H)
Space Complexity: O(1)
"""

if __name__ == '__main__':
    pass
