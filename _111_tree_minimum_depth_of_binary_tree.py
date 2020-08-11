# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # DFS version
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque()
        queue.append(root)
        depth = 1

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                # 這一行是因為我們每次都一定會放入node.left, node.right 我們不會因為node.l node.r 不存在就不放進去
                # 要記住我們的最後判斷就是要遇到一個 node 其 left 和 right 皆為null(表 leaf)
                if not node:
                    continue
                if not node.left and not node.right:
                    return depth
                queue.append(node.left)
                queue.append(node.right)
            depth += 1
        return depth

    # 如果用104的做法, 這個會錯！！！！
    # 假如輸入[1, 2]會輸出1, 但是正確答案是2 !!!!!!!
    # 所以算這種min的, 要特別確認是否終止為 leaf(請看底下 DFS 的要求)
    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        # if not root.left and not root.right:
        #     return 1
        return 1 + min(self.minDepth2(root.left), self.minDepth2(root.right))

    # BFS version
    def minDepth3(self, root):
        if not root:
            return 0
        left = self.minDepth3(root.left)
        right = self.minDepth3(root.right)
        if not left:
            return right + 1
        if not right:
            return left + 1
        return 1 + min(left, right)


"""
    DFS:
        運用遞歸，遞歸當前和左子樹和右子樹的深度，某節點的左右子樹都是空的時候，說明是葉子。計算根節點到此葉子的深度。
        
        注意：如果是葉子，那麼此葉子的深度是1.
        同時注意：如果有一方的某一子樹為空，那麼它的深度為0，但不應該進入樹的深度的計算當中去。!!!!!!

        Better solution:用HashMap存儲已經遍歷過的樹，減少空間複雜度。實現效率的提高。
        當root為空的時候直接返回0，因為MIN賦值很大，所以如果不單獨預判的話會返回MIN
        判斷樹的深度應該到葉子節點，也就是左右子結點都為空的那個結點
        樹的深度的根節點深度為1
        
        ** 我個人喜歡第一種方法(網頁寫他是DFS, 我個人猜想是因為:程式的第一步都是判斷 node 本身, 接下來才是node.l 然後才 node.r)

        https://blog.csdn.net/fuxuemingzhu/java/article/details/48519035
"""

if __name__ == '__main__':
    demo = Solution()
    root_1 = TreeNode(3)
    root_1.left = TreeNode(9)
    root_1.right = TreeNode(20)
    root_1.right.left = TreeNode(15)
    root_1.right.right = TreeNode(7)

    root_2 = TreeNode(1)
    root_2.left = TreeNode(2)

    root_3 = TreeNode(3)
    root_3.left = TreeNode(9)
    root_3.left.left = TreeNode(15)
    root_1.left.right = TreeNode(17)

    root_4 = TreeNode(1)
    root_4.right = TreeNode(2)

    # print(demo.minDepth(root_1))
    # print(demo.minDepth(root_2))
    # print(demo.minDepth(root_3))
    # print(demo.minDepth3(root_2))
    print(demo.minDepth(root_4))
