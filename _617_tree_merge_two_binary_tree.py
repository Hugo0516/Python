# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)

        return root


"""
    Reference: Hua Hua
    https://www.youtube.com/watch?v=EmVsf2sMNiU
    
    t.ly/E4HN
    
    此方法較慢, 因為每次都新創了一個 root 節點( # 16)
    Time Complexity: O(n1 + n2)
    Space Complexity: O(n), n 為 t1, t2 之交集
    
"""
