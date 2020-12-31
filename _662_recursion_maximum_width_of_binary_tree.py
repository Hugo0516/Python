# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_width = 0
        # queue of elements [(node, col_index)]
        queue = deque()
        queue.append((root, 0))

        while queue:
            level_length = len(queue)
            _, level_head_index = queue[0]
            # iterate through the current level
            for _ in range(level_length):
                node, col_index = queue.popleft()
                # preparing for the next level
                if node.left:
                    queue.append((node.left, 2 * col_index))
                if node.right:
                    queue.append((node.right, 2 * col_index + 1))

            # calculate the length of the current level,
            #   by comparing the first and last col_index.
            max_width = max(max_width, col_index - level_head_index + 1)

        return max_width


class Solution2:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        # table contains the first col_index for each level
        first_col_index_table = {}
        max_width = 0

        def DFS(node, depth, col_index):
            nonlocal max_width
            if node is None:
                return
            # if the entry is empty, set the value
            if depth not in first_col_index_table:
                first_col_index_table[depth] = col_index

            max_width = max(max_width, col_index - first_col_index_table[depth] + 1)

            # Preorder DFS, with the priority on the left child
            DFS(node.left, depth + 1, 2 * col_index)
            DFS(node.right, depth + 1, 2 * col_index + 1)

        DFS(root, 0, 0)

        return max_width


"""
Approach 1: BFS Traversal

Time Complexity: O(N) 
Space Complexity: O(N)

Approach 2: DFS Pre-order Traversal 

Time Complexity: O(N)
Sapce Complexity: O(N)
=> 這裡一定要用 pre order, 因為我們要最先得到 leftmost child of the certain depth
=> 這樣才能確保 line 53, 放入的是最左邊的數字

*** 這一題的重點!!! ***
要找到 node 與 node.leftchildren 和 node.rightchildren 的關係！！！
if root = C, C 設定從 0 開始才會符合底下關係
=> left child of root = 2C
=> right child of root = 2C + 1

"""

if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)

    print(demo.widthOfBinaryTree(root))
    print(demo2.widthOfBinaryTree(root))

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    root2.right.right = TreeNode(9)
    root2.right.right.right = TreeNode(7)
    root2.right.right.left = TreeNode(6)
    print(demo2.widthOfBinaryTree(root2))
