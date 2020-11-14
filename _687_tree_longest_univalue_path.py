# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        self._univaluePath(root)
        return self.ans

    def _univaluePath(self, root):
        if root is None:
            return 0

        left = self._univaluePath(root.left) if root.left is not None else -1
        right = self._univaluePath(root.right) if root.right is not None else -1
        pl = left + 1 if left >= 0 and root.val == root.left.val else 0
        pr = right + 1 if right >= 0 and root.val == root.right.val else 0
        self.ans = max(self.ans, pl + pr)   # 21 22 23 = Leetcopde #124 的 19行
        return max(pl, pr)
        # 21 22 24 = Leetocde #124 的 21行

"""
    Reference:
    http://zxi.mytechroad.com/blog/tree/leetcode-687-longest-univalue-path/
    
    Time Complexity : O(n)
    Space Complexity: O(n)
    
    可以和 Leetcode # 124 對照
"""
