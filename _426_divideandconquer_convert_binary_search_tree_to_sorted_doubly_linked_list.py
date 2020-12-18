# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal last, first
            if node:
                # left
                helper(node.left)
                # node
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    # to close DLL later on
                    first = node
                last = node
                # right
                helper(node.right)

        if not root:
            return None

        # the smallest (first) and the largest (last) nodes
        first, last = None, None
        helper(root)
        # close DLL
        last.right = first
        first.left = last
        return first


"""
這題為什麼要用 inorder 呢？ => 因為我們看他圖給的範例剛好最左下角是最小的(即:要被當成 first)(因為是 BST, 所以才是最小)
所以我們採用 inorder, 因為 inorder 第一個 append 的數字會是最左下角

Time Complexity: O(N), since each node is processed exactly once.

Space Complexity: O(N), We have to keep a recursion stack of the size of the tree height, 
which is O(logN) for the best case of completely balanced tree 
and O(N) for the worst case of completely unbalanced tree.
"""

if __name__ == '__main__':
    demo = Solution()
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    output_1 = demo.treeToDoublyList(root)
    tmp = output_1.val

    while output_1:
        print(output_1.left.val, output_1.val, output_1.right.val, end='/')
        output_1 = output_1.right

        if output_1.val == tmp:
            break
