# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def wrong(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return sum == 0
        return self.wrong(root.left, sum - root.val) or self.wrong(root.right, sum - root.val)

    # 回溯方法 (即 DFS)
    def hasPathSum2(self, root, sum):
        if not root:
            return False
        res = []
        return self.dfs2(root, sum, res, [root.val])

    def dfs2(self, root, target, res, path):
        # if not root:
        #     return False
        if sum(path) == target and not root.left and not root.right:
            return True
        left_flag, right_flag = False, False
        if root.left:
            left_flag = self.dfs2(root.left, target, res, path + [root.left.val])
        if root.right:
            right_flag = self.dfs2(root.right, target, res, path + [root.right.val])
        return left_flag or right_flag

    def hasPathSum3(self, root, sum):
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == sum:
            return True
        else:
            return self.hasPathSum3(root.left, sum - root.val) or self.hasPathSum3(root.right, sum - root.val)


class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


"""
    法ㄧ:
    這題的觀念很重要!!!!!!
    上面wrong 是錯誤思路！！！！ (和 104, 111 比較)
    
    這種代碼的錯誤在，沒有判斷root是否為葉子節點。比如root為空的話，題目的意思是要返回False的，而上面的代碼會返回sum == 0。
    又比如，對於測試用例樹為[1,2], sum = 0時，上面的結果也會返回為True，因為對於上述代碼，只要左右任意一個孩子的為空時sum == 0就返回True 。
    當題目中提到了葉子節點時，正確的做法一定要同時判斷節點的左右子樹同時為空才是葉子節點。
    
    法二：
    這方法好像不錯? 詳見113
    
    # 30 31 可以省略 (因為, root.l root.r 都是確認過才放進去的)
    
    請見以下解說:
    https://blog.csdn.net/fuxuemingzhu/java/article/details/71715810
    
    
    法三比較好！！！ 非常直覺
    https://www.youtube.com/watch?v=2PjOR354ASs
    
2020 / 12 / 31 updated
Approach: Recursion (我覺得是 top-down)

Time Complexity: O(N)
Space Complexity: O(LogN)
"""

if __name__ == '__main__':
    demo = Solution()
    root_1 = TreeNode(5)
    root_1.left = TreeNode(4)
    root_1.right = TreeNode(8)

    root_1.left.left = TreeNode(11)
    root_1.left.left.left = TreeNode(7)
    root_1.left.left.right = TreeNode(2)

    root_1.right.left = TreeNode(13)
    root_1.right.right = TreeNode(4)
    root_1.right.right.right = TreeNode(1)

    print(demo.hasPathSum(root_1, 22))
    print(demo.hasPathSum(root_1, 27))

    demo2 = Solution2()
    print(demo2.hasPathSum(root_1, 22))
