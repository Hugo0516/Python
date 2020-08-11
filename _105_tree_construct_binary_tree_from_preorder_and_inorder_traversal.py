# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root

"""
    和 106 互相比較 
    解決本題需要牢牢掌握先序遍歷和中序遍歷的含義，以及遞歸。

    先序遍歷：根節點，左子樹的先序遍歷，右子樹的先序遍歷。
    中序遍歷：左子樹的中序遍歷，根節點，右子樹的中序遍歷。

    可以看出，先序遍歷的開頭第一個元素是根元素。找到根節點在中序遍歷中的位置，則可以利用根節點將中序遍歷的數組分割出左右子樹。
    再根據左右子樹的長度對先序遍歷的數組切片。使用遞歸則可以構建出完整的樹。

    很多朋友不理解遞歸，這裡多說一下怎麼理解遞歸。首先一定要明確遞歸函數的定義、其輸入和輸出是什麼，而不用明白該函數內部具體是怎麼實現的。
    我們將遞歸函數當做黑盒使用，也當做普通函數使用，一定不要試圖用大腦理解該遞歸函數內部是怎麼遞歸的，很容易繞進去。即，我不需要知道這個函數怎麼實現的，我調用這個函數就是能實現某個功能。

    比如對於本題而言，buildTree(preorder, inorder)函數的輸入是一棵樹的先序遍歷序列和中序遍歷序列，該函數的返回值是構建好的這棵樹的根節點。
    我們在找到root節點後，設定其左右子樹時，依然調用buildTree(preorder, inorder)，
    此時的輸入變成了root左右子樹對應的先序遍歷和中序遍歷序列，該函數的返回值就是構建好的左右子樹的根節點。

    至此代碼就寫完了，我們看到構建root的左右子樹時，直接使用buildTree(preorder, inorder)函數，只要給定正確的輸入，這個函數就能給正確的輸出，不用去向這個函數到底乾了什麼。

    這樣理解遞歸是不是更清晰了呢？

    t.ly/ygUX
"""

if __name__ == '__main__':
    demo = Solution()
    root_1 = TreeNode(3)
    root_1.left = TreeNode(9)
    root_1.right = TreeNode(20)
    root_1.right.left = TreeNode(15)
    root_1.right.right = TreeNode(7)

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    preorder_2 = [3, 9, 6, 8, 20, 15, 7]
    inorder_2 = [6, 9, 8, 3, 15, 20, 7]
    print(demo.buildTree(preorder_2, inorder_2))