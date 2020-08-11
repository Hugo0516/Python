class BiTNode:
    def __init__(self, data=None):
        self.data = data
        self.lchild = None
        self.rchild = None


def createDupTree(root):
    # 二叉树根结点
    dupTree = BiTNode()
    if root:
        # 复制左子树
        dupTree.lchild = createDupTree(root.lchild)
        # 复制右子树
        dupTree.rchild = createDupTree(root.rchild)
        dupTree.data = root.data
        return dupTree
    return None

# 用偶自己寫的 即可
def printTreeMidOrder(root):
    if root == None:
        return
        # 遍历root结点的左子树
    if root.lchild != None:
        printTreeMidOrder(root.lchild)

    # 遍历Root结点的右子树
    if root.rchild != None:
        printTreeMidOrder(root.rchild)
        print(root.data)


def level_order(root: BiTNode):
    if root is None:
        return
    queue = [root]

    while queue:
        print(queue[0].data, end=' ')
        curr = queue.pop(0)

        if curr.lchild:
            queue.append(curr.lchild)
        if curr.rchild:
            queue.append(curr.rchild)


input_1 = BiTNode(1)
input_1.lchild = BiTNode(2)
input_1.rchild = BiTNode(3)
# input_1.lchild.lchild = BiTNode(4)
# input_1.lchild.rchild = BiTNode(5)
# input_1.rchild.lchild = BiTNode(6)
# input_1.rchild.rchild = BiTNode(7)
# input_1.lchild.lchild.lchild = BiTNode(8)
level_order(input_1)
print("\n")

dup_tree = createDupTree(input_1)

level_order(dup_tree)
