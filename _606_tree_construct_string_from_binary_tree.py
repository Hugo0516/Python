# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""

        s = str(t.val)
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)

        if t.left is None and t.right is None:
            return s
        if t.right is None:
            return s + "(" + left + ")"

        return s + "(" + left + ")" + "(" + right + ")"


class Solution2:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        stack = [t]
        visited = set()
        s = ""
        while stack:
            t = stack[-1]
            if t in visited:
                stack.pop()
                s += ")"
            else:
                visited.add(t)
                s += ("(" + str(t.val))
                if t.left is None and t.right is not None:
                    s += "()"
                if t.right is not None:
                    stack.append(t.right)
                if t.left is not None:
                    stack.append(t.left)

        return s[1:len(s) - 1]


"""
Reference: Hua Hua
=> Recursion, 最重要的是先找到終止條件 => 再來是 遞迴關係 => 最後 return

Case 1: Both the left child and the right child exist for the current node.
Case 2: None of the left or the right child exist for the current node.
Case 3: Only the left child exists for the current node.
Case 4: Only the right child exists for the current node. 

Approach 1: pre-order recursion

Time Complexity: O(n), The preorder traversal is done over the n nodes of the given Binary Tree.
Space Complexity: O(n), The depth of the recursion tree can go upto n in case of a skewed tree.

*** 要注意 test case ***, case 4 特別重要

Approach 2: Iterative method using stack, pre-order's stack version

Time Complexity: O(n)
Space Complexity: O(n)
"""

if __name__ == '__main__':
    demo = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.right = TreeNode(4)

    print(demo.tree2str(root))
    print(demo.tree2str(node))
    print('-----')

    demo2 = Solution2()
    print(demo2.tree2str(root))
