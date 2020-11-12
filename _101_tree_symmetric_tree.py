# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)


class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:

        def helper(node_1, node_2):
            if not node_1 and not node_2:
                return True
            elif not node_1 or not node_2:
                return False
            return node_1.val == node_2.val and helper(node_1.left, node_2.right) and helper(
                node_1.right, node_2.left)

        if not root:
            return True

        return helper(root.left, root.right)


"""
    Follow up: Solve it both recursively and iteratively.!!!!!
    
    和100題的解法很像, 都是採用pre-order 的方式
    
    定義新函數isMirror(left, right)，該函數的意義是判斷left和right是不是對稱的子樹。當left和right的值相等的時候，需要判斷下一層是否是對稱的。
    在遞歸判斷下一層的時候的時候，需要判斷的是left.left和right.right這兩棵樹是不是對稱的，以及left.right和right.left這兩棵樹是不是對稱的。
    
    代碼只是上面的思路的實現，可以用遞歸來完成。遞歸最重要的是要明白函數的定義、輸入、輸出，如果這些沒明白一定會把自己繞進去。    
    另外遞歸的時候應該把遞歸函數當做黑盒使用，即不需要知道此函數內部怎麼實現的，但是調用這個遞歸函數就是能達到某個功能。這樣會幫助理解遞歸。!!!!!!!!!

    本題提醒了我們：在遞歸的過程中不一定只有一個參數，也可以同時傳了兩個參數，每次遞歸的時候同時改變兩個採納數。

    https://blog.csdn.net/fuxuemingzhu/java/article/details/51345707


"""

if __name__ == '__main__':
    demo = Solution()
    root_1 = TreeNode(1)
    root_1.left = TreeNode(2)
    root_1.right = TreeNode(2)
    root_1.left.left = TreeNode(3)
    root_1.left.right = TreeNode(4)
    root_1.right.left = TreeNode(4)
    root_1.right.right = TreeNode(3)

    root_2 = TreeNode(1)
    root_2.left = TreeNode(2)
    root_2.right = TreeNode(2)
    root_2.left.right = TreeNode(3)
    root_2.right.right = TreeNode(3)

    print(demo.isSymmetric(root_1), demo.isSymmetric(root_2))

    demo2 = Solution2()
    print(demo2.isSymmetric(root_1))