# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre, self.first, self.second = None, None, None
        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.first:
                self.first = self.pre
            self.second = root
        self.pre = root
        self.inOrder(root.right)


"""
    這一題一看到 BST, 就要想到 in-order traversal, 因為結果會是有序的!!!!!!!!!!
    
    Time Complexity: O(n) (因為每個都要遍歷) / Space Complexity: O(n)(因為每個node都要存) 
    錯誤的位置關係：兩個錯誤的nodes在隔壁而已 or 兩個錯誤的 nodes 不在隔壁
    EX: 1 2 3 4 5 or 1 2 3 4 5
        1 3 2 4 5 or 1 4 3 2 5
    (明顯 3, 2要互換)/(這裡機器要想說 到底是3, 4換 還是 4, 2換 還是 2, 3換) 
    
    t.ly/nMiJ
"""

if __name__ == '__main__':
    demo = Solution()
    root_1 = TreeNode(1)
    root_1.left = TreeNode(3)
    root_1.left.right = TreeNode(2)

    root_2 = TreeNode(3)
    root_2.left = TreeNode(1)
    root_2.right = TreeNode(4)
    root_2.right.left = TreeNode(2)

    print(demo.inOrder(root_1))
    print(demo.inOrder(root_2))
