class TreeNode:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None



def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def height2(root):
    if not root:   # 左子樹 or 右子樹其中一個不平衡就可以返回false, 不用浪費時間
        return -1   # 也可以從 0 開始, 看你想要怎樣
    l = height2(root.left)   # 當前node的左子樹 的高度
    r = height2(root.right)
    return max(l, r) + 1


root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.left.left.left = TreeNode(6)
root2.left.left.right = TreeNode(7)

print(height(root2))
print(height2(root2))