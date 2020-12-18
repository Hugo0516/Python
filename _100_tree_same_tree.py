# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution2:
    def isSameTree(self, p, q):
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True


"""
    這裡解法用 pre-order 的方式, 我想是因為要是 "same" tree, 所以對 val值要求很高, 所以才用 pre-order

    這道題是樹的題目，屬於最基本的樹遍歷的問題。
    問題要求就是判斷兩個樹是不是一樣，基於先序，中序或者後序遍歷都可以做完成，因為對遍歷順序沒有要求。

    這裡我們主要考慮一下結束條件，如果兩個結點都是null，也就是到頭了，那麼返回true。
    如果其中一個是null，說明在一棵樹上結點到頭，另一棵樹結點還沒結束，即樹不相同，或者兩個結點都非空，並且結點值不相同，返回false。
    最後遞歸處理兩個結點的左右子樹，返回左右子樹遞歸的與結果即可。

    https://blog.csdn.net/fuxuemingzhu/java/article/details/51285076
    
    Time Complexity: O(N), where N is a number of nodes in the tree, since one visits each node exactly once.
    Space Complexity:O(log(N)) in the best case of completely balanced tree and 
                     O(N) in the worst case of completely unbalanced tree, to keep a recursion stack. 
"""

if __name__ == '__main__':
    demo = Solution()

    p_1 = TreeNode(1)
    p_1.left = TreeNode(2)
    p_1.right = TreeNode(3)

    p_2 = TreeNode(1)
    p_2.left = TreeNode(2)
    p_2.right = TreeNode(3)

    p_3 = TreeNode(1)
    p_3.left = TreeNode(2)

    p_4 = TreeNode(2)
    p_4.right = TreeNode(1)

    p_5 = TreeNode(1)
    p_5.left = TreeNode(2)
    p_5.right = TreeNode(1)

    p_6 = TreeNode(1)
    p_6.left = TreeNode(1)
    p_6.right = TreeNode(2)

    print(demo.isSameTree(p_1, p_2), demo.isSameTree(p_3, p_4), demo.isSameTree(p_5, p_6))

    demo2 = Solution2()
    print(demo2.isSameTree(p_1, p_2))
