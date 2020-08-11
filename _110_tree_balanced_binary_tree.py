# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.balanced = True    # 這點很重要，因為一改變所有 recursion 中的 balanced 就會被改變 (看 c++ 版本即可得知)

        def height(root):
            if not root or not self.balanced:   # 左子樹 or 右子樹其中一個不平衡就可以返回false, 不用浪費時間
                return 0
            l = height(root.left)   # 當前node的左子樹 的高度
            r = height(root.right)
            if abs(l - r) > 1:
                self.balanced = False
                # return 0
            return max(l, r) + 1

        height(root)
        return self.balanced


if __name__ == '__main__':
    demo = Solution()
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    left_2 = TreeNode(15)
    right_2 = TreeNode(7)

    root.left = left
    root.right = right
    right.left = left_2
    right.right = right_2
    print(demo.isBalanced(root))

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    print(demo.isBalanced(root2))

"""
    葉子節點的高度 = 0 !!!!!!!!
    
    Given a binary tree, determine if it is height-balanced.
    Balanced binary tree = height-balanced tree = AVL tree
    Time Complexity: O(n)
    這題時間複雜度 有點難估計！！！！！！！
    重看！！！！！！
    花花的別的方法：
    worst time complexity: O(n) + 2*O(n/2) + 4*O(n/4) = O(NLogN)
    
                r 
        H(L)  /   \ H(R)
            L       R
    isBalanced(r) = abs(H(L) - H(R)) <= 1 and isBalanced(r->L) and isBalanced(r->R)
    height(r) = 0, if r is null, 
                max(height(r->L), height(r->R)) + 1, otherwise
    
    看一下！！！！ 另一個解法是O(NLogN) 比較不好：
    http://zxi.mytechroad.com/blog/leetcode/leetcode-110-balanced-binary-tree/
"""
