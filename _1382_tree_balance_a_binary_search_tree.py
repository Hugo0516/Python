# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        stack = []

        def inorder(root: TreeNode):
            if not root:
                return
            else:
                inorder(root.left)
                stack.append(root.val)
                inorder(root.right)

        def build(left: int, right: int):
            if left > right:
                return None

            mid = left + (right - left) // 2
            # 藉由 27~29, 我們可以保證高度差 < 1
            node = TreeNode(stack[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        inorder(root)
        return build(0, len(stack) - 1)


"""
Reference: Hua Hua

Time Complexity: O(n)
Space Complexity: O(n)

*** 這一題要了解題目要考察的點是什麼 ***
=> 並不是要我們創一個 紅黑數 or AVL tree, 我們只是要把一棵樹變成平衡這樣, 不用想得太複雜
"""

if __name__ == '__main__':
    demo = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)

    output_1 = demo.balanceBST(root)
    stack = []


    def inorder(root: TreeNode):
        if root:
            inorder(root.left)
            stack.append(root.val)
            inorder(root.right)


    inorder(output_1)
    print(stack)

    print(output_1.left.val, output_1.val, output_1.right.val, output_1.right.right.val, end=' ')
