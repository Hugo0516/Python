# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, root, min, max):
        if not root:
            return True
        if root.val >= max or root.val <= min:
            return False

        return self.valid(root.left, min, root.val) and self.valid(root.right, root.val, max)

    def isValidBST2(self, root: TreeNode) -> bool:
        res = []
        self.inOrder(root, res)
        return res == sorted(res) and len(res) == len(set(res))

    def inOrder(self, root, res):
        if not root:
            return []
        l = self.inOrder(root.left, res)
        # if l:
        #     res.extend(l)
        # 上面兩句我測過 根本沒用
        res.append(root.val)
        r = self.inOrder(root.right, res)
        # if r:
        #     res.extend()
        # 這裡也是沒用



"""
    解題思路：
            方法一： recursion
            
            方法二: 用 inorder traversal + 比大小 and 不能重複(這題題目的BST tree 一開始就不打算給重複字)
            (所以我們才可以使用此方法)
            t.ly/xkL6
            https://www.youtube.com/watch?v=Jq0Wk9xeQ0U
            
            !!! 藉由這一題可以知道, BST 可以為空(連"根"都沒有)
            
            Both method's time complexity = O(n)
            Space Complexity: O(h)
"""

if __name__ == "__main__":
    demo = Solution()
    root_1 = TreeNode(2)
    root_1.left = TreeNode(1)
    root_1.right = TreeNode(3)

    root_2 = TreeNode(5)
    root_2.left = TreeNode(1)
    root_2.right = TreeNode(4)
    root_2.right.left = TreeNode(3)
    root_2.right.right = TreeNode(6)

    root_3 = TreeNode(10)
    root_3.left = TreeNode(4)
    root_3.left.left = TreeNode(3)
    root_3.left.right = TreeNode(5)
    root_3.right = TreeNode(12)
    root_3.right.left = TreeNode(11)
    root_3.right.right = TreeNode(13)

    print(demo.isValidBST(root_1), demo.isValidBST(root_2))
    print(demo.isValidBST2(root_3))
