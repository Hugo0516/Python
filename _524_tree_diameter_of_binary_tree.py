# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iteration version
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = {None: -1}
        s = [root]
        ans = 0

        while s:
            node = s[-1]
            if node.left in d and node.right in d:
                s.pop()
                l = d[node.left] + 1
                r = d[node.right] + 1
                ans = max(ans, l + r)
                d[node] = max(l, r)
            else:
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
        return ans

    # recursion method
    def diameterOfBinaryTree2(self, root: TreeNode) -> int:
        self.ans = 0
        self._helper(root)
        return self.ans

    def _helper(self, root: TreeNode):
        if not root:
            return -1

        left = self._helper(root.left) + 1
        right = self._helper(root.right) + 1
        self.ans = max(self.ans, left + right)
        return max(left, right)


"""
    reference:
    http://zxi.mytechroad.com/blog/tree/leetcode-543-diameter-of-binary-tree/
    
    Time Complexity: O(n)
    Sapce Complexity: O(h)
    
    記住 recursive 作法 即可
    我 iteration 還沒看過
"""
if __name__ == '__main__':
    demo = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.right = TreeNode(6)
    root.left.right.left = TreeNode(7)

    print(demo.diameterOfBinaryTree2(root))
    print(demo.diameterOfBinaryTree(root))
