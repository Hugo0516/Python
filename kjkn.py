print([2] + [2])


def qq(x, a, b):
    x + 'ww'


x = "aa"
qq(x, 11, 15)
print(x)


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def PreorderTraversal(root):
    res = []
    if root:
        res.append(root.data)
        res = res + PreorderTraversal(root.left)
        res = res + PreorderTraversal(root.right)
    return res


def PreorderTraversal2(root):
    res = []
    if root:
        res.append(root.data)
        res += PreorderTraversal2(root.left)
        res += PreorderTraversal2(root.right)
    return res


def PreorderTraversal3(root, res):
    if root:
        res.append(root.data)
        PreorderTraversal3(root.left, res)
        PreorderTraversal3(root.right, res)
    return res


def PreorderTraversal4(root, res):
    if root:
        res += str(root.data)
        res = PreorderTraversal4(root.left, res)
        res = PreorderTraversal4(root.right, res)
    return res


def PreorderTraversal5(root, res):
    if root:
        res += str(root.data)
        res += PreorderTraversal5(root.left, res)
        res += PreorderTraversal5(root.right, res)
    return res


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

ans1 = PreorderTraversal(root)
ans2 = PreorderTraversal2(root)
ans3 = PreorderTraversal3(root, [])
ans4 = PreorderTraversal4(root, ' ')
ans5 = PreorderTraversal5(root, ' ')

print(ans1, ans2, ans3, ans4, ans5)

