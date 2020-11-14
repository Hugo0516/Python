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
            # return 0
            return -1

        # left = self._univaluePath(root.left) if root.left is not None else -1
        # right = self._univaluePath(root.right) if root.right is not None else -1
        left = self._univaluePath(root.left)
        right = self._univaluePath(root.right)
        pl = left + 1 if left >= 0 and root.val == root.left.val else 0     # is same as 38 in 524 leetcode
        pr = right + 1 if right >= 0 and root.val == root.right.val else 0
        # pl = left + 1 if root.val == root.left.val else 0     # 不能改成這樣 因為root.left有可能=null
        # pr = right + 1 if root.val == root.right.val else 0   # 同上

        self.ans = max(self.ans, pl + pr)   # 20 21 29 = Leetcopde #124 的 19行
        return max(pl, pr)
        # 23 24 30 = Leetocde #124 的 21行

"""
    Reference:
    http://zxi.mytechroad.com/blog/tree/leetcode-687-longest-univalue-path/
    
    Time Complexity : O(n)
    Space Complexity: O(n)
    
    可以和 Leetcode # 124 對照
    **** 我 mark 掉的部分 17, 20, 21 為原寫法 => 但 為了跟 543 邏輯相近 我把它們mark掉換寫法
"""
