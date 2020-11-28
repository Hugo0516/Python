# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # iterative method
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pointer = root

        while pointer:
            if p.val < pointer.val and q.val < pointer.val:
                pointer = pointer.left
            elif p.val > pointer.val and q.val > pointer.val:
                pointer = pointer.right
            else:
                return pointer

    # recursive method
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                break
        return root


"""
    Reference: Michelle
    https://www.youtube.com/watch?v=B48MMwTlRuA
    
    Time Complexity : O(N), where N is the number of nodes in the BST. 
    In the worst case we might be visiting all the nodes of the BST.
    Time Complexity 我覺得怪怪的, 不是O(LogN)???
    
    Space Complexity : O(1). 
    
    Related: LC 236
    因為這題是 236 題的特例, 所以用236題的方法直接複製貼上也會過
"""
if __name__ == '__main__':
    demo = Solution()
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    output = demo.lowestCommonAncestor(root, root.left, root.right)
    print(output.val)
